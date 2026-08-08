from helper import transform, UP, DOWN, LEFT, RIGHT, TL, TR, BR, BL

problem_data = 325489


print("Part 1:", abs((n:=325489)-([x for i in range(4)if(x:=(l:=(f**2 if(f:=int(n**0.5))%2 else(f:=f-1)**2))+(s:=((f+2)**2-l)//4)*i)<n][-1]+s//2))+((f+1)//2))
side_idx = 0
side_length = 2
x, y = 1, 0
positions = {(0, 0): 1}
n_dirs = [DOWN, LEFT, BL, TL]
direction = UP
t = transform

while True:
    side_idx = 0
    while side_idx < 4:
        side_position = 0
        while side_position < side_length:
            positions[(x, y)] = sum([positions[key] for t_dir in [t(direction, x) for x in n_dirs] if (key:= (x+t_dir[0], y+t_dir[1])) in positions])
            if positions[(x, y)] > problem_data:
                print(f"Part 2: {positions[(x, y)]}")
                exit()
            side_position += 1
            if side_position < side_length:
                x += direction[0]
                y += direction[1]
        side_idx += 1
        if side_idx == 4:
            x += direction[0]
            y += direction[1]
            direction = t(direction, LEFT)
        else:
            direction = t(direction, LEFT)
            x += direction[0]
            y += direction[1]
    side_length += 2
