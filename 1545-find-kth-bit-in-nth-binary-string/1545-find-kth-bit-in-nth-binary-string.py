class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def _invert(binary_string: str):
            binary_inverted_string = ""
            for x in binary_string:
                inverted_string = "0" if x == "1" else "1"
                binary_inverted_string += inverted_string
            return binary_inverted_string

        def _reverse(binary_string: str):
            len_binary_string = len(binary_string)
            reversed_binary_string = ""
            for i in range(len_binary_string - 1, -1, -1):
                reversed_binary_string += binary_string[i]
            return reversed_binary_string
            
        def _generate(n: int):
            if n == 1:
                return "0"

            before =  _generate(n-1)
            return before + "1" + _reverse(_invert(before))

        binary_string = _generate(n)
        # print("binary_string : ", binary_string)
        len_binary_string = len(binary_string)
        for i in range(len_binary_string):
            if i+1 == k:
                return binary_string[i]