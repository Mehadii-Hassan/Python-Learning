number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[1][2]) #output- 6
print(number_grid[2][1]) #output- 8

for row in number_grid:
    print(row) #output - full matrix will be show

for row in number_grid:
    for col in row:
        print(col) #output- 1-0 (serial wise every element)
