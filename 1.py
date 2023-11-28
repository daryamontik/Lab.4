class List:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Элемент отсутствует в списке")

    def search(self, item):
        if item in self.items:
            return f"Элемент {item} найден в списке"
        else:
            return f"Элемент {item} не найден в списке"

    def size(self):
        return len(self.items)

    def display(self):
        if self.size() == 0:
            print("Список пуст")
        else:
            print("Элементы списка:")
            for item in self.items:
                print(item)

my_list = List()

while True:

    print("1. Добавить элемент")
    print("2. Удалить элемент")
    print("3. Поиск элемента")
    print("4. Узнать размер списка")
    print("5. Вывести список на экран")
    print("0. Выход")

    choice = input("Ваш выбор: ")
    if choice =="1":
        item = input("Введите элемент, который хотите добавить: ")
        my_list.add(item)
    elif choice == "2":
        item = input("Введите элемент, который хотите удалить: ")
        my_list.remove(item)
    elif choice == "3":
        item = input("Введите элемент, который хотите найти: ")
        result = my_list.search(item)
        print(result)
    elif choice == "4":
        size = my_list.size()
        print(f"Размер списка равен: {size}")
    elif choice == "5":
        my_list.display()
    elif choice == "0":
        print("Программа завершена")
        break
    else:
        print("Некорректный выбор. Попробуйте ещё раз.")