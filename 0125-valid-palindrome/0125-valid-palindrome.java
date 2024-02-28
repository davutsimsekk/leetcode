class Solution {
    public boolean isPalindrome(String s) {
    s=s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        
    StringBuilder input1= new StringBuilder();
    input1.append(s).reverse();
    return(input1.toString().equals(s));
    }
}