print('51 простое число')
def t1():
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_51st_prime():
        count = 0
        number = 2
        while True:
            if is_prime(number):
                count += 1
                if count == 51:
                    return number
            number += 1
    fifty_first_prime = find_51st_prime()
    print("51ое простое число:",fifty_first_prime)

def t2():
    def reverse_string(text):
        reversed_string = text[::-1]
        return reversed_string
    text = str(input("Введите текст:"))
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

        most_common_char = max(char_count, key=char_count.get)

    print("Наиболее повторяющийся символ в строке: ",most_common_char)
    print("Реверсия строки:",reverse_string(text))
def t3():
    my_list = [13, 56, 'Python', 34, 19, 'love']
    for i in range(len(my_list)):
        if isinstance(my_list[i], int):
            if my_list[i] % 2 == 0:
                digits = [int(digit) for digit in str(my_list[i])]
                product = 1
                for digit in digits:
                    product *= digit
                my_list[i] = product
            else:
                my_list[i] = 1

    print("Измененный список:", my_list)


def t4():
    my_dict = {'a': 50, 'b': 5, 'c': 56, 'd': 4, 'e': 58, 'f': 20}
    sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])
    print("Три ключа с самыми маленькими значениями:")
    for key, value in sorted_dict[:3]:
        print(f"{key}: {value}")

#Магазин игрушек
def t5():
    toy_store = {
        'Машинка': ['Бип-бип', 100, 10],
        'Кукла': ['Поиграй со мной', 200, 5],
        'Мишка': ['Где мой мёд?', 150, 8],
        'Лего': ['Собери меня', 800, 12],
        'Мяч': ['Поиграем в футбол', 250, 3],
        'Коньки': ['Спортивный инвентарь', 12000, 7]
    }

    while True:
        print("\nМеню:")
        print("1.Просмотр описания")
        print("2.Просмотр цены")
        print("3.Просмотр количества")
        print("4.Вся информация")
        print("5.Покупка")
        print("6.Выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            toy_name = input("Введите название игрушки: ")
            if toy_name in toy_store:
                print(f"Описание игрушки '{toy_name}': {toy_store[toy_name][0]}")
            else:
                print("Игрушка не найдена.")

        elif choice == '2':
            toy_name = input("Введите название игрушки: ")
            if toy_name in toy_store:
                print(f"Цена игрушки '{toy_name}': {toy_store[toy_name][1]}")
            else:
                print("Игрушка не найдена.")

        elif choice == '3':
            toy_name = input("Введите название игрушки: ")
            if toy_name in toy_store:
                print(f"Количество игрушек '{toy_name}': {toy_store[toy_name][2]}")
            else:
                print("Игрушка не найдена.")

        elif choice == '4':
            print("Информация о наличии игрушек в магазине:")
            for toy_name, toy_info in toy_store.items():
                print(f"{toy_name}: {toy_info[0]}, Цена: {toy_info[1]}, Количество: {toy_info[2]}")

        elif choice == '5':
            total_cost = 0
            print("Покупка игрушек:")
            while True:
                toy_name = input("Введите название игрушки для покупки (или 'n' для выхода): ")
                if toy_name == 'n':
                    break
                if toy_name in toy_store:
                    quantity = int(input("Введите количество: "))
                    if quantity <= toy_store[toy_name][2]:
                        cost = toy_store[toy_name][1] * quantity
                        toy_store[toy_name][2] -= quantity
                        total_cost += cost
                        print(f"Покупка успешно совершена. Сумма к оплате: {total_cost}")
                    else:
                        print("Извините, товара в таком количестве нет в наличии.")
                else:
                    print("Игрушка не найдена.")

        elif choice == '6':
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню от 1 до 6.")
def t6():
    my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    even_sum = 0

    for num in my_tuple:
        if num % 2 == 0:
            even_sum += num

    print("Сумма четных элементов:", even_sum)

ch = input("Введите номер задания(0 - чтобы выйти): ")
while True:
    if ch == '0':
        break
    elif ch == '1':
        t1()
    elif ch == '2':
        t2()
    elif ch == '3':
        t3()
    elif ch == '4':
        t4()
    elif ch == '5':
        t5()
    elif ch == '6':
        t6()
    else:
        print("Неверный выбор")
    ch = input("Введите номер задания:")