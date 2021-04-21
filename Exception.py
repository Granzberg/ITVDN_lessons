def calk():
    try:
        x = float(input("x = "))
        y = float(input("y = "))
        z = x / y
        print(z)
    except (ZeroDivisionError, ValueError) as error:
        print("Error: ", error)


if __name__ == "__main__":
    calk()
