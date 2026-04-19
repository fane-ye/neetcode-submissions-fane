class Solution {
    func minimumDifference(_ nums: [Int], _ k: Int) -> Int {
        let nums = nums.sorted()
        var _max: Int
        var _min: Int
        var diff: Int = Int.max
        var l = 0
        for r in 0..<nums.count {
            _max = nums[r]

            if (r - l + 1  == k) {
                _min = nums[l]
                diff = min(diff, (_max - _min))
                l += 1

            }

        }

        return diff

    }
}
