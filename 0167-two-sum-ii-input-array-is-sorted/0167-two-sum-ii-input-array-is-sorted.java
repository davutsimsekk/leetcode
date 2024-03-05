class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int indexone=0;
        int indextwo=numbers.length-1;
        while (indexone<indextwo){
            int value=numbers[indexone]+numbers[indextwo];
            if (value<target){
                indexone++;
            }
            else if(value>target){
                indextwo--;
            }
            else{
                break;
            }   
        }
        int[] res= {indexone+1,indextwo+1};
        return res;
    }
}