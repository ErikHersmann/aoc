with open("inpt1", "r") as f:
    data = [line.strip() for line in  f.readlines() if line.strip() != ""]

df = []
df.append((data[0][7:]).split())


for line in data[1:]:
    if ":" == line[-1]:
        df.append([])
    else:
        df[-1].append(line.split())


for line in df:
    print(line)

