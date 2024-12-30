from speech_to_text import speech_to_text
from text_preprocessor import preprocess_text
from input_validator import validate_input

def main():
    # Step 1: Get input (either through speech or text)
    user_input = input("Enter your query (or speak into the mic): ")
    
    # If the user inputs text, we process it directly
    # If the user speaks, we convert speech to text
    if user_input == "":
        user_input = speech_to_text()  # Assume a mic is available for speech input
    
    # Step 2: Preprocess the input text
    preprocessed_input = preprocess_text(user_input)
    
    # Step 3: Validate the processed input
    if validate_input(preprocessed_input):
        print("Valid input:", preprocessed_input)
    else:
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()