# sort 보다 max, min이 시간복잡도가 더 짧다
# nums.sort() : O(NlogN)
# max, min: O(N)

def maxTwoDiff(nums):
    return abs(max(nums) - min(nums))
    
def main():
    print(maxTwoDiff([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23])) # 49가 리턴되어야 합니다.

if __name__ == "__main__":
    main()
