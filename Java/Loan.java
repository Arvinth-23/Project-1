import java.util.Scanner;
class loan{
    void employee(int salary,int age,int loan){

        if(salary>= 20000|| age<=25){
            System.out.println("Enter your Loan amount:");
            if(loan<=50000){
                System.out.println("Your Loan amount is eligible");
            }
            else{
                System.out.println("Your loan amount is not eligible");
            }
        }
        else{
            System.out.println("Your Not eligible for Loan");
        }

    }
    public static void main(String[] args) {
        Scanner sc=new Scanner (System.in);
        loan sub=new loan();
    System.out.println("Enter your Salary:");
     int salary=sc.nextInt();
    System.out.println("Enter your age:");
    int age=sc.nextInt();
    System.out.println("Enter your Loan amount:");
    int loan=sc.nextInt();
    sub.employee( salary,age, loan);

}
}