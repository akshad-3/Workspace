import java.util.*;
public class arrays{

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String[] user= new String[4];

        for(int i=0;i<4;i++){
            System.out.print("Enter the item "+i+" :");
            user[i]=scanner.nextLine();
        }
        for(String users : user){

            System.out.println(users);
        }
    }
}