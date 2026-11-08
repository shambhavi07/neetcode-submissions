class Solution {
    public long countFairPairs(int[] nums, int lower, int upper) {
        Arrays.sort(nums);
        int n= nums.length;
        long count=0;

        for(int i=0; i<n; i++){
            int start=firstAtLeast(nums, lower-nums[i], i+1);
            int end = firstAtLeast(nums, upper-nums[i]+1, i+1);
            count += end-start;
        }
        return count;
    }

    private int firstAtLeast(int[] nums, int target, int left){
        int lo=left;
        int hi=nums.length;
        while (lo<hi){
            int mid= lo+(hi-lo)/2;
            if(nums[mid]>=target){
                hi=mid;
            } else {
                lo=mid+1;
            }

        }
        return lo;
    }
}
