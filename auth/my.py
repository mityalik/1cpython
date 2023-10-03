import time

def admin_console(name):
    f1 = open('products.txt', 'r+')
    try:
        print(f"Добро пожаловать, {name}, вы вошли как администратор - вам доступна возможность редактирования списка товаров.\nПожалуйста, будьте внимательны при вводе данных!")
        time.sleep(1)
        flag = True
        print("Правила ввода товаров следующие:\n1 - Вводите товары по истечению таймера, чтобы избежать путаницу\n2 - Не вводите два одинаковых названия товара!\n3 - Как хотите закончить учёт - введите '0'")
        while flag == True:
            ans = input("Введите название товара: ")
            if ans == "0":
                flag = False
                break
            else:
               flag_l = True
               for x in f1.readlines():
                    if x.split()[0] == ans:
                        print("Данный товар уже есть в базе данных!")
                        flag_l = False
                        flag = False
                        break
                    if flag_l == True:
                        f1.write(f"{ans}\n")


            

    finally:
        f1.close()

def sklad_console(name):
    f1 = open('sklad.txt', 'r+')
    f2 = open('products.txt', 'r+')
    try:
        print(f"Добро пожаловать, {name}, вы вошли как заведующий склада - вам доступна возможность добавления товаров на склад.\nПожалуйста, будьте внимательны при вводе данных!")
        time.sleep(1)
        flag = True
        print("Правила ввода товаров следующие:\n1 - Вводите товары по истечению таймера, чтобы избежать путаницу\n2 - Не вводите два одинаковых названия товара!\n3 - Как хотите закончить учёт - введите '0'\n4 - Вводите название товара и цену, которая есть в списке.")
        while flag == True:
            for x in f2.readlines():
                    print(x.strip())
            ans = input("Введите название товара: ")
            ans2 = input("Введите цену товара: ")
            if ans == "0":
                flag = False
                break
            else:
                next_gen = True

                if next_gen == True:
                    lines = f1.readlines()
                    for x in lines:
                        if x.split(",")[0] == ans:
                            flag = False
                        
                    if flag == True:
                        print("Товар добавлен!")
                        f1.write(f"{ans},{ans2}\n")
                else:
                    print("Товара нет в базе, сообщите админу")

            
    finally:
        f1.close()
        f2.close()

def main_console(name):
    f2 = open('customer.txt', 'r+')
    f1 = open('sklad.txt', 'r+')
    try:
        print(f"Добро пожаловать, {name}, вы вошли как продавец/маркетолог - вам доступна возможность учета продажи товаров.\nПожалуйста, будьте внимательны при вводе данных!")
        time.sleep(1)
        flag = True
        print("Правила ввода товаров следующие:\n1 - Вводите товары по истечению таймера, чтобы избежать путаницу\n2 - Не вводите два одинаковых названия товара!\n3 - Как хотите закончить учёт - введите '0'\n4 - Как только товар будет продан, вы можете ввести кол-во проданного товара")
        ans = input("Введите название товара: ")
        ans2 = input("Введите цену товара: ")
        count = 1
        for x in f1.readlines():
            print(x.strip())
            if x.split(",")[0] == ans:
                print("Товар есть в базе данных, считаем!")
                count = count * (int(ans2) * int(x.split(",")[1]))
                f2.write(f"{ans},{count}\n")
                break
        else:
            print("Товара нет!")
            

    finally:
        f1.close()
f = open('base.txt','r+')
try:
    ans = int(input("Выберите действите:\n1- Регистрация\n2- Вход\n"))
    if ans == 1:
        flag = False
        log = input("Введите логин: ")
        for x in f.readlines():
            if x.split(",")[0] == log:
                flag = True
        if flag == False:
            print("Логин свободен")
            pas = input("Введите пароль: ")
            age =int(input("Введите возраст: "))
            name = input("Введите ФИ: ")
            group = int(input("Введите группу:\n1 - Администратор,\n2 - Заведующий складом,\n3 - Продавец\n->"))
            if (group > 3 or group < 1):
                print("Неверный ввод!")
            else:
                f.write(f"\n{log},{age},{name},{pas},{group}")
                time.sleep(1)
                print("Регстрация успешно завершена, можете запустить код ещё раз и войти в аккаунт!")
        else:
            print("Логин занят")
    elif ans == 2:
        flag = False
        log = input("Введите логин: ")
        for x in f.readlines():
            if x.split(",")[0] == log:
                flag = True
                print("Логин найден, введите пароль: ")
                pas = input()
                if (x.split(",")[3] == pas):
                    print(f"Вход выполнен, добро пожаловать, {log}")
                    if (x.split(",")[4] == "1"):
                        admin_console(x.split(",")[0])
                    elif (x.split(",")[4] == "2"):
                        sklad_console(x.split(",")[0])
                    elif (x.split(",")[4] == "3"):
                        main_console(x.split(",")[0])
                    break
                else:
                    print(f"Прошу прощения, {log}, пароль введен неверно.")
                    break
        if flag == False:
            print("Логин не найден в Базе Данных!")
        time.sleep(1)
    else:
        print("Неверный ввод! Повторите попытку позже")
        time.sleep(1)
        f.close()




finally:
    f.close()
