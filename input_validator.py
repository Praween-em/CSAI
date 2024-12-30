def validate_input(user_input):
    """
    Validates the processed user input to ensure it's usable.
    
    Args:
        user_input (str): The processed user input.
    
    Returns:
        bool: True if the input is valid, False otherwise.
    """
    with open("archive\en","r", encoding='utf-8' ) as file:
        content = file.read().splitlines()
    

    
    # Basic validation: check if the input is empty
    if not user_input:
        print("Error: Input cannot be empty.")
        return False
    
    # Check if certain keywords or patterns exist in the input
    # (You can expand this with more validation rules as needed)
    for invalid_word in content :
        if invalid_word.lower() in user_input.lower(): 
            print("Error: Input should contain a valid query.")
            return False

    return True

