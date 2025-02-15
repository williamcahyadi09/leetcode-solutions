class ProductOfNumbers:

    def __init__(self):
        self.prefix_product = deque()
        self.last_product = 1
        self.idx = 0
        

    def add(self, num: int) -> None:
        curr = self.last_product * num
        self.prefix_product.append(curr)
        if curr == 0:
            self.last_product = 1
            self.prefix_product = deque()
            self.idx = 0
        else:
            self.last_product = curr
            self.idx+=1


    def getProduct(self, k: int) -> int:
        # print("self.prefix_product : ", self.prefix_product)
        # print("self.idx : ", self.idx)
        if k > self.idx:
            return 0
        if k == self.idx:
            return self.prefix_product[self.idx-1]
        return self.prefix_product[self.idx-1] // self.prefix_product[self.idx-1-k]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)