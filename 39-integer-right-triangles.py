import math


def main():
    x = integer_right_triangles(1000)
    print(x)


def integer_right_triangles(n):
    max_p = 0
    max_solution_count = 0
    for i in range(1, n + 1, 1):
        solution_count = find_sides(i)
        if solution_count > max_solution_count:
            max_solution_count = solution_count
            max_p = i
    return max_p


def find_sides(p):
    solutions = 0
    a_limit = int(p / 3) + 1
    # Assumption: value of a will not be greater than 1/3 of p.
    for a in range(1, a_limit + 1, 1):
        counter = 0
        ub = p
        lb = a
        forward = True
        # Binary search for value of b.
        while forward:
            b = lb + int((ub - lb) / 2)
            c = math.sqrt(a**2 + b**2)
            if a + b + c == p:
                solutions += 1
                forward = False
            if lb == b or ub == b:
                forward = False
            if a + b + c > p:
                ub = b
            else:
                lb = b
    return solutions


if __name__ == "__main__":
    main()
