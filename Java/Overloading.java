public class Overloading{
    
    //Method Overloading : it is a method with more then one same name but with diffrent PARAMITER.
    
    public static void main(String[] args){

        //System.out.println(add(1,2));
        //System.out.println(add(1,2,3));
        System.out.println(add(1,2,3,4));

    }
    static double add(double a,double b,double c,double d){
        return a+b+c+d;
    }

}