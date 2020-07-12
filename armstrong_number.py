number =input("Enter a number :").strip()
number_list = list(number)
index = 0
total = 0
if number.isdigit() != True:
   print("It is an invalid entry. Don`t use non-numeric, float or negative values!")
else:
   while index < len(number):
       total += int(number_list[index]) ** len(number)
       index += 1
   if int(number) == total:
       print("{} is an Armstrong number".format(number))
   else:
       print("{} is not an Armstrong number".format(number))
