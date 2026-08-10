class Solution:
    def isNumber(self, s: str) -> bool:
        def try_int(idx=0, pre_e=True):
            if not ((has_num:= (c:= s[idx]).isnumeric()) or c == "+" or c == "-"):
                return False
            while (idx:= idx+1) < len(s) and (has_num:= s[idx].isnumeric()): pass
            return has_num if idx == len(s) else ((try_int(idx+1, False) if idx < (len(s) - 1) else False) if (s[idx].upper() == "E" and pre_e and has_num) else False)
        def try_float(idx=0, has_dot=False):
            if not((has_num:= (c:= s[0]).isnumeric()) or c == "+" or c == "-" or (has_dot:= c == ".")):
                return False
            while (idx:= idx+1) < len(s) and ((dot:= (c:= s[idx]) == ".") or c.isnumeric()):
                if dot:
                    if has_dot:
                        return False
                    has_dot = True
                else:
                    has_num = True
            return has_num if idx == len(s) else (try_int(idx+1, False) if idx < (len(s) - 1) else False) if (s[idx].upper() == "E" and has_num) else False
        return try_int() or try_float()