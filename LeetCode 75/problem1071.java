package leetcode_problems;

public class problem1071 {
    public static String gcdOfStrings(String str1, String str2) {
        if (!(str1 + str2).equals(str2 + str1)) {
            return "";
        }
        int l1 = str1.length();
        int l2 = str2.length();
        int smaller = Math.min(l1, l2);
        while (smaller > 1) {
            if (l1 % smaller == 0 && l2 % smaller == 0) {
                return str1.substring(0, smaller);
            }
            smaller --;
        }
        return str1.substring(0, 1);
    }

    public static void main(String[] args) {
        System.out.println(gcdOfStrings("ABABAB", "ABAB"));
    }
}