public class Solution {
    public int FindDuplicate(int[] nums) {
        foreach (int num in nums) {
            Console.WriteLine(num);
            if (nums[Math.Abs(num)] < 0) {
                return Math.Abs(num);
                }
            else {
                nums[Math.Abs(num)] *= -1;
            }
        }
        return -1;                   
    }
}
