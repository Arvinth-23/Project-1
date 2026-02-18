import java.time.LocalDate;
import java.util.Scanner;
class Ageca{
     int birthYear;


   int getinput(){
     Scanner sc = new Scanner(System.in);
     System.out.println("Enter your Birth Year");
     birthYear = sc.nextInt();
     return birthYear;

}
    void calculate(){
        int currentYear = LocalDate.now().getYear();
        int age = currentYear - birthYear;
        System.out.println("Your Age:"+age);

}
}
  public class Agecal{
     public static void main(String[] args) {
       Ageca ac = new Ageca();
       ac.getinput();
       ac.calculate();

}
 }
