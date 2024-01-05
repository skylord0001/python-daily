def get_recent_most(my_list):
    recent_most = []
    first_data_type = None

    for item in reversed(my_list):
        current_data_type = type(item)

        if first_data_type is None:
            # If it's the first element, set the data type
            first_data_type = current_data_type
            recent_most.append(item)
        elif current_data_type == first_data_type:
            # If the data type matches the first one, add to the list
            recent_most.append(item)
        else:
            # If it's a different data type, break the loop
            break

    return recent_most

my_list = ['1', 'aff', 'str', {'key': '3'}, '1', 'aff', 'str', {'key': '2'}]

# Call the function to get the recent most elements
recent_most = get_recent_most(my_list)

# Print the recent most elements
for item in reversed(recent_most):
    print(item)
