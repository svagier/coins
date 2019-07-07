saved = {}

def max_return(value):
    if value in saved:
        return saved[value]
    else:
        total = 0
        (a, b, c) = (value // 2, value // 3, value // 4)
        if a + b + c > value:
            total += max_return(a)
            total += max_return(b)
            total += max_return(c)
        else:
            total += value
        saved[value] = total
        return total


def main():

    while True:
        try:
            coin = int(input())
            print(max_return(coin))
        except:
            break


if __name__ == "__main__":
    main()