def task(n, m):
    if m > n:
        print("Після вирубки не може залишитись більше дерев ніж до неї")
        raise Exception('Invalid input!')
    elif m == 0:
        variants = 1
    elif m == 1:
        variants = n
    elif m == n:
        variants = 0
    else:
        distance, variants = 0, 0
        while True:
            usedPositions = m + distance * (m - 1)
            if usedPositions > n:
                break
            variants += n - usedPositions + 1
            distance += 1
    return variants


def int_validation(a):
    while True:
        try:
            a = int(a)
        except:
            print("Введіть ціле додатнє число")
            a = input()
            continue
        if a < 0:
            print("Введіть ціле додатнє число")
            a = input()
            continue
        break
    return a


def main():
    print("Скільки дерев посаджено?")
    n = int_validation(input())
    print("Скільки дерев має залишитись після вирубки?")
    m = int_validation(input())

    result = task(n, m)
    print("Існує ", result, " способів вирубки дерев")


if __name__ == "__main__":
    main()
