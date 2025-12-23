from helper import problem_data

data = problem_data

T = 2503
reindeers = []
specs = []
for line in data.splitlines():
    line = line.split()
    speed, duration, rest, name = int(line[3]), int(line[6]), int(line[-2]), line[0]
    specs.append([speed, duration, rest, name])
    reindeers.append((
        ((T // (duration + rest)) * duration)
        + min((T - ((T // (duration + rest)) * (duration + rest))), duration)
    ) * speed)
print(f"Part 1: {max(reindeers)}")

# Is this POOP yet ?
reindeers = {
    idx: {
        "speed": specs[idx][0],
        "running": specs[idx][1],
        "resting": specs[idx][2],
        "currently_resting": False,
        "resting_remainder": 0,
        "running_remainder": specs[idx][1],
        "score": 0,
        "distance": 0,
        "name": specs[idx][3],
    }
    for idx in range(len(reindeers))
}
for time in range(T):
    for reindeer_idx, reindeer in reindeers.items():
        if reindeer["currently_resting"]:
            reindeer["resting_remainder"] -= 1
            if reindeer["resting_remainder"] == 0:
                reindeer["currently_resting"] = False
                reindeer["running_remainder"] = reindeer["running"]
        else:
            reindeer["distance"] += reindeer["speed"]
            reindeer["running_remainder"] -= 1
            if reindeer["running_remainder"] == 0:
                reindeer["currently_resting"] = True
                reindeer["resting_remainder"] = reindeer["resting"]
    best = None
    for idx, reindeer in reindeers.items():
        if not best or reindeer["distance"] > best[0]:
            best = [reindeer["distance"], [idx]]
        elif reindeer["distance"] == best[0]:
            best[1].append(idx)
    for idx in best[1]:
        reindeers[idx]["score"] += 1
print(f"Part 2: {max(reindeer["score"] for reindeer in reindeers.values())}")
