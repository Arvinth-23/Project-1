import java.util.Scanner;
public class tri{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter rows");
        int rows = sc.nextInt();
        for(int i=0;i<=rows;i++){
            for(int j=1;j<=rows-i;j++){
                System.out.print(" ");
            }
                for(int k=1;k<=i*2-1;k++){
                    System.out.print(k);
                }
                System.out.println();
            
        }

        }
}
