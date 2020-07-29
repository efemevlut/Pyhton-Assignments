sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

count = 0
count_2 = 0
print("- " * 15)

for i in sudoku:
    if sudoku[count_2] == i :
        for ii in i:
            count += 1
            print(ii, end="  ")
            if count == 3 :
                print("|", end=" ")
            elif count == 6:
                print("|", end=" ")
        count = 0
            
    print("")
    count_2 += 1
    if count_2 == 3:
        print("- " * 15)
    elif count_2 == 6:
        print("- " * 15)
    elif count_2 == 9:
        print("- " * 15)  
