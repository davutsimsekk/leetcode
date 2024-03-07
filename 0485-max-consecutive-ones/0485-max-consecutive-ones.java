class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int counter=0;
        int result=0;
        for(int i:nums){
            if(i==1){
                counter+=1;
                
            }
            else {
                result=Math.max(result,counter);
                counter=0;
            }
            
            
        }
        result=Math.max(result,counter);
        return result;
    }
}