fib_number= int(input("Enter a number : "))
a = 1
b = 1
fib_list = [a, b]
while a + b <= fib_number:
    a, b = b, a + b
    fib_list.append(b)
print(fib_list)
