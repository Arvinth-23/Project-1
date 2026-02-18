public class DigitCounter {
    public static void main(String[] args) {
        int number = 46694839;
        int count= 0;
        int temp = Math.abs(number);
        if (temp == 0) {
            count = 1; 
        } else {
            while (temp != 0) {
                temp =temp / 10;
                count++;
            }
        }
        System.out.println("The number of digits is: " + count);
    }
}
