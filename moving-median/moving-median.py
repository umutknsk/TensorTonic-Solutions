def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    num_of_iterations = len(values) - window_size + 1
    result = []
    
    for i in range(num_of_iterations):
        sliced_list = sorted(values[i:i + window_size])
        n = len(sliced_list)
        
        if window_size % 2 != 0:
            median = sliced_list[n // 2]
        else:
            median = (sliced_list[n // 2  - 1] + sliced_list[n // 2]) / 2
            
        result.append(median)

    return result