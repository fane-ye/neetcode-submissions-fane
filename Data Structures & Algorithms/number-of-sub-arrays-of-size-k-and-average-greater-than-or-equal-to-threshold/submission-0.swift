class Solution {
    func numOfSubarrays(_ arr: [Int], _ k: Int, _ threshold: Int) -> Int {
        var avg: Double = 0
        var l: Int = 0
        var count: Int = 0
        for r in 0..<arr.count {
            avg += Double(arr[r])/Double(k)

            if (r - l + 1 == k) {
                if (avg >= Double(threshold)) {
                    count += 1
                }
                avg -= Double(arr[l])/Double(k)
                l += 1
            }
            
        }
        return count
        

    }
}
