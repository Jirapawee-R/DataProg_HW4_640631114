def create_possible_number(input_list):
    if len(input_list) == 0:
        return input_list
    elif len(input_list) == 1:
        return input_list
    else:
        result = []

        # Find all sample space of number that could create from number in list
        # Example x = {1,2,3}
        # all possible number that could be created is {123, 132, 213, 231, 312, 321}
        for i in range(len(input_list)):
            # Define first element in list
            # Example: define a = [1] from x = {1,2,3}
            a = input_list[i]

            # Create another list to collect other remaining element which is not the element in 'a'
            # Example: in_list = [2,3] | input_list[:i] = [] | input_list[i+1:] = [2,3]
            in_list = input_list[:i] + input_list[i+1:]

            # Generate all possible value that start with element 'a'
            # Example loop 1: j.a = 2 , j.in_list = 3 >> a+j = 23 >> result = [123]
            # Example loop 2: j.a = 3 , j.in_list = 2 >> result = 32 >> result = [132]
            for j in create_possible_number(in_list):
                result.append(a + j)

        return result


input_number = input("\nEnter positive integer to list (separate by space) : ").split()

sample_space = []

# Collect all possible number that could be create from input list
for p in create_possible_number(input_number):
    sample_space.append(p)
print('Sample space : ', sample_space)

