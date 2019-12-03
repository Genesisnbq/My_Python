print(type('ffff'))  # str
print(type(b'ffff'))  # byte

# bytes 时 字节的序列, str 时 字符的序列
# str-> bytes  -> encode

print('='*20)

s1 = '中'
b1 = s1.encode('utf-8')
print(b1)

print('='*20)

b1 = b1.decode('utf-8')
print(b1)

print('='*20)

# 拓展 str-> bytes
s = '倪彬琪'
b1 = bytes(s, encoding='utf-8')
b2 = bytes(s, encoding='GBK')
print(b1)
print(b2)

print('='*20)  # =============================

s1 = str(b1, encoding='utf-8')
s2 = str(b2, encoding='GBK')
print(s1)
print(s2)
print('='*20)  # =============================

# bytearray
s1 = '你好, 朦胧'
b1 = bytearray(s1.encode('utf-8'))
print(b1)
print(type(b1))
print(b1.decode('utf-8'))

print('='*20)  # =============================

# utf-8 3个字节
b1[:6] = bytearray('美丽', encoding='utf-8')
print(b1)
print(b1.decode('utf-8'))
