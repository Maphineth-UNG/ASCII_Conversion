"""
ASCII Conversion Tool

This script provides functions to convert ASCII text to different formats:
binary, decimal, and hexadecimal. It also allows the user to choose the
desired conversion type through a command-line interface.

Key Features:
- ASCII to binary conversion.
- ASCII to decimal conversion.
- ASCII to hexadecimal conversion.
- User-friendly CLI using Click.
"""

import logging
import click
from rich.console import Console
from rich.table import Table

# Set up logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set up Rich console
console = Console()

def ascii_to_binary(text: str) -> str:
    """
    Convert ASCII text to its binary representation.

    Args:
        text (str): The ASCII text to be converted.

    Returns:
        str: A space-separated string representing the binary equivalent of each character in the input text.

    Example:
        >>> ascii_to_binary("AB")
        '01000001 01000010'
    """
    logger.debug("Converting ASCII text '%s' to binary", text)
    return ' '.join(format(ord(char), '08b') for char in text)

def ascii_to_decimal(text: str) -> str:
    """
    Convert ASCII text to its decimal representation.

    Args:
        text (str): The ASCII text to be converted.

    Returns:
        str: A space-separated string representing the decimal equivalent of each character in the input text.

    Example:
        >>> ascii_to_decimal("AB")
        '65 66'
    """
    logger.debug("Converting ASCII text '%s' to decimal", text)
    return ' '.join(str(ord(char)) for char in text)

def ascii_to_hexadecimal(text: str) -> str:
    """
    Convert ASCII text to its hexadecimal representation.

    Args:
        text (str): The ASCII text to be converted.

    Returns:
        str: A space-separated string representing the hexadecimal equivalent of each character in the input text.

    Example:
        >>> ascii_to_hexadecimal("AB")
        '41 42'
    """
    logger.debug("Converting ASCII text '%s' to hexadecimal", text)
    return ' '.join(format(ord(char), '02x') for char in text)

@click.command()
@click.option('--text', prompt='Enter the ASCII text to convert', help='The ASCII text to be converted.')
def convert_ascii(text: str) -> None:
    """
    Command-line interface for ASCII conversion.

    Prompts the user to select a conversion type (binary, decimal, or hexadecimal)
    and displays the converted result.

    Args:
        text (str): The ASCII text to be converted.

    Example Usage:
        $ python main.py --text "Hello"
        Choose the conversion type:
        1. Binary
        2. Decimal
        3. Hexadecimal
        Enter your choice (1/2/3): 1
        Binary representation of 'Hello': 01001000 01100101 01101100 01101100 01101111
    """
    console.print("Choose the conversion type:")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Option", style="dim")
    table.add_column("Conversion Type")
    table.add_row("1", "Binary")
    table.add_row("2", "Decimal")
    table.add_row("3", "Hexadecimal")
    console.print(table)

    choice = console.input("[bold cyan]Enter your choice (1/2/3): [/bold cyan]")

    if choice == '1':
        # Converting ASCII to Binary
        try:
            binary_result = ascii_to_binary(text)
            logger.info("Binary representation of '%s': %s", text, binary_result)
            console.print(f"[green]Binary representation of '{text}': {binary_result}[/green]")
        except ValueError as error:
            logger.error("Error converting ASCII to binary: %s", error)
    elif choice == '2':
        # Converting ASCII to Decimal
        try:
            decimal_result = ascii_to_decimal(text)
            logger.info("Decimal representation of '%s': %s", text, decimal_result)
            console.print(f"[green]Decimal representation of '{text}': {decimal_result}[/green]")
        except ValueError as error:
            logger.error("Error converting ASCII to decimal: %s", error)
    elif choice == '3':
        # Converting ASCII to Hexadecimal
        try:
            hexadecimal_result = ascii_to_hexadecimal(text)
            logger.info("Hexadecimal representation of '%s': %s", text, hexadecimal_result)
            console.print(f"[green]Hexadecimal representation of '{text}': {hexadecimal_result}[/green]")
        except ValueError as error:
            logger.error("Error converting ASCII to hexadecimal: %s", error)
    else:
        logger.error("Invalid choice. Please enter 1, 2, or 3.")
        console.print("[red]Invalid choice. Please enter 1, 2, or 3.[/red]")

if __name__ == "__main__":
    convert_ascii()
