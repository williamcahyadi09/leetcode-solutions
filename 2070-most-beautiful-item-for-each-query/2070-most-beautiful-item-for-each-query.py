class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        def binary_search(price_list: list, target: int):
            l = 0
            r = len(price_list) - 1
            ans = -1
            while(l <= r):
                mid = l + (r-l)//2
                if price_list[mid] <= target:
                    ans = price_list[mid]
                    l = mid + 1
                else:
                    r = mid - 1
            return ans


        items.sort()
        price_map = {}
        price_list = []
        max_beauty = -1
        for price, beauty in items:
            if price_map.get(price) is None:
                price_map[price] = 0
                price_list.append(price)
            max_beauty = max(max_beauty, beauty)
            price_map[price] = max_beauty

        ans = []
        for q in queries:
            temp = binary_search(price_list, q)
            if temp > 0:
                ans.append(price_map[temp])
            else:
                ans.append(0)
        return ans
