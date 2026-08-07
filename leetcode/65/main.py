class Solution:
    def isNumber(self, s: str) -> bool:
        def try_to_match_as_int(idx, before_e):
            encountering_e_is_valid = False
            encountered_a_number = False
            if idx == len(s):
                return False
            if s[idx].isnumeric():
                encountering_e_is_valid = True and before_e
                encountered_a_number = True
                idx += 1
            elif s[idx] in ["+", "-"]:
                idx += 1
            else:
                return False
            while idx < len(s) and s[idx].isnumeric():
                encountering_e_is_valid = True and before_e
                encountered_a_number = True
                idx += 1
            if idx == len(s):
                return encountered_a_number
            if s[idx] in ["e", "E"]:
                if encountering_e_is_valid:
                    return try_to_match_as_int(idx+1, False)
            return False
        def try_to_match_as_decimal(idx, before_e):
            encountering_e_is_valid = False
            encountering_dot_is_valid = True
            if s[idx].isnumeric():
                encountering_e_is_valid = True and before_e
                idx += 1
            elif s[idx] in ["+", "-"]:
                idx += 1
            elif s[idx] == ".":
                encountering_dot_is_valid = False
                idx += 1
            else:
                return False
            while idx < len(s) and (s[idx].isnumeric() or s[idx] == "."):
                if s[idx] == ".":
                    if not encountering_dot_is_valid:
                        return False
                    encountering_dot_is_valid = False
                else:
                    encountering_e_is_valid = True and before_e
                idx += 1
            if idx == len(s):
                return encountering_e_is_valid
            if s[idx] in ["e", "E"]:
                if encountering_e_is_valid:
                    return try_to_match_as_int(idx+1, False)
            return False
        if not try_to_match_as_int(0, True):
            return try_to_match_as_decimal(0, True)
        return True


sol = Solution()
# for number in ["-1E+3", "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]:
#     assert sol.isNumber(number)
for number in ["4e+", "-.E3", "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]:
    assert not sol.isNumber(number)

#     An integer number followed by an optional exponent.
#     A decimal number followed by an optional exponent.


# An integer number is defined with an optional sign '-' or '+' followed by digits.
# A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:
#     Digits followed by a dot '.'.
#     Digits followed by a dot '.' followed by digits.
#     A dot '.' followed by digits.
# An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.
# The digits are defined as one or more digits.