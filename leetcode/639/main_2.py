from itertools import chain


class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        single_or_pair_map = (
            {element: 1 for element in [str(a) for a in range(1, 27)]}
            | {
                element: 0
                for element in list(
                    chain.from_iterable(
                        [
                            ["0", "0*"],
                            [str(a) for a in range(27, 100)],
                            [f"0{a}" for a in range(0, 10)],
                            [f"{a}*" for a in range(3, 10)],
                        ]
                    )
                )
            }
            | {
                "*": 9,
                "**": 15,
                "1*": 9,
                "2*": 6,
                "*0": 2,
                "*1": 2,
                "*2": 2,
                "*3": 2,
                "*4": 2,
                "*5": 2,
                "*6": 2,
                "*7": 1,
                "*8": 1,
                "*9": 1,
            }
        )

        n = len(s)
        prev = 1
        prev_prev = 0
        for pointer in range(n - 1, -1, -1):
            prev_prev, prev = (
                prev,
                (
                    (single_or_pair_map[s[pointer]] * prev) % MOD
                    + (
                        (
                            single_or_pair_map[s[pointer : pointer + 2]]
                            if pointer < n - 1
                            else 0
                        )
                        * prev_prev
                    )
                    % MOD
                )
                % MOD
            )
        return prev
