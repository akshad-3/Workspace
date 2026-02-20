import java.io.IOException;
import java.io.*;

public class readline{
    public static void main(String[] args)
        throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.println("Enter the name and age :");
        String name = br.readLine();
        int age = Integer.parseInt(br.readLine());

        System.out.println("the name and age is :"+name+age);
    }
}