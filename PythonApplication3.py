code = bytearray()

with open('weather.data','rb') as f:
    data=f.read()
double=[]
oldscode = 0
for i in range(0,len(data),32):
    strg = ''
    for j in range (0,24):
        if data[i+j] != 0:
           strg = strg + chr(data[i+j])
    bte1 = data[i+31] & 0x7f
    bte2 = data[i+30] & 0xf0
    if bte1 == 0x7f and bte2 == 0xf0 :
        number = data[i+24:i+31]
        scode = int.from_bytes(number, byteorder='little')
        scode &= 0x0fffffffffffff
        scode |= oldscode
        mask = 0xff
        mask <<= 44

        for k in range(0,6):
            symb = scode & mask
            symb >>= ((5 - k) * 8 + 4)
            print (symb)
            code.append(symb)
            mask >>= 8
        oldscode = scode & 0xf
        oldscode <<= 52 
print (code)