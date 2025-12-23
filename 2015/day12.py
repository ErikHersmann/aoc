from json import load

def dfs(element, part_two: bool):
    match element:
        case dict():
            return sum([dfs(element[child], part_two) for child in element])if (part_two and "red" not in element.values()) else 0
        case list():
            return sum([dfs(child, part_two) for child in element])
    return element if isinstance(element, int) else 0

with open("input.txt", "r") as f:
    blob = load(f)
print("\n".join(f"Part {idx}: {dfs(blob, idx==2)}" for idx in [1, 2]))
