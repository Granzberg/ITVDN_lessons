def calculator():
    while True:
        try:
            x = float(input("x = "))
            choice = input("Выбирите действие(+, -, *, /, **): ")
            y = float(input("y = "))
            result = 0

            if choice == "+":
                result = x + y
            elif choice == "-":
                result = x - y
            elif choice == "*":
                result = x * y
            elif choice == "/":
                result = x / y
            elif choice == "**":
                result = x ** y
        except (ZeroDivisionError, ValueError) as e:
            print("Ошибка: ", e)
            print("Повторите ввод")
            print("*" * 30)
        else:
            print("Ответ: ", result)
            break


calculator()
