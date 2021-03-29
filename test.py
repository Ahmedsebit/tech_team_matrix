def print_student(x):
    if type(x) != int:
        return x + 1
    else:
        return 'Please enter a number'
    

value = print_student(10)
print(value)