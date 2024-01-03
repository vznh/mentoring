# >! Section 1
x = ValueError
y = ValueError 
z = ValueError

"Don't touch this thing below."
print(f"{type(x)} {type(y)} {type(z)}")

# >! Section 2
a = ValueError
b = ValueError
c = ValueError

"Don't touch this thing below."
assert a == 26
assert b == 89
assert c == 5
"This will all be True within your terminal if everything is right!"

# >! Section 3
# Add a comment here
def add_numbers(x: int, y: int, z: float) -> float:
    return x + y + z
