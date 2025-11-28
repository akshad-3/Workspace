import java.util.*;

class car{
    String name;
    int price;
    void start(){
    System.out.println("The name of car is "+name+" & price is & "+price);
    }
}
public class class3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        car mycar=new car();

        mycar.name=input.nextLine();
        mycar.price=input.nextInt();
        mycar.start();
    }
}
