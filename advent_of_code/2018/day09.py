current_marble_idx = 0
player_count = 426#426
player_idx = player_count-1
last_marble = 72058*100
marble_id = 1
player_scores = [0 for _ in range(player_count)]
marbles = [0]
while marble_id < last_marble:
    player_idx = (player_idx+1)%player_count
    if not marble_id%23:
        player_scores[player_idx] += marble_id
        seven_counter_clockwise = (current_marble_idx - 7)%len(marbles)
        player_scores[player_idx] += marbles.pop(seven_counter_clockwise)
        current_marble_idx = seven_counter_clockwise
        marble_id += 1
        continue
    one_clockwise = (current_marble_idx + 1)%len(marbles)
    if one_clockwise == len(marbles)-1:
        marbles.append(marble_id)
        current_marble_idx = len(marbles)-1
    else:
        marbles.insert(one_clockwise+1, marble_id)
        current_marble_idx = one_clockwise+1
    marble_id += 1
    if marble_id%100000 == 0:
        print(marble_id)
print(max(player_scores))