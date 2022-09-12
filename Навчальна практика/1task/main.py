
print("Скільки дерев посаджено?")
n = int(input())
print("Скільки дерев має залишитись після вирубки?")
m = int(input())

if m > n:
    print("Після вирубки не може залишитись більше дерев ніж до неї")
    raise Exception('Invalid input!')

if m == 0:
    variants = 1
elif m == 1:
    variants = n
elif m == n:
    variants = 0
else:
    distance, variants = 0, 0
    while (True):
        usedPositions = m + distance * (m - 1)
        if usedPositions > n:
            break
        variants += n - usedPositions + 1
        distance += 1

print("Існує ", variants, " способів вирубки дерев")
