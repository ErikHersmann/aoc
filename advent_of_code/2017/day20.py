from helper import problem_data
from time import sleep
from collections import deque

particles = []
for idx, line in enumerate(problem_data.splitlines()):
    line = line.split(", ")
    particles.append([tuple(map(int, x[3:].strip(">").split(","))) for x in line])
    particles[-1].append(sum(abs(x) for x in particles[-1][0]))
    particles[-1].append(idx)

# Simulate for some timesteps and just print out the top candidates and try to see a pattern
t = 0
part_1 = True

while True:
    print(f"\n{t}: {len(particles)}")
    for idx, particle in enumerate(particles):
        (pos, vel, acc, _, num) = particle
        vel = tuple(vel[i] + acc[i] for i in range(3))
        pos = tuple(pos[i] + vel[i] for i in range(3))
        particles[idx] = [pos, vel, acc, sum(abs(x) for x in pos), num]
    if not part_1:
        pos_list = [p[0] for p in particles]
        pending_removal = deque()
        for idx, pos  in enumerate(pos_list):
            if pos_list.count(pos) > 1:
                pending_removal.append(idx)
        while len(pending_removal)> 0:
            particles.pop(pending_removal.pop())
    t += 1
    for item in list(sorted(particles, key=lambda x: x[3]))[:5]:
        print(item)
