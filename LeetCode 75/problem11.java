package leetcode_problems;

public class problem11 {
    public int maxArea(int[] height) {
        int i = 0;
        int j = height.length - 1;
        int result = (j - i) *  Math.min(height[i], height[j]);

        while (i < j) {
            if (height[i] <= height[j]) {
                i++;
            } else {
                j--;
            }
            result = Math.max(result, (j - i) *  Math.min(height[i], height[j]));
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(new problem11().maxArea(new int[]{1,8,6,2,5,4,8,3,7}));
    }
}
