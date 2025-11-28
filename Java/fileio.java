import java.io.*;

public class fileio {
    public static void main(String[] args) {
        try {
        BufferedWriter writer = new BufferedWriter(new FileWriter("O.txt"));
        writer.write("I am writing this file after implemanting the FIle I/O.");
        writer.close();
            
        } catch (IOException e) {
            e.printStackTrace();
        }
        try{
            BufferedReader reader = new BufferedReader(new FileReader("O.txt"));
            System.out.printf(reader.readLine());
            reader.close();
        }
        catch(IOException e){
            e.printStackTrace();
        }
    }    
}
