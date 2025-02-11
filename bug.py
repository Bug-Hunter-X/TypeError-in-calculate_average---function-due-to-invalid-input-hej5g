def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}") #This will print 0 as intended

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}") #This will print 3.0 as intended

my_list = [1,2, 'a']
average = calculate_average(my_list) #This will throw an error because of unsupported operand type(s) for +: 'int' and 'str'
print(f"The average is: {average}")