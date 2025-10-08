class Car{
    String brand = "Ford";
    String modle = "Mustang";
    int year = 1969;
    boolean running = false;
}

public class object{
    public static void main(String[] args){
        Car car = new Car();

        System.out.println(car.brand);
        System.out.println(car.modle);
        System.out.println(car.year);
        System.out.println(car.running);
    }
}