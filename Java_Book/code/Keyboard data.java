import java.util.Scanner;

public class ScannerDemo {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int x = in.nextInt();
    int y = in.nextInt();
    System.out.printf("%d * %d은 %d입니다.", x,y,x*y);
  }
}

// 10 20    10 * 20 200
