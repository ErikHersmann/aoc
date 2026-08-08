def knot_hash(input_string):
    def one_round(numbers, cur, skip):
        for length in lengths:
            for idx in range(length // 2):
                left, right = (cur + idx) % maxnum, (cur + length - 1 - idx) % maxnum
                numbers[left], numbers[right] = numbers[right], numbers[left]
            cur = (length + skip + cur) % maxnum
            skip += 1
        return (cur, skip)

    def calculate_dense_hash(numbers):
        result = []
        for idx in range(0, 256, 16):
            temp = numbers[idx]
            for idx2 in range(idx + 1, idx + 16):
                temp ^= numbers[idx2]
            result.append(temp)
        return "".join([(hex(num)[2:]).zfill(2) for num in result])

    maxnum = 256
    lengths = [ord(x) for x in input_string] + [17, 31, 73, 47, 23]
    cur, skip, round_idx = 0, 0, 0
    sparse_hash = list(range(maxnum))
    while round_idx < 64:
        (cur, skip) = one_round(sparse_hash, cur, skip)
        round_idx += 1
    return calculate_dense_hash(sparse_hash)
