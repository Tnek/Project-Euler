
public class Problem2 {
	public static double pow(double x, int y) {
		if (y == 0) { 
			return 1;
		}
		return x * pow(x, y-1);	
	}
	public static void main(String[] args) {
		double phi = (1 + Math.sqrt(5)) / 2;
		double psi = (1 - Math.sqrt(5)) / 2;
		System.out.println(Math.round((((pow(phi, 35)  + pow(psi, 35)) / Math.sqrt(5)) - 1) / 2));
		
	}
}
