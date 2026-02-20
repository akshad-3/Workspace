
public class atoverride{
    public static void main(String[] args){
        class animal{
    public void thisistheclasss(){
        System.out.println("this is the methos from the animal class");
    }
}
class dog extends animal{
    @Override
    public void thisistheclass(){
        System.out.println("this is the method from the dog class");
    }
}
    dog dogesh = new dog();
    dogesh.thisistheclass();
    }
}