
import java.util.Scanner;

class BalloonColors {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt(); // Read the number of test cases
        
        for (int i = 0; i < T; i++) {
            String s = scanner.next(); // Read the string
            
            int countA = 0; // Count of 'a' balloons
            int countB = 0; // Count of 'b' balloons
            
            for (char c : s.toCharArray()) {
                if (c == 'a') {
                    countA++;
                } else if (c == 'b') {
                    countB++;
                }
            }
            
            int minFlips = Math.min(countA, countB); // Minimum number of flips
            
            System.out.println(minFlips);
        }
        
        scanner.close();
    }
}
