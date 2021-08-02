def create_possible_number(input_list):
    if len(input_list) == 0:
        return input_list
    elif len(input_list) == 1:
        return input_list
    else:
        result = []

        # Find all sample space of number that could create from number in list
        for i in range(len(input_list)):
            # Define first element in list
            a = input_list[i]
            # Create another list to collect remaining element in the first list
            in_list = input_list[:i] + input_list[i+1:]

            # Generate all possible value that start with element 'a'
            for j in create_possible_number(in_list):
                result.append(a + j)

        return result


input_number = input("Enter positive integer to list (separate by space) : ").split()
print('Input list : ', input_number)

sample_space = []
for p in create_possible_number(input_number):
    print(p)

