def romanToInt(s: str) -> int:
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    } 

    prev_value = 0
    total = 0
    for i in reversed(s):
        value = roman_map[i]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

print(romanToInt("III"))    # Output: 3
print(romanToInt("IV"))     # Output: 4
print(romanToInt("IX"))     # Output: 9
print(romanToInt("LVIII"))  # Output: 58
print(romanToInt("MCMXCIV")) # Output: 1994

misc_arry = [1, "Hello", 3.4]
print(misc_arry)