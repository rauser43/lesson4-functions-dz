print("*" * 10)
def simple_separator():
    pass


def long_separator(count):
    return "*" * count
print (long_separator(3))
print (long_separator(4))


def separator(simbol, count):
    return (simbol * count)
print(separator ('-', 10))
print(separator ('#', 5))


def hello_world():
    print ("*" *10)
    print ()
    print ("Hello World!")
    print ()
    print ("#" *10)
print(hello_world())


def hello_who(who='World'):
    print("*" * 10)
    print()
    print(f"Hello {who}!")
    print()
    print("#" * 10)
print(hello_who ())


def pow_many(power, *args):
    result = 0
    for number in args:
        result += number
    return result ** power
print(pow_many (1, 1, 2))
print(pow_many (1, 2, 3))
print(pow_many (2, 1, 1))
print(pow_many (3, 2))
print(pow_many (2, 1, 2, 3, 4))

def print_key_val(**kwargs):
    for k,v in kwargs.items():
         print (f"{k}-->{v}")
print_key_val(name='Max', age=21)
print_key_val(animal='Cat', is_animal=True)


def year_birth():
    year = input('Ввведите год рождения А.С.Пушкина:')
    while year != '1799':
        print("Не верно")
    year = input('Ввведите год рождения А.С.Пушкина:')

def day_birth():
    day = input('Ввведите день рождения Пушкин?')
    while day != '6':
        print("Не верно")
    day = input('В какой день июня родился Пушкин?')


print('Верно')

#def right_date (ask, date):
    #trial = input(ask)
    #while ask != '6':
        #print("верно")
    #trial= input(ask)


#right_date("Введите год рождения?", 1799)
#right_date("Введите день рождения?", 6)
amount=0
purches_list=[]
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(f"Ваш баланс {amount}")

    choice = input('Выберите пункт меню:')
    if choice == '1':
        bill = int(input ("Введите сумму:"))
        amount += bill
    elif choice == '2':
        bill = int(input ("Введите сумму покупки:"))
        if bill>amount:
            print ("Пополните баланс")
        else:
            amount -= bill
            purchase=input ("Введите название покупки:")
            purches_list.append ([purchase,bill])
    elif choice == '3':
        print(purches_list)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')






