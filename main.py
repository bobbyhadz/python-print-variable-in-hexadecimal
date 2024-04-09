# Print a variable in Hexadecimal in Python

my_str = 'bobbyhadz.com'


result = ' '.join(hex(ord(char)) for char in my_str)
print(result)  # 👉️ 0x62 0x6f 0x62 0x62 0x79 0x68 0x61 0x64 0x7a 0x2e 0x63 0x6f 0x6d

# ------------------------------------------

result = ' '.join(f'{ord(char):x}' for char in my_str)
print(result)  # 👉️ 62 6f 62 62 79 68 61 64 7a 2e 63 6f 6d