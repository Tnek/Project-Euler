public class Problem4 {
	public static boolean palindrome(int x) {
		String str = Integer.toString(x);
		StringBuilder reverse = new StringBuilder();
		for (int i = 0; i < str.length(); i++) {
			reverse.append(str.charAt(i));
		}
		return reverse.toString() == str;
	}
	public static void main(String[] args) {
		int ans = 0;
		for (int i = 100; i < 999; i++) {
			for (int j = 100; j < 999; j++) {
				if (palindrome(i * j) == true) {
					ans = i * j;
				}
			}
		}
		System.out.println(ans);
	}
}
