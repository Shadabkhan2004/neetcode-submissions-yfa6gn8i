class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map = new HashMap<>();
        
        for(int i=0;i<nums.length;i++){
            int no = nums[i];
            int remno = target - no;

            if(map.containsKey(remno)){
                return new int[]{map.get(remno),i};
            }

            map.put(nums[i],i);
        }

        return new int[]{};
    }
}
