class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        appendingList=list()
        mostCandies=0
        # identify the kid w/ the most candy
        for i in candies:
            if i>mostCandies:
                mostCandies=i
                
        for i in candies:
            if i+extraCandies>=mostCandies:
                appendingList.append(True)
            else:
                appendingList.append(False)
        return appendingList
