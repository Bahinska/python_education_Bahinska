# Варіант 1 Створити клас Booking, який містить такі поля
#  1. Name (Тільки літери)
#  2. PricePerDay (Число з 2 знаками після коми)
#  3. StartDate (Клас Date, що містить 3 поля: день (1-31 / 1-30 / 1-29 / 1-28), місяць (1-12) рік (2019+). Min: 23.10.2019
#  4. EndDate (Клас Date, що містить 3 поля: день (1-31 / 1-30 / 1-29 / 1-28), місяць (1-12) рік (2019+). Min: StartDate
# Створити такі методи:
#  1. Зчитати масив (клас для роботи з масивом екземплярів класу Booking) Booking з файла (1)
#  2. Додати новий Booking. Booking з датами 27.10.2019 - 5.11.2019 додати неможливо, якщо існує вже Booking в цьому діапазоні, наприклад 29.10.2019-31.10.2019 / 31.10.2019 - 2.11.2019 (3)
#  3. Додати валідацію на поля Name, Price, StartDate, EndDate (2.5)
#  4. Обрахувати загальну ціну за Booking: PricePerDay * DaysCount (1.5)
#  5. Кожен 2 доданий Booking ціна за день автоматично піднімається на 10.00. (1.5)
 # 6. Вивести всі Bookings на екран (0.5)
from Collection import *
import os.path

def menu():
    collection = Collection()
    while True:
        help_message = get_help_message()
        task = input(help_message)
        if task == '1':
            file = read_json(collection)
        if task == 'exit':
            quit()

def get_help_message():
    help_message = "*" * 51
    help_message += "\n  Possible commands:" + \
                    "\n  1  - to read from file. " + \
                    "\n  exit - to exit.  \n"
    help_message += "*" * 51 + "\n"
    return help_message


@Validation.validate_inp
def read_json(collection):
    file = input("File name: ")
    if os.path.exists(file):
        collection.read_json_file(file)
        return file
    else:
        raise ValueError("File does not exist!")

if __name__ == '__main__':
    menu()
