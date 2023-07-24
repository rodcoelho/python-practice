nx = ['0','1','2','3','4','5','6','7','8','9']
lx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ux = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
mk = {}
for i in range(26):
    mk[lx[i]] = i

def cipher(message,shift):
    result = ''
    for chars in message:
        if chars in nx:
            place = nx.index(chars)
            try:
                result += nx[place+shift]
            except:
                result += nx[shift-(len(nx)-place)]
        elif chars in lx:
            place = lx.index(chars)
            try:
                result += lx[place+shift]
            except:
                result += lx[shift-(len(lx)-place)]
        elif chars in ux:
            place = ux.index(chars)
            try:
                result += ux[place+shift]
            except:
                result += ux[shift-(len(ux)-place)]
        else:
            result += chars
    return result

def prepdata(message,key):
    # make message into list of chars
    messagelist = []
    for chars in message:
        messagelist.append(chars)

    # make keylist
    keylist = []
    for chars in key:
        keylist.append(mk[chars])
    final_key = []
    for i in range(len(messagelist) // len(keylist) + 1):
        for elements in keylist:
            final_key.append(elements)
    return messagelist, keylist, final_key

def vigenere(message, key):
    messagelist, keylist, final_key = prepdata(message,key)
    result = ''
    for i in range(len(messagelist)):
        x = cipher(messagelist[i],final_key[i])
        result += x
    return result

def de_vigenere(message,key):
    messagelist, keylist, final_key = prepdata(message,key)
    result = ''
    for i in range(len(messagelist)):
        x = cipher(messagelist[i], -final_key[i])
        result += x
    return result

x = vigenere('My name is rodrigo', 'baad')
print(x)

y = de_vigenere(x, 'baad')
print(y)