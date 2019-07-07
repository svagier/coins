def divide(value):
    a = value // 2
    b = value // 3
    c = value // 4
    return a, b, c

def max_return(value):
    total = 0
    (a, b, c) = divide(value)
    if a + b + c > value:
        total += max_return(a)
        total += max_return(b)
        total += max_return(c)
    else:
        total += value
    return total


def main():
    for testcase in range(10):
        coin = int(input())
        print(max_return(coin))


if __name__ == "__main__":
    main()