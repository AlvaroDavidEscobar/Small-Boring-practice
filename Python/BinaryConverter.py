while True:
    BinaryRaw = []
    BinaryProcessed = ""
    Number = int(input())
    Repeats = 0
    while Number >= 1:
        if Number % 2 == 0: BinaryRaw.append(0)
        else: BinaryRaw.append(1)
        Repeats += 1
        Number = int(Number / 2)
        print(f"{" " * Repeats}{Number}")
    for i in reversed(BinaryRaw):
        BinaryProcessed += f"{i}"
    print(" " + BinaryProcessed)
    print("============================")
