"""
This script provides functions to convert ASCII text to different formats:
binary, decimal, and hexadecimal. It also allows the user to choose the
desired conversion type through a command-line interface.
"""

import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Function to convert ASCII to Binary
def ascii_to_binary(text):
    """
    Converts an ASCII string to its binary representation.
    Each character is represented by 8 bits.

    Args:
    text (str): The ASCII string to be converted.

    Returns:
    str: A string containing the binary representation of the ASCII text.
    """
    logger.debug("Converting ASCII text '%s' to binary", text)
    return ' '.join(format(ord(char), '08b') for char in text)

# Function to convert ASCII to Decimal
def ascii_to_decimal(text):
    """
    Converts an ASCII string to its decimal representation.
    Each character is represented by its ASCII value.

    Args:
    text (str): The ASCII string to be converted.

    Returns:
    str: A string containing the decimal representation of the ASCII text.
    """
    logger.info("Converting ASCII text '%s' to decimal", text)
    return ' '.join(str(ord(char)) for char in text)

# Function to convert ASCII to Hexadecimal
def ascii_to_hexadecimal(text):
    """
    Converts an ASCII string to its hexadecimal representation.
    Each character is represented by a 2-digit hex value.

    Args:
    text (str): The ASCII string to be converted.

    Returns:
    str: A string containing the hexadecimal representation of the ASCII text.
    """
    logger.warning("Converting ASCII text '%s' to hexadecimal", text)
    return ' '.join(format(ord(char), '02x') for char in text)

# Main function to get user input and perform conversions
if __name__ == "__main__":
    ascii_text = input("Enter the ASCII text to convert: ")
    print("Choose the conversion type:")
    print("1. Binary")
    print("2. Decimal")
    print("3. Hexadecimal")
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        # Converting ASCII to Binary
        try:
            BINARY_RESULT = ascii_to_binary(ascii_text)
            logger.info("Binary representation of '%s': %s", ascii_text, BINARY_RESULT)
            print(f"Binary representation of '{ascii_text}': {BINARY_RESULT}")
        except ValueError as error:
            logger.error("Error converting ASCII to binary: %s", error)
    elif choice == '2':
        # Converting ASCII to Decimal
        try:
            DECIMAL_RESULT = ascii_to_decimal(ascii_text)
            logger.info("Decimal representation of '%s': %s", ascii_text, DECIMAL_RESULT)
            print(f"Decimal representation of '{ascii_text}': {DECIMAL_RESULT}")
        except ValueError as error:
            logger.error("Error converting ASCII to decimal: %s", error)
    elif choice == '3':
        # Converting ASCII to Hexadecimal
        try:
            HEXADECIMAL_RESULT = ascii_to_hexadecimal(ascii_text)
            logger.info("Hexadecimal representation of '%s': %s", ascii_text, HEXADECIMAL_RESULT)
            print(f"Hexadecimal representation of '{ascii_text}': {HEXADECIMAL_RESULT}")
        except ValueError as error:
            logger.error("Error converting ASCII to hexadecimal: %s", error)
    else:
        logger.error("Invalid choice. Please enter 1, 2, or 3.")
        print("Invalid choice. Please enter 1, 2, or 3.")
