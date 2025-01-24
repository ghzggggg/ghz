import textwrap
N = input()
long_string = input()
width = 80

formatted_string = textwrap.fill(long_string, width)
print(formatted_string)