class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] result = new int[nums1.length+nums2.length];
        int l = result.length;
        for(int i =0;i<nums1.length;i++)
        {
            result[i] = nums1[i];
        }
        for(int i =0;i<nums2.length;i++)
        {
            result[nums1.length+i] = nums2[i];
        }
        Arrays.sort(result);
		
        if(l% 2!=0)
        {
            return result[l/2];
        }
        else
        {
            double ans =result[l/2] + result[(l/2)-1] ;
            return ans/2;
        }
    }
}
