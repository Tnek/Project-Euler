
public class Problem5 {
	public static boolean divis(int x) {
		for (int i = 11; i <= 20; i++) {
			if (x % i != 0) { return false; }
		}
		return true;
	}
	public static void main(String[] args) {
		int i = 2520;
		while (divis(i) == false) {
			i += 2520;
		}
		System.out.println(i);
	}
}
