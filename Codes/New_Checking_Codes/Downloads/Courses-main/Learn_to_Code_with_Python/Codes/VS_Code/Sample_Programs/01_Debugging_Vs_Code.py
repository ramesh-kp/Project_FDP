print()
print("Welcome to my program")
def do_fun_stuff():
    a = 20
    print("Hello")
    print("Good Bye")
    a = 25
    return a

final_value = do_fun_stuff()
print(do_fun_stuff())
print()

values = [1, 2, 3, 4, 5]
def multiply(numbers):
    total = 0
    for index, number in enumerate(numbers):
        total += number * (index - 1)
    return total
print(multiply(values))
print()
