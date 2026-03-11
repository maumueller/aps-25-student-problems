
/******************************************************************************
 *  Compilation:  javac FenwickTree.java
 *  Execution:    java FenwickTree
 *
 *  A Fenwick tree.
 *
 ******************************************************************************/

import java.util.*;
import java.io.*;

/**
 * Created by ricardodpsx@gmail.com on 4/01/15.
 * <p>
 * In {@code Fenwick Tree} structure We arrange the array in an smart way to
 * perform efficient <em>range queries and updates</em>.
 * The key point is this: In a fenwick array, each position "responsible" for
 * storing cumulative data of N previous positions (N could be 1)
 * For example:
 * array[40] stores: array[40] + array[39] ... + array[32] (8 positions)
 * array[32] stores: array[32] + array[31] ... + array[1] (32 positions)
 * <p>
 * <strong>But, how do you know how much positions a given index is
 * "responsible" for?</strong>
 * <p>
 * To know the number of items that a given array position 'ind' is responsible
 * for
 * We should extract from 'ind' the portion up to the first significant one of
 * the binary representation of 'ind'
 * for example, given ind == 40 (101000 in binary), according to Fenwick
 * algorithm
 * what We want is to extract 1000(8 in decimal).
 * <p>
 * This means that array[40] has cumulative information of 8 array items.
 * But We still need to know the cumulative data bellow array[40 - 8 = 32]
 * 32 is 100000 in binnary, and the portion up to the least significant one is
 * 32 itself!
 * So array[32] has information of 32 items, and We are done!
 * <p>
 * So cummulative data of array[1...40] = array[40] + array[32]
 * Because 40 has information of items from 40 to 32, and 32 has information of
 * items from 32 to 1
 * <p>
 * Memory usage: O(n)
 *
 * @author Ricardo Pacheco
 */
public class intOverflow {

	int[] array; // 1-indexed array, In this array We save cumulative information to perform
			// efficient range queries and updates

	public intOverflow(int size) {
		array = new int[size + 1];
	}

	/**
	 * Range Sum query from 1 to ind
	 * ind is 1-indexed
	 * <p>
	 * Time-Complexity: O(log(n))
	 *
	 * @param ind index
	 * @return sum
	 */
	public int rsq(int ind) {
		assert ind > 0;
		int sum = 0;
		while (ind > 0) {
			sum += array[ind];
			// Extracting the portion up to the first significant one of the binary
			// representation of 'ind' and decrementing ind by that number
			ind -= ind & (-ind);
		}

		return sum;
	}

	/**
	 * Range Sum Query from a to b.
	 * Search for the sum from array index from a to b
	 * a and b are 1-indexed
	 * <p>
	 * Time-Complexity: O(log(n))
	 *
	 * @param a left index
	 * @param b right index
	 * @return sum
	 */
	public int rsq(int a, int b) {
		assert b >= a && a > 0 && b > 0;

		return rsq(b) - rsq(a - 1);
	}

	/**
	 * Update the array at ind and all the affected regions above ind.
	 * ind is 1-indexed
	 * <p>
	 * Time-Complexity: O(log(n))
	 *
	 * @param ind   index
	 * @param value value
	 */
	public void update(int ind, int value) {
		assert ind > 0;
		while (ind < array.length) {
			array[ind] += value;
			// Extracting the portion up to the first significant one of the binary
			// representation of 'ind' and incrementing ind by that number
			ind += ind & (-ind);
		}
	}

	public int size() {
		return array.length - 1;
	}

	/**
	 * Read the following commands:
	 * init n Initializes the array of size n all zeroes
	 * set a b c Initializes the array with [a, b, c ...]
	 * rsq a b Range Sum Query for the range [a,b]
	 * up i v Update the i position of the array with value v.
	 * exit
	 * <p>
	 * The array is 1-indexed
	 * Example:
	 * set 1 2 3 4 5 6
	 * rsq 1 3
	 * Sum from 1 to 3 = 6
	 * rmq 1 3
	 * Min from 1 to 3 = 1
	 * input up 1 3
	 * [3,2,3,4,5,6]
	 *
	 * @param args the command-line arguments
	 */
	public static void main(String[] args) throws Exception {
		var scanner = new Reader();
		var N = scanner.nextInt();
		var M = scanner.nextInt();
		var sq = new intOverflow(N);
		var m = new HashMap<String, Integer>();
		for (int i = 0; i < N; i++) {
			var inp = scanner.readLine().split(" ");
			var amount = Integer.parseInt(inp[0]);
			var builder = new StringBuilder();
			builder.append(inp[1]);

			for (int j = 2; j < inp.length; j++) {
				builder.append(" ");
				builder.append(inp[j]);
			}
			m.put(builder.toString(), i + 1);
			sq.update(i + 1, amount);
		}
		var stringBuilder = new StringBuilder();
		for (int i = 0; i < M; i++) {
			var inp = scanner.readLine();
			if (inp.equals("calculate")) {
				var fst = m.get(scanner.readLine());
				var snd = m.get(scanner.readLine());
				int answer = sq.rsq(fst, snd);
				stringBuilder.append(answer);
				stringBuilder.append("\n");
			} else {
				var input = scanner.readLine().split(" ");
				var n = Integer.parseInt(input[0]);
				var builder = new StringBuilder();
				builder.append(input[1]);

				for (int j = 2; j < input.length; j++) {
					builder.append(" ");
					builder.append(input[j]);
				}
				var taskNumber = m.get(builder.toString());
				sq.update(taskNumber, n);
			}
		}
		System.out.println(stringBuilder.toString());
	}

	static class Reader {
		final private int BUFFER_SIZE = 1 << 16;
		private DataInputStream din;
		private byte[] buffer;
		private int bufferPointer, bytesRead;

		public Reader() {
			din = new DataInputStream(System.in);
			buffer = new byte[BUFFER_SIZE];
			bufferPointer = bytesRead = 0;
		}

		public Reader(String file_name) throws IOException {
			din = new DataInputStream(
					new FileInputStream(file_name));
			buffer = new byte[BUFFER_SIZE];
			bufferPointer = bytesRead = 0;
		}

		public String readLine() throws IOException {
			byte[] buf = new byte[64]; // line length
			int cnt = 0, c;
			while ((c = read()) != -1) {
				if (c == '\n') {
					if (cnt != 0) {
						break;
					} else {
						continue;
					}
				}
				buf[cnt++] = (byte) c;
			}
			return new String(buf, 0, cnt);
		}

		public int nextInt() throws IOException {
			int ret = 0;
			byte c = read();
			while (c <= ' ') {
				c = read();
			}
			boolean neg = (c == '-');
			if (neg)
				c = read();
			do {
				ret = ret * 10 + c - '0';
			} while ((c = read()) >= '0' && c <= '9');

			if (neg)
				return -ret;
			return ret;
		}

		public long nextLong() throws IOException {
			long ret = 0;
			byte c = read();
			while (c <= ' ')
				c = read();
			boolean neg = (c == '-');
			if (neg)
				c = read();
			do {
				ret = ret * 10 + c - '0';
			} while ((c = read()) >= '0' && c <= '9');
			if (neg)
				return -ret;
			return ret;
		}

		public double nextDouble() throws IOException {
			double ret = 0, div = 1;
			byte c = read();
			while (c <= ' ')
				c = read();
			boolean neg = (c == '-');
			if (neg)
				c = read();

			do {
				ret = ret * 10 + c - '0';
			} while ((c = read()) >= '0' && c <= '9');

			if (c == '.') {
				while ((c = read()) >= '0' && c <= '9') {
					ret += (c - '0') / (div *= 10);
				}
			}

			if (neg)
				return -ret;
			return ret;
		}

		private void fillBuffer() throws IOException {
			bytesRead = din.read(buffer, bufferPointer = 0,
					BUFFER_SIZE);
			if (bytesRead == -1)
				buffer[0] = -1;
		}

		private byte read() throws IOException {
			if (bufferPointer == bytesRead)
				fillBuffer();
			return buffer[bufferPointer++];
		}

		public void close() throws IOException {
			if (din == null)
				return;
			din.close();
		}
	}

}
