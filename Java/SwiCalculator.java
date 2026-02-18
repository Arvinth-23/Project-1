import java.util.Scanner;
public class SwiCalculator{
    public static void main (String[]args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the num 1:");
        int num1= sc.nextInt();
        System.out.println("Enter the num 2:");
        int num2 = sc.nextInt();
        System.out.println("Enter the operation to be performed:");
        String input = sc.next();
        char op = input.charAt(0);

        switch(op){
            case'+':
                System.out.println("Addition:"+(num1+num2));
                break;
            case'-':
                System.out.println("Subtraction:"+(num1-num2));
                break;
            case'*':
                System.out.println("Multiplication:"+(num1*num2));
                break;
            case'/':
                System.out.println("Division:"+(num1/num2));
                break;
            case'%':
                System.out.println("Modulo:"+(num1%num2));
                break;
            default:
                System.out.println("Invalid Operation");    
             
             
             }


    }
}