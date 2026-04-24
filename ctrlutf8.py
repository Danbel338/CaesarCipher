
# UTF-8 ENCODING
# HEX RANGE: 0000 -> 007F 
#   BINARY PATTERN: 0yyyxxxx
# HEX RANGE: 0080 -> 07FF
#   BINARY PATTERN: 110yxxxx 10yyxxxx
# HEX RANGE: 0800 -> FFFF
#   BINARY PATTERN: 1110xxxx 10yyxxxx 10yyxxxx
# HEDX RANGE: 01 0000 -> 10 FFFF
#   BINARY PATTERN: 11110xxx 10yyxxxx 10yyxxxx


MASK1 : int = 0b10000000
MASK2 : int = 0b11000000
MASK3 : int = 0b11100000
MASK4 : int = 0b11110000


hex_range = ((0x000,0x007F), (0x0080,0x07FF), (0x0800,0xFFFF), (0x010000,0x10FFFF))

def inrange(n : int,r : tuple):
    return r[0] <= n <= r[1]

def separate_chars(ls):
    for l in ls:
        byte_order(l) 
    return ls


def byte_order(n : int):
    if (n & MASK4) == MASK4:
        print(4)
        return 4
    elif (n & MASK3) == MASK3:
        print(3)
        return 3
    elif (n & MASK2) == MASK2:
        print(2)
        return 2
    elif (n & MASK1) == MASK1:
        print(1)
        return 1
    print(0)
    return 0



if __name__ == '__main__':
    separate_chars(bytearray("hol𝼞n9ncfña",'utf-8'))
