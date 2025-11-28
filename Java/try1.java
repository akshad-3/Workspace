public class try1 {
    public static void main(String[] args){
        try{
            int a=5/0;
        }
        catch(Exception e){
            System.out.println("Error :"+e);
        }
        finally{
            System.out.println("Out Finally...");
        }
       throw new ArithmeticException("This is my custom error");
    }    
}
