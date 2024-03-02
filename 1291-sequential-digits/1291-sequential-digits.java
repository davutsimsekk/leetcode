class Solution {
    public List<Integer> sequentialDigits(int low, int high) {


             ArrayList<Integer> result=new ArrayList<Integer>();
        result.sort(null);
        for(int i=1;i<10;i++){
            int tmp=i;
            int nextDigit=i+1;
            while (tmp<high+1 && nextDigit<10){
                
                tmp=tmp*10+nextDigit;
                if (low-1<tmp && tmp<high+1) {
                    result.add(tmp);
                }
            nextDigit+=1;
            }

        }
    result.sort(null);
    return result;
    }
}