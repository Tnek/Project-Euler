public class Problem7 {
	public static boolean isprime(int x) {
		for(int i = 3; i <= Math.sqrt(x); i+=2) {
			if (x % i == 0) { return false; }
		}
		return true;
	}
	public static void main(String[] args) {
		int i = 3, count = 1;
		int[] primes = new int[10001];
		primes[0] = 2;

		while (count < 10001) {
			if (isprime(i)) { 
				primes[count] = i;
				count += 1;
			}
			i += 2;
		}
		System.out.println(primes[10000]);
	}
}

