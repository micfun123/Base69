import base69

tests = {
    74: "69*|14",
    890: "69*|Co",
    927: "69*|DH",
    629: "69*|8#",
    825: "69*|Bt",
    226: "69*|3G",
    252: "69*|3g",
    503: "69*|7D",
    883: "69*|Ch",
    636: "69*|96",
    374: "69*|5O",
    258: "69*|3m",
    102: "69*|1W",
    951: "69*|Df",
    66: "69*|*",
}

# this file more useful when used with pytest
for number, _base69 in tests.items():
    assert base69.encode_base69(number) == _base69
    assert base69.decode_base69(_base69) == number

print("All tests were successful!")
