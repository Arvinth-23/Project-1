import java.util.Scanner;

public class AddElementUserInput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of elements: ");
        int size = sc.nextInt();
        int[] arr = new int[size];
        System.out.println("Enter elements:");
        for (int i = 0; i < size; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.print("Enter element to add: ");
        int newElement = sc.nextInt();
        int[] newArr = new int[size + 1];
        for (int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }
        newArr[size] = newElement;
        System.out.println("New array is:");
        for (int i = 0; i < newArr.length; i++) {
            System.out.print(newArr[i] + " ");
        }
        sc.close();
    }
}
