class example2 implements Runnable{
    public void run(){
        for(int i=0;i<=5;i++){
            System.out.println(i);
            try{
            Thread.sleep(1000);
            }
            catch(InterruptedException e){}
        }
    }
}
public class threading1 {
    public static void main(String[] args){
        Thread t1 = new Thread(new example2());
        t1.start();
    }
}
