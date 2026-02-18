import java.util.Scanner;
public class Student{
    public static void main (String []args){
        int total = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of Subject:");
        int n = sc.nextInt();
        for(int i =1; i<=n;i++){
            System.out.println("Enter the mark of subject " +i+":");
            int mark = sc.nextInt();
            total = total + mark ;
            }
            
            System.out.println("Total Mark:"+total);
            double avg = total/n;
            System.out.println("Average Mark:"+avg);
            if(avg>=90){
                System.out.println("Grade: A");
            }
            else if(avg>=80){
                System.out.println("Grade: B");
            }
            else if(avg>=70){
                System.out.println("Grade: C");
            }
            else if(avg>=60){
                System.out.println("Grade: D");
            }
            else{
                System.out.println("Grade: F");
            }
        } 

            }
