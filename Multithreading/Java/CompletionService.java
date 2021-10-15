package Multithreading.Java;

import java.util.Random;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorCompletionService;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

class CompletionService {
    public static void main(String[] args) throws Exception {
        completionService();
    }
    
    static void completionService() throws InterruptedException, ExecutionException {
        ExecutorService threadPool = Executors.newFixedThreadPool(3);
        ExecutorCompletionService<Integer> service = new ExecutorCompletionService<>(threadPool);

        for (int i = 0; i < 10; i++) {
            service.submit(new Task(i), i);
        }

        int count = 10;
        while (count > 0) {
            Future<Integer> f = service.poll();
            if (f != null) {
                System.out.println("Thread " + f.get() + " got done");
                count -= 1;
            }
        }

        threadPool.shutdown();
    }
}

class Task implements Runnable {
    Random random = new Random(System.currentTimeMillis());
    int n;

    public Task(int n) {
        this.n = n;
    }

    public void run() {
        try {
            Thread.sleep(random.nextInt(101));
            System.out.println("res: " + n * n);
        } catch (InterruptedException ex) {
            ex.printStackTrace();
        }
    }
}
