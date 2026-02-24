def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    total_values = len(values)
    
    count_dict = {}
    for val in values:
        count_dict[val] = count_dict.get(val, 0) + 1
    
    return [count_dict[val] / total_values for val in values]