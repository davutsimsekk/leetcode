class Solution {
    public int countDigits(int num) {
        int res =0;
        String StringNum=Integer.toString(num);

        for (int i = 0; i < StringNum.length(); i++) {
            
            if (num%(StringNum.charAt(i)-'0')==0){
                res++;
            }

        }
    return res;
    }
}