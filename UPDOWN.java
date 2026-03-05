/* This program is used to get input from User and chaeck if number is greater than or lesser than or equal to 
according works   i*/
import java.lang.*;
import java.util.*;
class UPDOWN
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();  
		while(t-- > 0){
			int c = sc.nextInt();
			if(c > 7){
				System.out.println("UP");
			}
			else if (c == 7){
				System.out.println("EQUAL");
			}
			else{
				System.out.println("DOWN");
			}
		}
		sc.close();
	}
}