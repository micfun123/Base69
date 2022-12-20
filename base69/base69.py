import string

__all__ = ["encode_base69", "decode_base69", "InvalidInput"]

values = (
    list(string.digits)
    + list(string.ascii_uppercase)
    + list(string.ascii_lowercase)
    + ["+", "/", "=", "@", "*", "-", "!", "#"]
)
CONVERSION_TABLE = dict(zip(range(len(values)), values))


class InvalidInput(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


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

    if not type(input) == int:
        raise InvalidInput(
            "Input must be an integer as we only support integers for now"
        )

    base69 = ""
    while input > 0:
        remainder = input % 70
        base69 = CONVERSION_TABLE[remainder] + base69
        input = input // 70
    base69 = "69*|" + base69
    return base69


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

    if not input.startswith("69*|"):
        raise InvalidInput("Invalid Base69 input! Base69 must begin '69*|'")

    input = input[4:]

    base = 0
    for i in range(len(input)):
        base += list(CONVERSION_TABLE.keys())[
            list(CONVERSION_TABLE.values()).index(input[i])
        ] * (70 ** (len(input) - i - 1))
    return base
