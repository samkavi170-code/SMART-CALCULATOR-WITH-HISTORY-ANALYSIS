history = []
ops = {"add": 0, "sub": 0, "mul": 0, "div": 0}

def calc(a, b, op):
    if op == '+':
        ops["add"] += 1
        return a + b

    elif op == '-':
        ops["sub"] += 1
        return a - b

    elif op == '*':
        ops["mul"] += 1
        return a * b

    elif op == '/':
        ops["div"] += 1
        if b != 0:
            return a / b
        else:
            return "Error"

    else:
        return "Invalid"


while True:
    print("\n1. Calc  2. History  3. Analysis  4. Exit")
    ch = input("Choice: ")

    if ch == '4':
        break

    elif ch == '1':
        a = float(input("A: "))
        b = float(input("B: "))
        op = input("Op (+,-,*,/): ")

        r = calc(a, b, op)
        print("Result:", r)

        history.append(f"{a}{op}{b} = {r}")

    elif ch == '2':
        print("\n--- History ---")
        for h in history:
            print(h)

    elif ch == '3':
        print("\n--- Analysis ---")
        for k, v in ops.items():
            print(k, "used", v, "times")

    else:
        print("Invalid choice")
