# absolute values of a list of numbers
numbers = [-1, 2, 0, -4, -10, 5]
abs_numbers = []

# "Normal way"
for number in numbers:
    abs_numbers.append(abs(number))
print("Absolute numbers (normal for loop): %s" % abs_numbers)

# Listcomp
abs_numbers = [abs(number) for number in numbers]
print("Absolute numbers (listcomp): %s" % abs_numbers)

non_zero_numbers = [abs(number) for number in numbers if number != 0]
print("Non-zero numbers: %s" % non_zero_numbers)

# OUTPUT:
#  ➜  ListCompPython git:(master) ✗ python list_comp.py
#  Absolute numbers (normal for loop): [1, 2, 0, 4, 10, 5]
#  Absolute numbers (listcomp): [1, 2, 0, 4, 10, 5]
#  Non-zero numbers: [1, 2, 4, 10, 5]
