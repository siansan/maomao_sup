a = "0003D3A8E6B3B2C2"


b = [ (a[i+2]+a[i+3]+a[i]+a[i+1]) for i in range(len(a)) if i%4 == 0 ]
b = b[::-1]
big5_str = "".join(b)
swapped_bytes = bytes.fromhex(big5_str).decode('big5', 'ignore')
print(swapped_bytes)