from copy import deepcopy

number_of_intersections, number_of_streets = map(int, input().split())
start, target, delay, george_number_of_intersections = map(int, input().split())
george_intersections = list(map(int, input().split()))
george = []
intersections = {}
for _ in range(number_of_streets):
    first_intersection, second_intersection, traversal_time = map(int, input().split())
    if first_intersection not in intersections:
        intersections[first_intersection] = {}
    if second_intersection not in intersections:
        intersections[second_intersection] = {}
    intersections[first_intersection][second_intersection] = traversal_time
    intersections[second_intersection][first_intersection] = traversal_time


delay *= -1
for idx in range(1, len(george_intersections)):
    g_start, end = george_intersections[idx-1], george_intersections[idx]
    george.append([sorted([g_start, end]), delay, delay + intersections[g_start][end]])
    delay += intersections[g_start][end]
    if delay < 0:
        george.pop(-1)


best = [100000000]

def dp(cur, time, visited):
    if time >= best[0]:
        return
    if cur == target:
        best[0] = min(best[0], time)
        return
    if cur not in intersections:
        return
    for next_station in intersections[cur]:
        if next_station in visited:
            continue
        end = time + intersections[cur][next_station]
        for george_route in george:
            (buh, g_st_t, g_end_t) = george_route
            if sorted([cur, next_station]) == buh and g_st_t <= time <= g_end_t:
                end = g_end_t + intersections[cur][next_station]
                break
        next_set = deepcopy(visited)
        next_set.add(next_station)
        dp(next_station, end, next_set)

dp(start, 0, set([start]))
print(best[0])