import java.util.Scanner;
public class Calculator{
    public static void main (String []args){
        Scanner sc = new Scanner(System .in);
        System.out.println("Enter the first Num:");
        int num1=sc.nextInt();
        System.out.println("Enter the Second Num:");
        int num2=sc.nextInt();
        while( true ){
        System.out.println("Enter your Choice :");
        System.out.println("1.ADD");
        System.out.println("2.SUBRACT");
        System.out.println("3.MULTIPLY");
        System.out.println("4.DIVIDE");
        System.out.println("5.MODULUS");
        System.out.println("6.EXIT");
        int choice=sc.nextInt();
       
        
        if (choice==1){
            System.out.println("Addition:"+(num1+num2));
        }
        else if(choice==2){
            System.out.println("Subraction:"+(num1-num2));
        }
        else if(choice==3){
            System.out.println("Multiplication:"+(num1*num2));
        }
        else if(choice==4){
            System.out.println("Division:"+(num1/num2));
        }
        else if(choice==5){
            System.out.println("Modulus:"+(num1%num2));
        }
        else if(choice==6){
            break;
        }
        else{
            System.out.println("Enter corrrect choice");
        }
    
        }
        
    }

}