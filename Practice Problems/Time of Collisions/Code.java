import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main implements Runnable {

	private void solve() throws IOException {
		int tc = nextInt();
		for (int i = 0; i < tc; i++) {
			solve1();
		}
	}

	int[][] ok;
	long[][] sum;
	int[] a, v;
	int n;
	final int add = 22;

	private void solve1() {
		n = nextInt();
		a = new int[n];
		v = new int[n];
		int[] cnt = new int[45];
		for (int i = 0; i < n; i++) {
			a[i] = nextInt();
			v[i] = nextInt() + add;
			cnt[v[i]]++;
		}
		ok = new int[45][];
		for (int i = 0; i < ok.length; i++) {
			ok[i] = new int[cnt[i]];
		}
		Arrays.fill(cnt, 0);
		for (int i = 0; i < n; i++) {
			int t = v[i];
			ok[t][cnt[t]++] = a[i];
		}
		for (int[] arr : ok) {
			Arrays.sort(arr);
		}

		Rational ret = Rational.ZERO;
		long[] s = new long[45];

		for (int i = 0; i < 45; i++) {
			for (int j = 0; j < i; j++) {
				s[i - j] += sum(ok[j], ok[i]);
			}
		}

		for (int i = 0; i < 45; i++) {
			if (s[i] != 0)
				ret = ret.add(new Rational(s[i], i));
		}

		out.println(ret);
	}

	long sum(int[] a, int[] b) {
		if (a.length == 0 || b.length == 0)
			return 0;
		int ind = 0;
		long res = 0, sum = 0;
		for (int i = 0; i < a.length; i++) {
			while (ind < b.length && b[ind] < a[i]) {
				sum += b[ind++];
			}
			res += -sum + (long) a[i] * ind;
		}
		return res;
	}

//	long sumHigher(int x, int num) {
//		int[] a = ok[num];
//		int l = -1, r = a.length;
//		while (r - l > 1) {
//			int m = (r + l) >> 1;
//			if (a[m] > x) {
//				r = m;
//			} else {
//				l = m;
//			}
//		}
//		int ind = r;
//		long s = sum[num][a.length] - sum[num][ind];
//		s -= (long) x * (a.length - ind);
//		return s;
//	}

	public static class Rational implements Comparable<Rational> {
		BigInteger num;
		BigInteger den;

		public static final Rational ZERO = new Rational(0);
		public static final Rational ONE = new Rational(1);
		public static final Rational POSITIVE_INFINITY = new Rational(1, 0);
		public static final Rational NEGATIVE_INFINITY = new Rational(-1, 0);

		public Rational(long num) {
			this.num = BigInteger.valueOf(num);
			this.den = BigInteger.ONE;
		}

		public Rational(long num, long den) {
			this.num = BigInteger.valueOf(num);
			this.den = BigInteger.valueOf(den);
			reduce();
		}

		public Rational(BigInteger num, BigInteger den) {
			this.num = num;
			this.den = den;
			reduce();
		}

		void reduce() {
			BigInteger gcd = num.gcd(den);
			if (gcd.signum() != 0) {
				num = num.divide(gcd);
				den = den.divide(gcd);
			}
			if (den.signum() < 0) {
				num = num.negate();
				den = den.negate();
			}
		}

		public Rational add(Rational r) {
			return new Rational(num.multiply(r.den).add(r.num.multiply(den)),
					den.multiply(r.den));
		}

		public Rational sub(Rational r) {
			return new Rational(num.multiply(r.den).subtract(
					r.num.multiply(den)), den.multiply(r.den));
		}

		public Rational mul(Rational r) {
			return new Rational(num.multiply(r.num), den.multiply(r.den));
		}

		public Rational div(Rational r) {
			return new Rational(num.multiply(r.den), den.multiply(r.num));
		}

		public Rational negate() {
			return new Rational(num.negate(), den);
		}

		public Rational inverse() {
			return new Rational(den, num);
		}

		public Rational abs() {
			return new Rational(num.abs(), den);
		}

		public int signum() {
			return num.signum();
		}

		public double doubleValue() {
			return num.doubleValue() / den.doubleValue();
		}

		public int compareTo(Rational other) {
			return (num.multiply(other.den).compareTo(other.num.multiply(den)));
		}

		public boolean equals(Object obj) {
			return obj instanceof Rational && num.equals(((Rational) obj).num)
					&& den.equals(((Rational) obj).den);
		}

		public int hashCode() {
			return num.hashCode() * 31 + den.hashCode();
		}

		public String toString() {
			if (den.equals(BigInteger.ONE)) {
				return num.toString();
			}
			if (num.compareTo(den) < 0) {
				return num + "/" + den;
			}
			return num.divide(den) + " " + num.mod(den) + "/" + den;
		}
	}

	public static void main(String[] args) {
		new Thread(new Main()).start();
	}

	BufferedReader br;
	StringTokenizer st;
	PrintWriter out;
	boolean eof = false;

	public void run() {
		Locale.setDefault(Locale.US);
		try {
			br = new BufferedReader(new InputStreamReader(System.in));
			out = new PrintWriter(System.out);
			solve();
			out.close();
		} catch (Throwable e) {
			e.printStackTrace();
			System.exit(239);
		}
	}

	String nextToken() {
		while (st == null || !st.hasMoreTokens()) {
			try {
				st = new StringTokenizer(br.readLine());
			} catch (Exception e) {
				eof = true;
				return "0";
			}
		}
		return st.nextToken();
	}

	int nextInt() {
		return Integer.parseInt(nextToken());
	}

	long nextLong() {
		return Long.parseLong(nextToken());
	}

	double nextDouble() {
		return Double.parseDouble(nextToken());
	}
}
