def preprocess_text(user_input):
    """
    Preprocesses the raw user input to normalize and clean it.
    
    Args:
        user_input (str): The raw input from the user.
    
    Returns:
        str: The cleaned and normalized input.
    """
    # Remove leading/trailing whitespace
    cleaned_input = user_input.strip()
    
    # Convert to lowercase for uniformity
    normalized_input = cleaned_input.lower()
    
    # Remove any special characters (only alphanumeric characters and spaces)
    processed_input = ''.join(
        char for char in normalized_input if char.isalnum() or char.isspace()
    )
    
    return processed_input
