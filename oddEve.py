class Solution:
	def countOddEven(self, arr):
		#Code here
		countOdd, countEven=0,0
		for x in arr:
		    if x%2==0: countEven+=1
		    if x%2!=0: countOdd+=1
		return countOdd, countEven