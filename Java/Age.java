import java.time.LocalDate;
import java.util.Scanner;
class Age{
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your birth year:");
        int birthYear=sc.nextInt();
        int currentYear= LocalDate.now().getYear();
        int age = currentYear - birthYear;
        System.out.println(" You are " + age + " years old.");
    }

}
