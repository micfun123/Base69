import string

__all__ = ["encode_base69", "decode_base69", "InvalidInput"]

# Base-69 character set (69 unique characters)
values = (
    list(string.digits)
    + list(string.ascii_uppercase)
    + list(string.ascii_lowercase)
    + ["+", "/", "=", "@", "*", "-", "!", "]"]
)
CONVERSION_TABLE = dict(zip(range(len(values)), values))

class InvalidInput(Exception):
    def __init__(self, message: str) -> None:
        message = f"Invalid input was provided! ({message})"
        super().__init__(message)

def encode_base69(input: int) -> str:
    """
    Encode an integer to Base69

    Parameters:
        input (`int`): The number to convert

    Returns:
        `str`: The encoded Base69 result

    Raises:
        `InvalidInput`: If the input is invalid
    """
    if not isinstance(input, int):
        raise InvalidInput("Must be of type: int")

    if input < 0:
        raise InvalidInput("Input must be non-negative")

    if input == 0:
        return "69*|" + CONVERSION_TABLE[0]

    base69 = ""
    while input > 0:
        remainder = input % 69
        base69 = CONVERSION_TABLE[remainder] + base69
        input = input // 69

    return "69*|" + base69

def decode_base69(input: str) -> int:
    """
    Decode Base69 text to an integer

    Parameters:
        input (`str`): the Base69 to decode

    Returns:
        `int`: The decoded integer result

    Raises:
        `InvalidInput`: If the input is invalid
    """
    if not isinstance(input, str):
        raise InvalidInput("Must be of type: str")

    if not input.startswith("69*|"):
        raise InvalidInput("Invalid Base69 input! Base69 must begin with '69*|'")

    input = input[4:]
    base = 0

    for i, char in enumerate(reversed(input)):
        try:
            value = list(CONVERSION_TABLE.keys())[list(CONVERSION_TABLE.values()).index(char)]
            base += value * (69 ** i)
        except ValueError:
            raise InvalidInput(f"'{char}' is not a valid Base69 character")

    return base
