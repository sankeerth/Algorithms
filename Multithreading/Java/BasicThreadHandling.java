package Multithreading.Java;

class Demonstration {
    public static void main(String []args) throws InterruptedException {
        ExecuteMe executeMe = new ExecuteMe();
        Thread innThread = new Thread(executeMe);
        innThread.start();
        System.out.println("Main thread sleeping at: " + System.currentTimeMillis());
        Thread.sleep(5000);
        innThread.interrupt();
        System.out.println("Main thread exiting at: " + System.currentTimeMillis());
    }
}

class ExecuteMe implements Runnable {
    @Override
    public void run() {
        try {
            System.out.println("InnerThread sleep at: " + System.currentTimeMillis());
            Thread.sleep(1000 * 1000);
        } catch (InterruptedException e) {
            System.out.println("InnerThread interrupted at: " + System.currentTimeMillis());
        }
    }
}

/*
class Demonstration {
    public static void main(String []args) {
        ExecuteMe executeMe = new ExecuteMe();
        Thread innThread = new Thread(executeMe);
        innThread.setDaemon(true);
        innThread.start();
    }
}

class ExecuteMe implements Runnable {
    @Override
    public void run() {
        int count = 0;
        while (count < 5) {
            count += 1;
            System.out.println("Hello again");

            try {
                Thread.sleep(500);
            } catch (InterruptedException ex) {
                // do nothing
            }
        }
    }
}
*/
