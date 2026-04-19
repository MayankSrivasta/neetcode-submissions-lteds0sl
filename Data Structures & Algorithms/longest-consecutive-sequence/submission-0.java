class Solution {
    public int longestConsecutive(int[] nums) {
        
		Set<Integer> numSet = new HashSet<>();
		for (int num : nums) {
			numSet.add(num);
		}

		int longest = 0;

//		100 4 200 1 3 2
		for (int n : numSet) {
			int length = 1;
			while (numSet.contains(n + length)) {
				length++;
			}
			longest = Math.max(length, longest);
		}
		return longest;
	
    }
}
