def selu(x):
    """
    Apply SELU activation to each element.
    """
    lmbd, alpha = 1.0507009873554804934193349852946, 1.6732632423543772848170429916717
    result = [lmbd * i if i > 0 else lmbd * alpha * (math.exp(i) - 1) for i in x]

    return result