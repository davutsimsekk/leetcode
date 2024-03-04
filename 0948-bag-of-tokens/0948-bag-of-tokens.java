
class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        Arrays.sort(tokens);
        int res = 0;
        int indexone = 0;
        int indextwo = tokens.length - 1;
        while (indexone <= indextwo) {
            if (power >= tokens[indexone]) {
                power -= tokens[indexone];
                indexone++;
                res++;
            } else if (res > 0) {
                if (indexone == indextwo) {
                    indextwo--;
                } else {
                    power += tokens[indextwo];
                    indextwo--;
                    res--;
                }
            } else {
                indextwo--;
            }
        }
        return res;
    }
}
