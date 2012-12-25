
public class Problem6 {
	public static void main(String[] args) {
		int squaresum = 0, sumsquare = 0;
		for (int i = 0; i <= 100; i++) {
			squaresum += i;
			sumsquare += Math.pow(i, 2);
		}
		System.out.println((int) Math.pow(squaresum, 2) - sumsquare);
	}
}
