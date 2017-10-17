def str_to_bin(st):
    
    return ' '.join(format(ord(x), 'b') for x in st)

def bin_to_str(bits):
    return ''.join(chr(int(bits[i*8:i*8+8],2)) for i in range(len(bits)//8))
    

print(str_to_bin('hi'))
print(bin_to_str("0110100001101001"))