import argparse
import os
import sys
import subprocess
import re
import dateutil.parser
from os.path import expanduser
from datetime import datetime, timedelta

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
FAULT_ANALYSIS_DIR = 'FAULT_ANALYSIS'
APPLICATION_LOGS_FILE = 'application_logs_for_{}.txt'
REQUEST_IDS_FOR_EXCEPTION = 'requestIds_for_{}.txt'
FAULT_SERVICE_LOGS_FILE = 'service_log_faults.txt'
FAULT_ACCOUNT_FILE = 'accountId_with_faults.txt'
FAULT_EXCEPTION = 'exceptions.txt'
FAULT_INSTANCE = 'instance_with_exceptions.txt'
NO_EXCEPTION_FILE = 'no_exception'

class esv2_fault_analyzer(object):
    def __init__(self, start_time, end_time, service_name):
        self.start_time = start_time
        self.end_time = end_time
        self.service_name = service_name
        self.metric_names = {}

    def analyze(self):
        self.create_directory()
        self.initialize_metric_names()
        
        # Analyze faults if only there were any during the time period
        if not self.retrieve_fault_service_logs():
            print('No faults found during the provided time period')
            return

        self.analyze_fault_service_logs()

    def create_directory(self):
        print('\n===== Creating working directory =====\n')

        # Get the base directory path for user and create a directory with FAULT_ANALYSIS
        home = expanduser("~")
        base_directory = home + '/' + FAULT_ANALYSIS_DIR
        if not os.path.exists(base_directory):
            os.mkdir(base_directory)

        os.chdir(base_directory)

        folder_name = '{}_faults_{}_{}'.format(self.service_name, self.start_time, self.end_time)
        print('Creating a folder with name {} for analyzing {} faults from {} to {}'.format(folder_name, self.service_name, self.start_time, self.end_time))
        if not os.path.exists(folder_name):
        	os.mkdir(folder_name)

        os.chdir(folder_name)

    def initialize_metric_names(self):
        # Initialize the metric names for ES and ESv2 service log since they are different in few cases
        self.metric_names['es'], self.metric_names['es'] = {}, {}
        self.metric_names['es'], self.metric_names['esv2'] = {}, {}
        
        # ApiId
        self.metric_names['es']['api_id'] = 'RestapiId'
        self.metric_names['esv2']['api_id'] = 'ApiId'

        # ExceptionName
        self.metric_names['es']['exception_name'] = 'ExceptionSimpleName'
        self.metric_names['esv2']['exception_name'] = 'BackplaneException'

        # HostName
        self.metric_names['es']['host_name'] = 'Host'
        self.metric_names['esv2']['host_name'] = 'Hostname'

        # Operation
        self.metric_names['es']['operation'] = 'Operation'
        self.metric_names['esv2']['operation'] = 'Method'

        # RequestId
        self.metric_names['es']['request_id'] = 'RequestId'
        self.metric_names['esv2']['request_id'] = 'BackplaneRequestId'

    def analyze_fault_service_logs(self):
        self.account_and_api_details_for_faults()
        self.exception_details_for_faults()
        self.instance_details_for_faults()

        fault_exceptions_file = open(FAULT_EXCEPTION, 'r+', encoding='utf-8')
        exception_lines = fault_exceptions_file.read().splitlines()

        count = 0
        for line in exception_lines[1:-1]: # Omitting first and last line since it is the output of SQ
            if count < 3: # Getting app logs and stack trace for top 3 exceptions

                # Getting exception name and remove color characters
                exceptionName = line.split(None, 1)[0].strip("$'\033'\[m")

                # Getting request ids for the exception
                self.get_request_ids_for_exception(exceptionName)

                # Printing stack trace of the first request with this exception
                self.print_and_save_stack_trace(exceptionName)

                count = count + 1

    def account_and_api_details_for_faults(self):
        print('\n===== Retrieving accountId and apis affected by faults =====\n')

        api_id = self.metric_names[self.service_name]['api_id']
        host_name = self.metric_names[self.service_name]['host_name']
        operation = self.metric_names[self.service_name]['operation']

        query = "SELECT AccountId, {}::string, {}::string, {}::string, count(1) as faults \
        FROM read('{}') GROUP BY AccountId, {}::string, {}::string, {}::string \
        ORDER BY faults DESC SINK TO file('{}'), TO console" \
        .format(api_id, host_name, operation, FAULT_SERVICE_LOGS_FILE, api_id, host_name, operation, FAULT_ACCOUNT_FILE)

        cmd = 'sqsh -16 -c "{}"'.format(query)
        print(cmd)
        os.system(cmd)

    def exception_details_for_faults(self):
        print('\n===== Retrieving exceptions caused by faults =====\n')

        exception_name = self.metric_names[self.service_name]['exception_name']

        query = "SELECT {}::string, count(1) as faults FROM read('{}') GROUP BY {}::string ORDER BY faults DESC SINK TO file('{}'), TO console". \
        format(exception_name, FAULT_SERVICE_LOGS_FILE, exception_name, FAULT_EXCEPTION)

        cmd = 'sqsh -16 -c "{}"'.format(query)
        print(cmd)
        os.system(cmd)

    def instance_details_for_faults(self):
        print('\n===== Retrieving instance details for faults =====\n')

        query = "SELECT InstanceId, AvailabilityZone, count(1) as faults FROM read('{}') GROUP BY \
        InstanceId, AvailabilityZone ORDER BY faults DESC LIMIT 10 SINK TO file('{}'), TO console". \
        format(FAULT_SERVICE_LOGS_FILE, FAULT_INSTANCE)

        cmd = 'sqsh -16 -c "{}"'.format(query)
        print(cmd)
        os.system(cmd)

    def get_request_ids_for_exception(self, exception):
        print('\n===== Retrieving request ids for exception =====\n')

        request_id = self.metric_names[self.service_name]['request_id']
        exception_name = self.metric_names[self.service_name]['exception_name']

        # ExceptionSimpleName can also be NULL in certain cases
        if not exception:
            query = "SELECT {}::string, StartTime, Time FROM read('{}') WHERE {}::string IS NULL LIMIT 5 SINK TO file('{}')". \
            format(request_id, FAULT_SERVICE_LOGS_FILE, exception_name, REQUEST_IDS_FOR_EXCEPTION.format(NO_EXCEPTION_FILE))
        else:
            query = "SELECT {}::string, StartTime, Time FROM read('{}') WHERE {}::string='{}' LIMIT 5 SINK TO file('{}')". \
            format(request_id, FAULT_SERVICE_LOGS_FILE, exception_name, exception, REQUEST_IDS_FOR_EXCEPTION.format(exception))

        cmd = 'sqsh -16 -c "{}"'.format(query)
        print('Getting requestIds for {}...'.format(exception))
        print(cmd)
        os.system(cmd)

    def print_and_save_stack_trace(self, exception):
        print('\n===== Stack trace from application log =====\n')

        # ExceptionSimpleName can also be NULL in certain cases
        if not exception:
            exception = NO_EXCEPTION_FILE

        try:
            with open(REQUEST_IDS_FOR_EXCEPTION.format(exception), 'r+', encoding='utf-8') as request_id_file:
                # reading first request id for the exception
                request_id_entry_line = request_id_file.read().splitlines()[1]
                split_values = request_id_entry_line.split()
                request_id = split_values[0].strip("$'\033'\[m").rstrip()
                start_time_str = split_values[1]
                start_time = dateutil.parser.parse(start_time_str)
                start_time_str = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
                end_time = dateutil.parser.parse(start_time_str) + timedelta(seconds=60)
                end_time_str = end_time.strftime("%Y-%m-%dT%H:%M:%SZ")
                
                # retriving app log
                query = "SELECT raw FROM {}_application_log WHERE Timestamp >= datetime('{}') AND \
                Timestamp < datetime('{}') AND raw=~'{}' SINK TO file('{}')". \
                format(self.service_name, start_time_str, end_time_str, request_id, APPLICATION_LOGS_FILE.format(request_id))
                
                cmd = 'sqsh -16 -c "{}"'.format(query)
                print('Getting application logs for {} and printing failure causes'.format(request_id))
                print(cmd)                
                os.system(cmd)

                cmd = 'tr -d "\n\r" < {} | cat {}'.format(APPLICATION_LOGS_FILE.format(request_id), APPLICATION_LOGS_FILE.format(request_id))
                os.system(cmd)

        except IOError:
            print('No file found with exceptions causing faults')

    def retrieve_fault_service_logs(self):
        print('\n===== Retrieving service logs for faults =====\n')

        query = "SELECT raw FROM {}_service_log WHERE EndTime >= datetime('{}') AND EndTime < datetime('{}') AND Counters#Fault=1 SINK TO file('{}')". \
        format(self.service_name, self.start_time, self.end_time, FAULT_SERVICE_LOGS_FILE)

        cmd = 'sqsh -16 -c "{}"'.format(query)
        print(cmd)
        os.system(cmd)

        if not os.path.exists(FAULT_SERVICE_LOGS_FILE):
            print('Faults service_log file not created. Exiting ...')
            return False

        line_count = int(os.popen('wc -l {}'.format(FAULT_SERVICE_LOGS_FILE)).read().split(' ')[0])
        # There will be more than 5 lines in the file if there were any faults
        return True if line_count > 5  else False        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(sys.argv)
    parser.add_argument('-s', '--start_time', required=False, help='Start time of the request, for ex: 2020-05-20T02:10:00Z in UTC')
    parser.add_argument('-e', '--end_time', required=False, help='End time of the request, for ex: 2020-05-20T02:30:00Z in UTC')
    parser.add_argument('-n', '--service_name', required=True, help='Service name, for ex: "es", "esv2"')
    options = parser.parse_args()

    if not options.start_time or not options.end_time:
        time_before_5_mins = datetime.now() - timedelta(minutes=5)
        time_before_20_mins = datetime.now() - timedelta(minutes=20)
        options.start_time = time_before_20_mins.strftime(DATETIME_FORMAT)
        options.end_time = time_before_5_mins.strftime(DATETIME_FORMAT)

    if options.service_name not in ['es', 'esv2']:
        print('Service name has to be one among es or esv2')
        exit(0)

    ca = esv2_fault_analyzer(options.start_time, options.end_time, options.service_name)
    ca.analyze()
