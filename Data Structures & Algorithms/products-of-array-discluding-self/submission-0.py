class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productList = []

        for i, num in enumerate(nums):
            product = 1
            for j, n in enumerate(nums):
                if j == i:
                    continue
                product *= n
            productList.append(product)
        return productList