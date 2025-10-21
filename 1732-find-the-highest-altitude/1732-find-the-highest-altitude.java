class Solution {
    public int largestAltitude(int[] gain) {
        int curr=0;
        int res=curr;
        for (int i=0; i<gain.length; i++){
            curr+=gain[i];
            if (curr>res){
                res=curr;
            }
        }
        return res;
    }
}