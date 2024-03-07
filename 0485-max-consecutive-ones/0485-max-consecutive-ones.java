class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int result = 0 ;
        int counter = 0;
        for(int num:nums){
            if(num == 1){
                counter++;
                if (counter > result){
                    result++;
                }
            }

            else{
                counter =0;
            }
            
        }  
        
        return result;
        }
    
    }