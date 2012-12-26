public class Problem3 {
	public static boolean primecheck(long x) {
		for (int i = 3; i < Math.sqrt(x); i += 2) {
			if (x % i == 0) { return false; };
		} 
		return true;
	}
	public static void main(String[] args) {
		long x = 600851475143L, ans = 0;
		for (long i = 3; i < Math.sqrt(x); i += 2) {
			if (x % i == 0 && primecheck(i) == true) {
				ans = i;
			}
		}
		System.out.println(ans);
	}
}
