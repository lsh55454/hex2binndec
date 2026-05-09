while True:
    try:
        line = (input())
        if not line: break
        print("BIN: ", end="")
        for i in line:
            print(f"{int(i, 16):04b}", end=" ")
        print()
        print("DEC: ", int(line, 16))
    except EOFError:
        break

