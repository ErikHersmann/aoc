class Solution:
    def numDecodings(self, s: str) -> int:
        total = 0
        MOD = 10**9 + 7
        single_or_pair_map = {
            element: 1 for element in [str(a) for a in range(1, 27)]
        }
        single_or_pair_map["*"] = 9
        single_or_pair_map["*0"] = 2
        single_or_pair_map["**"] = 15
        single_or_pair_map["*1"] = 2
        single_or_pair_map["*2"] = 2
        single_or_pair_map["*3"] = 2
        single_or_pair_map["*4"] = 2
        single_or_pair_map["*5"] = 2
        single_or_pair_map["*6"] = 2
        single_or_pair_map["*7"] = 1
        single_or_pair_map["*8"] = 1
        single_or_pair_map["*9"] = 1
        single_or_pair_map["1*"] = 9
        single_or_pair_map["2*"] = 6

        def dp(pointer, product):
            nonlocal total
            if pointer == len(s):
                total += product%MOD
                return
            if pointer < len(s) and s[pointer] != "0":
                dp(pointer+1, product * single_or_pair_map[s[pointer]])
            if pointer < len(s)-1 and (pair := s[pointer:pointer+2]) in single_or_pair_map:
                dp(pointer+2, product * single_or_pair_map[pair])

        dp(0, 1)
        return total%MOD

def main():
    sol = Solution()
    print(sol.numDecodings("*1*1*0"))

if __name__ == "__main__":
    main()