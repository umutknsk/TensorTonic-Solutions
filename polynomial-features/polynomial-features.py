def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # result = []

    # for i in values:
    #     new_row = []
    #     for j in range(degree + 1):
    #         new_value = i ** j
    #         new_row.append(new_value)

    #     result.append(new_row)

    # return result

    return [[value ** i for i in range(degree + 1)] for value in values]