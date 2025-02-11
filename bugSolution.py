def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    for number in numbers:
        if not isinstance(number,(int,float)):
            raise ValueError("List must contain only numbers")
    return sum(numbers) / len(numbers)

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}") #This will print 0 as intended

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}") #This will print 3.0 as intended

my_list = [1,2, 'a']
try:
    average = calculate_average(my_list) #This will now raise a ValueError
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}")