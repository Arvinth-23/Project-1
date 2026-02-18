import java.util.Scanner;
public class Prime{
    public boolean isPrime(int n){
        if(n<=1){
            return false;
        }
        for (int i=2;i<=n; i++){
            if (n% i ==0){
                return false;
            }
        }
        return true;
    }
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        System.out.println(":Eneter teh number:");
        int n =sc.nextInt();
        Prime p =new Prime();
        if(p.isPrime(n)){
            System.out.println(n+"is prime number");
        }
        else{
            System.out.println(n+"is not a prime number");
        }

    }
}