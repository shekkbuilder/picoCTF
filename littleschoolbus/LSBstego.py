flag = ""

with open("littleschoolbus.bmp", "rb") as img:
    # skip 54 bytes because of the .bmp header
    data = img.read()[54:418]
    b = bytearray(data)

for byte in b:
    # store every LSB(bit) in the flag
    flag += str(byte & 0x1)

'''
    Assuming that the flag will be ascii-based,
    we will be looking for 1-byte chunks since each char is 1-byte long.
    Thus, the existence of the 'skip' variable so we can read the content
    of the flag per-byte.
'''
skip = 8
j = 0

try:
    for i in flag:
        print chr(int(hex(int( (flag[ j: j + 8]), 2)), 16)),
        j+=8
# throws a meaningless excpetion to ruin our 1337 output
except:
    pass
