import math


def generate_sequence(m: int):
    h = 2 * m - 1
    matrix = [[0] * h for _ in range(h)]

    # Define movement directions
    rotations = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]

    # Set center element
    matrix[m - 1][m - 1] = 1  # Python uses 0-based indexing
    print(1, end=", " if 1 != (h - 2) ** 2 else "")

    for n in range(1, (h - 2) ** 2):
        g = int(math.sqrt(n))
        r = (g + g % 2) // 2
        q = 4 * r**2
        d = n - q

        # Determine position based on n
        if n <= q - 2 * r:
            j = d + 3 * r
            k = r
        elif n <= q:
            j = r
            k = -d - r
        elif n <= q + 2 * r:
            j = r - d
            k = -r
        else:
            j = -r
            k = d - 3 * r

        # Convert to 0-based indexing
        j = j + m - 1
        k = k + m - 1

        # Calculate sum of neighbors
        s = 0
        for c in range(8):
            v = [j, k]
            v[0] += rotations[c][0]
            v[1] += rotations[c][1]
            if 0 <= v[0] < h and 0 <= v[1] < h:
                s += matrix[v[0]][v[1]]

        matrix[j][k] = s
        print(s, end=", " if n < (h - 2) ** 2 - 1 else "")

    print()  # Newline at the end


# Run the function
if __name__ == "__main__":
    generate_sequence(4)
    print(
        "1, 1, 2, 4, 5, 10, 11, 23, 25, 26, 54, 57, 59, 122, 133, 142, 147, 304, 330, 351, 362, 747, 806, 880, 931"
    )
