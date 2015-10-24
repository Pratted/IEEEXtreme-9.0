ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def base62_encode(num, alphabet=ALPHABET):
    """Encode a number in Base X

    `num`: The number to encode
    `alphabet`: The alphabet to use for encoding
    """
    if (num == 0):
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def base62_decode(string, alphabet=ALPHABET):
    """Decode a Base X encoded string into the number

    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for encoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num

base = raw_input()

n = raw_input()
tmp = []
base_utf = []
for c in base:
    base_utf.append(ord(c))

tmp = base_utf[:]

for i in range(int(n)):
    target = raw_input()
    target_utf = []
    base_utf = tmp[:]
    for c in target:
        target_utf.append(ord(c))


    k = 0
    for  j in range(len(base_utf), len(target_utf)):
        base_utf.append(base_utf[k])
        k = (k+1)%(len(base_utf))

    xorurl = []
    for j in range(len(base_utf)):
        xorurl.append(target_utf[j] ^ base_utf[j])
    #print xorurl
    num = []
    num = xorurl[len(xorurl)-8:len(xorurl)]

    hexstr = ''
    hexstr += '0x' + '0'*(2-len(hex(num[0])[2:])) + hex(num[0])[2:]
    for j in range(1,len(num)):
        hexstr += '0'*(2-len(hex(num[j])[2:])) + hex(num[j])[2:]

    res = base62_encode(int(hexstr, 0))
    print base +"/"+ res