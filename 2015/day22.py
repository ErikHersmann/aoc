from sys import maxsize

# Just do DP
# End of recursion:
# Dead
# worse than global best
# Boss at negative or 0 hp

# Variables to keep as arguments of DP:
# Posion duration, mana, spendature, p_shield, p_hp, b_hp

best = [maxsize]
player_hp = 50
mana = 500


def dp(
    poison,
    recharge,
    shielding,
    current_mana,
    total_mana_spent,
    player_hp,
    boss_hp,
):
    # Reduce health by one
    # check health
    # Apply effects once
    # Player action
    # Apply effects once
    # Boss damage

    for _ in range(2):
        if poison > 0:
            poison -= 1
            boss_hp -= 3
        if recharge > 0:
            recharge -= 1
            current_mana += 101
        if shielding > 0:
            shielding -= 1

    if boss_hp <= 0:
        best[0] = min(total_mana_spent, best[0])
        return
    if player_hp <= 0:
        return
    player_hp -= 2 if shielding else 9
    if current_mana >= 229 and recharge == 0:
        dp(
            poison,
            recharge + 5,
            shielding,
            current_mana - 229,
            total_mana_spent + 229,
            player_hp-1,
            boss_hp,
        )
    if current_mana >= 173 and poison == 0:
        dp(
            poison + 6,
            recharge,
            shielding,
            current_mana - 173,
            total_mana_spent + 173,
            player_hp-1,
            boss_hp,
        )
    if current_mana >= 113 and shielding == 0:
        dp(
            poison,
            recharge,
            shielding + 6,
            current_mana - 113,
            total_mana_spent + 113,
            player_hp-1,
            boss_hp,
        )
    if current_mana >= 73:
        dp(
            poison,
            recharge,
            shielding,
            current_mana - 73,
            total_mana_spent + 73,
            player_hp + 1,
            boss_hp - 2,
        )
    if current_mana >= 53:
        dp(
            poison,
            recharge,
            shielding,
            current_mana - 53,
            total_mana_spent + 53,
            player_hp-1,
            boss_hp - 4,
        )

# I just varied the hp to 55 LO
dp(0, 0, 0, 500, 0, 55, 51)
print(best[0])

# 1256 is too high