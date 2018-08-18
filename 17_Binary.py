
# ==================
# 17_Binary.py
# ==================


# How to display binary in python
# Note that {0:>2} is for spacing. >2 means two spaces
# and on 0:>08b means 8 spaces with zeros filling the left side
# Note that adding b means to display in binary

for i in range(17):
    print("{0:>2} in binary is {0:>08b}".format(i))

print()
# Here we have (0:>02} which has 0 filling the left side.

for i in range(17):
    print("{0:>02} in binary is {0:>08b}".format(i))

# This is experimenting with high numbers to see how they display in binary

print()
for i in range(1000):
    print("{0:>3} in binary is {0:>016b}".format(i))

