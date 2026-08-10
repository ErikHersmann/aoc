class Solution:
    def isNumber(self, s: str) -> bool:
        def try_int(idx):
            if not (idx < len(s) and ((has_num:= (c:= s[idx]).isnumeric()) or c == "+" or c == "-")):
                return False
            while (idx:= idx+1) < len(s)e
            return has_num and idx == len(s)
        if not((has_dot:=False) or (has_num:= (c:= s[(idx:= 0)]).isnumeric()) or c == "+" or c == "-" or (has_dot:= c == ".")):
            return False
        while (idx:= idx+1) < len(s) and ((dot:= (c:= s[idx]) == ".") or c.isnumeric()):
            if dot:
                if has_dot:
                    return False
                has_dot = True
            else:
                has_num = True
        return has_num and (idx == len(s) or (c.upper() == "E" and try_int(idx+1)))