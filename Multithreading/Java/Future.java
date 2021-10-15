package Multithreading.Java;

import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.ExecutionException;

class FutureDemo {
    static ExecutorService threadPool = Executors.newFixedThreadPool(2);
    public static void main(String[] args) {
        System.out.println("Sum: " + pollingStatusAndSum(10));
        threadPool.shutdown();
    }

    static int pollingStatusAndSum(int n) {
        int res = -1;

        Callable<Integer> sumTask = new Callable<Integer>(){
            public Integer call() throws Exception {
                Thread.sleep(10);
                int sum = 0;

                for (int i = 1; i <= n; i++) {
                    sum += i;
                }
                return sum;
            }
        };

        Callable<Void> randomTask = new Callable<Void>(){
            public Void call() throws Exception {
                Thread.sleep(1000 * 3600);
                return null;
            }
        };

        Future<Integer> f1 = threadPool.submit(sumTask);
        Future<Void> f2 = threadPool.submit(randomTask);

        try {
            f2.cancel(true);

            while (!f1.isDone()) {
                System.out.println("Waiting");
            }

            res = f1.get();
        } catch (InterruptedException ex) {
            System.out.println(ex.getCause());
        } catch (ExecutionException ex) {
            System.out.println(ex.getCause());
        }

        System.out.println("Second task cancelled: " + f2.isCancelled());

        return res;
    }
}
