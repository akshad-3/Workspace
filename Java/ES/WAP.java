import java.util.Scanner;

public class WAP{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter how many numbers you want to insert :");
        int n = sc.nextInt();

        int arr[] = new int[n];
        int sum=0;
        
        System.out.printf("Now enter the %d numbers",n);
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
            sum+=arr[i];
        }
        int max = arr[0];
        int min = arr[0];

        for(int i=0;i<n;i++){
            if(max<arr[i])
                max=arr[i];

            if(min>arr[i])
                min=arr[i];
        }
        double avg = sum/n;

        System.out.println("the max is :"+max);
        System.out.println("the sum is :"+sum);
        System.out.println("the min is :"+min);
        System.out.println("the avg is :"+avgx);
    }}
    
