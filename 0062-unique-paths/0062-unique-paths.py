class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        main_per=1
        mper=1
        nper=1
        for i in range(1,m+n-1):
            main_per*=i
            if i==m-1:
                mper=main_per
            if i==n-1:
                nper=main_per
        return main_per//(mper*nper)