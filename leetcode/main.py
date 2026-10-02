from itertools import product
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        base = "".join([str(x) for x in range(k)])
        chars = [c for c in base][::-1]
        unvisited = set(["".join(permutation) for permutation in product(base, repeat=n)])
        target = "0" * n
        unvisited.remove(target)
        while len(unvisited):
            # Remove only the first char of each element in unvisited
            # See if n-1 last chars of target == element
            # if so we can add chars[-1] of that element
            # Maybe we have to DP this too ?
            for c in chars:
                check = c + target[:n-1]
                if check in unvisited:
                    unvisited.remove(check)
                    target = c + target
                    break
        
        # Check all substrings of permutation with the first character removed
        # Efficient combinations
        # Never start with 00
        # Start with the biggest number: Combine 
        # ABC : [AA, AB, AC, BA, BB, BC, CA, CB, CC]
        # [AA, AB, AC, BA, BB, BC, CA, CB]
        # CCA
        # [AB, AC, BA, BB, BC, CA, CB]
        # CCAA
        # [AC, BA, BB, BC, CA, CB]
        # CCAAB
        # [AC, BA, BC, CA, CB]
        # CCAABB
        # [AC, BC, CA, CB]
        # CCAABBA
        # [BC, CA, CB]
        # CCAABBAC
        # [BC, CA]
        # CCAABBACB
        # [CA]
        # CCAABBACBC
        # []
        # CCAABBACBCA
        # Start with Biggest 
        # Take greedy thing with biggest overlap from all remaining
        # By searching remaining with window + any where window is length n - 1
        return target

sol = Solution()
print(sol.crackSafe(3, 2))