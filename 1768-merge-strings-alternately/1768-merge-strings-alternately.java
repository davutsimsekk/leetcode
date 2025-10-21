class Solution {
    public String mergeAlternately(String word1, String word2) {
        int l=0;
        int r=0;
        int i=0;
        String res="";
        while(l<word1.length() && r<word2.length()){
            if (i%2==0){
                res+=word1.charAt(l);
                l++;
            }
            else{
                res+=word2.charAt(r);
                r++;
            }
            i++;
        }

        while (r<word2.length()){
            res+=word2.charAt(r);
            r++;
        }
        while (l<word1.length()){
            res+=word1.charAt(l);
            l++;
        }
        


        return res;

    }
}