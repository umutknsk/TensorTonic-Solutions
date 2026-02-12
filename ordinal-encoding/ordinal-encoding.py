def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    mapping = {order: i for i, order in enumerate(ordering)}

    return [mapping[value] for value in values]