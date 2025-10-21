class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        HashSet<Integer> nums1Set=new HashSet<Integer>();
        HashSet<Integer> nums2Set=new HashSet<Integer>();
        for (int i=0;i<nums1.length;i++){
            nums1Set.add(nums1[i]);
        }
        for (int i=0;i<nums2.length;i++){
            nums2Set.add(nums2[i]);
        }

        List<Integer> diff1 = new ArrayList<>(nums1Set);
        diff1.removeAll(nums2Set);

        List<Integer> diff2 = new ArrayList<>(nums2Set);
        diff2.removeAll(nums1Set);

        return Arrays.asList(diff1,diff2);
        
        
    }
}