from sys import maxsize
from math import ceil


PART = 1
boss_hp = 103
boss_dmg = 9
boss_armor = 2

player_hp = 100
weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
armors = [[13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5], [0, 0, 0]]
rings = [
    [25, 1, 0],
    [50, 2, 0],
    [100, 3, 0],
    [20, 0, 1],
    [40, 0, 2],
    [80, 0, 3],
    [0, 0, 0],
    [0, 0, 0],
]
best_cost = 0 if PART == 2 else maxsize
for weapon in weapons:
    for armor in armors:
        for ring1 in range(len(rings)):
            for ring2 in range(ring1+1, len(rings)):
                r1, r2 = rings[ring1], rings[ring2]
                player_dmg = weapon[1] + r1[1] + r2[1]
                player_armor = armor[2] + r1[2] + r2[2]
                cost = weapon[0] + armor[0] + r1[0] + r2[0]
                player_turns_required_for_bkill = ceil(boss_hp / max(player_dmg - boss_armor, 1))
                boss_turns_required_for_pkill = ceil(player_hp / max(boss_dmg - player_armor, 1))
                if PART == 1:
                    best_cost = min(best_cost, cost) if player_turns_required_for_bkill <= boss_turns_required_for_pkill else best_cost
                elif PART == 2:
                    best_cost = max(best_cost, cost) if player_turns_required_for_bkill > boss_turns_required_for_pkill else best_cost
print(f"part {PART}: {best_cost}")
