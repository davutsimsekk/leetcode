class Solution {
    public int minimumLength(String s) {
        int indexone=0;
        int indextwo=s.length()-1;
        while (indexone<indextwo){
            if (s.charAt(indexone)==s.charAt(indextwo)){
                char value=s.charAt(indexone);
                while (s.charAt(indexone)==value && indexone<=indextwo) {
                    indexone++;
                    if (indexone==s.length()-1){
                        return 0;
                    }
                }
                while (s.charAt(indextwo)==value && indexone<=indextwo) {
                    
                    indextwo--;
                    if (indextwo==0){
                        return 0;
                    }
                }
            

            }
            else{
                break;
            }
        
        }
 
            return indextwo-indexone+1;
        
    }
}