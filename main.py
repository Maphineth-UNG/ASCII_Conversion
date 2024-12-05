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

# Function to convert ASCII to Binary
def ascii_to_binary(text):
    logger.debug("Converting ASCII text '%s' to binary", text)
    return ' '.join(format(ord(char), '08b') for char in text)

# Function to convert ASCII to Decimal
def ascii_to_decimal(text):
    logger.debug("Converting ASCII text '%s' to decimal", text)
    return ' '.join(str(ord(char)) for char in text)

# Function to convert ASCII to Hexadecimal
def ascii_to_hexadecimal(text):
    logger.debug("Converting ASCII text '%s' to hexadecimal", text)
    return ' '.join(format(ord(char), '02x') for char in text)

# Command-line interface using Click
@click.command()
@click.option('--text', prompt='Enter the ASCII text to convert', help='The ASCII text to be converted.')
def convert_ascii(text):
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
    # import doctest
    # doctest.testmod()
    convert_ascii()
