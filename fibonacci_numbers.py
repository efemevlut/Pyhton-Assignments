#Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.

fibonacci = []

for i in range(-2, 8) :
    if i < 0 :
        fibonacci.append(1)
    else : 
        fibonacci.append(fibonacci[i] + fibonacci[i+1])
        
print(fibonacci)
