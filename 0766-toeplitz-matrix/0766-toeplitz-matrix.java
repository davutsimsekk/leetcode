class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
                
        for (int i = 0; i < matrix[0].length; i++) {
            int row=0;
            int col=i;
            int value=matrix[row][col];
            while (row<matrix.length && col<matrix[0].length) {
                if (matrix[row][col]!=value){
                    return false;
                }
                row+=1;
                col+=1;
            }
        
        }
        for (int i = 0; i < matrix.length; i++) {
            int row=i;
            int col=0;
            int value=matrix[row][col];
            while (row<matrix.length && col<matrix[0].length) {
                if (matrix[row][col]!=value){
                    return false;
                }
                row+=1;
                col+=1;
            }
        
        }
        return true;
    }
}