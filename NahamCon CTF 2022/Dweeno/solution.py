f = open('./resource/output.txt', 'r')
result = ''
while True:
    binary = f.readline()
    if not binary:
        break
    result += chr(int(binary, 2) ^ int('01010101', 2))
print(result)
