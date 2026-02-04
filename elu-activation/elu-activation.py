def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Gemini Solution
    # # Pre-binding math.exp to a local variable speeds up lookups in loops
    # exp = math.exp
    # alpha = float(alpha)
    
    # return [float(i) if i > 0 else alpha * (exp(i) - 1) for i in x]

    result = [i if i > 0 else alpha * (math.exp(i) - 1) for i in x]

    return result