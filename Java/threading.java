class example extends Thread{
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
public class threading {
    public static void main(String[] args){
        example t1=new example();
        example t2=new example();
        t1.start();
        t2.start();
    }
}
