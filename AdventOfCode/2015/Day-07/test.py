a = -124
if a < 0:
    a = a + 2**16

print(a, bin(a))
a = a >> 2
print(a, bin(a))
