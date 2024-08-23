class Solution(object):
    def maxArea(self, height):
        n=len(height)
        l=0
        r=n-1
        area_max=0
        while l<r:
            w=r-l
            h=min(height[l],height[r])
            a=w*h
            area_max=max(area_max,a)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return area_max
        