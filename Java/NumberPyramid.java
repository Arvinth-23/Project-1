import java.util.Scanner;
public class pyramid{
    void  pyramid(int a){
        for (int n=1;n<=a;n++){
            for(int m=1; m<=n;m++){
                System.out.println(m);
            }
            System.out.println();
            
        }

    }
    public static void main (String[]args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enetre rows");
        int a = sc.nextInt();
        pyramid(a);
    }
}