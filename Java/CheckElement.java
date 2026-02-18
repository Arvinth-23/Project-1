 
import java.util.Scanner;

public class CheckElement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter size of array:");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println("Enter element to check:");
        int element = sc.nextInt();
        boolean found = false;
        for (int i = 0; i < n; i++) {
            if (arr[i] == element) {
                System.out.println("Element found at index: " + i);
                found = true;
                break;   
            }
        }
        if (!found) {
            System.out.println("Element is not found in the array");
        }
        sc.close();
    }
}
