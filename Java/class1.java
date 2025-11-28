class Car{
    String name;
    int price;
    void drive(){
        System.out.printf("Driving the car....\nname : %s",name);
    }
}
public class class1{
    public static void main(String args[]){
        Car mycar=new Car();
        mycar.name="Mazada";
        mycar.price=1200000;
        mycar.drive();
    }
}