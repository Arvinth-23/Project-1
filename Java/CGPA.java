import java.util.Scanner;
class CGPA{
    void  calculate( int a,Scanner sc){
        int total_grade =0;
        int total_credit = 0;
      for(int i =1;i<= a;i++){
        System.out.println("Enter subject"+i +"grade:");
        int grade=sc.nextInt();
        System.out.println("Enter subject"+i +"credit:");
        int credit=sc.nextInt(); 
        total_grade += grade * credit;
        total_credit += credit;
        
             }
             double cg= (double)total_grade/total_credit;
             System.out.println("CGPA is :"+cg);
        
    }
    public static void main (String[]args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of subject :");
        int a= sc.nextInt();
        CGPA obj = new CGPA();
        obj.calculate(a,sc);
    }

}