

my_array = [11,23,56,98,2,5,100,36,57]              #creates an array
min_Value = my_array[0]                             # assigning the first value of the array to min_value

for i in my_array:                                  # initiating for loop
    if i < min_Value:                               # checking if the current value is less than min_value through if statement
        min_Value = i                               # if the current value is less than min_value, then min_value is updated with the current value

print('Lowest value: ',min_Value )                  # printing the lowest value in the array
    


