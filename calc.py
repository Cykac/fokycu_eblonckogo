again = True
while again:
    num_1 = int(input("Введіть,будь ласка, перше число: "))
    num_2 = int(input("Введіть,будь ласка, друге число: "))
    oper = input("Введіть тип операції: ")

    if oper == '+':
        print("Результат: " + str(num_1 + num_2))
    elif oper == '-':
        print("Результат: " + str(num_1 - num_2))
    elif oper == '*':
        print("Результат:"  + str(num_1 * num_2))
    elif oper == '/':
        if num_2 != 0:
            print("Результат: " + str(num_1 / num_2))
    else:
        print("Ти щось не те надрукува,прощавай")
    again = input("Бажаєте продовжити?(y/n)\n")
    if again == 'n':
        again = False
    

