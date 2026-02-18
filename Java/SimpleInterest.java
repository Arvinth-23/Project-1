/* this program get input from user as principal amount , intererest rate and time period and calculate 
simple interest and print the resutl on console */

import java.util.Scanner;
public class SimpleInterest{
    public static void main (String [] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the principal Amount:");
        double p = sc.nextDouble();
        System.out.println("Enter the interest rate:" + "%" +);
        double r = sc.nextDouble();
        System.out.println("Enter the time in years:");
        double t = sc.nextDouble();
        double sp = (p * r * t)/100 ;
        System.out.println("Simple Interest is :" + sp);
            }
}