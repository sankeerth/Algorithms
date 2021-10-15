def bookkeep_loans(api_inputs):
    merchant_loan_map = {}
    merchant_debt_map = {}

    create_loan = 'CREATE_LOAN'
    increase_loan = 'INCREASE_LOAN'
    pay_loan = 'PAY_LOAN'
    transaction_processed = 'TRANSACTION_PROCESSED'

    for input in api_inputs:
        api, data = input.split(':')

        if api == transaction_processed:
            merchant_id, loan_id, amount, repayment_percent = data.split(',')
            amount, repayment_percent = int(amount), float(repayment_percent)
            repay_amount = int((repayment_percent / 100) * amount)
            if (merchant_id, loan_id) not in merchant_loan_map:
                continue # no such loan for merchant
            merchant_loan_map[(merchant_id, loan_id)] -= min(repay_amount, merchant_loan_map[(merchant_id, loan_id)])
        else:
            merchant_id, loan_id, amount = data.split(',')
            amount = int(amount)
            if api == create_loan:
                if (merchant_id, loan_id) in merchant_loan_map:
                    continue # already exists
                merchant_loan_map[(merchant_id, loan_id)] = amount
            elif api == increase_loan:
                if (merchant_id, loan_id) not in merchant_loan_map:
                    continue # no such loan for merchant
                if merchant_loan_map[(merchant_id, loan_id)] > 0:
                    merchant_loan_map[(merchant_id, loan_id)] += amount
            elif api == pay_loan:
                if (merchant_id, loan_id) not in merchant_loan_map:
                    continue # no such loan for merchant
                merchant_loan_map[(merchant_id, loan_id)] -= min(amount, merchant_loan_map[(merchant_id, loan_id)])

    for key, amount in merchant_loan_map.items():
        merchant_id, loan_id = key
        merchant_id = merchant_id.lstrip()
        if amount > 0:
            if merchant_id in merchant_debt_map:
                merchant_debt_map[merchant_id] += amount
            else:
                merchant_debt_map[merchant_id] = amount

    merchant_debt_map = dict(sorted(merchant_debt_map.items()))
    for merchant_id, amount in merchant_debt_map.items():
        print(merchant_id + ',' + str(amount))

bookkeep_loans(['CREATE_LOAN: acct_foobar,loan1,5000', 'PAY_LOAN: acct_foobar,loan1,1000'])