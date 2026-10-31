class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        wuh = [map(lambda x,y: sum(months[:int(x)-1]) + int(y), el.split("-")) for el in [arriveAlice, leaveAlice, arriveBob, leaveBob]]
        print(wuh)
        m, d = map(int, arriveAlice.split("-"))
        a_start = sum(months[:m-1]) + d
        m, d = map(int, leaveAlice.split("-"))
        a_end = sum(months[:m-1]) + d
        m, d = map(int, arriveBob.split("-"))
        b_start = sum(months[:m-1]) + d
        m, d = map(int, leaveBob.split("-"))
        b_end = sum(months[:m-1]) + d
        return 1+min(a_end, b_end)-max(b_start, a_start) if a_end >= b_start >= a_start or b_end >= a_start >= b_start else 0