class Solution {
    public int[][] modifiedMatrix(int[][] matrix) {
        
        for (int i = 0; i < matrix[0].length; i++) {
            int maxOfCol=-1;
            for (int j = 0; j < matrix.length; j++) {
                
                if (matrix[j][i]>maxOfCol){
                    maxOfCol=matrix[j][i];
                }


            }

            for (int j = 0; j < matrix.length; j++) {
                if (matrix[j][i]==-1){
                    matrix[j][i]=maxOfCol;
                }
            }
        }
        return matrix;
        
    }
}