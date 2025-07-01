def encode(a):
    d = "bHf"
    e = "gLi"
    if len(a) > 3:
        c = a[1:] + a[0]  
        f = d + c + e  
        return f
    else:
        return a[::-1]  
def decode(encoded_a):
    n = encoded_a[3:-3]  
    if len(n) > 0:
        m = n[-1] + n[0:-1]  
        return m


x = int(input("Type 1 to encode\nType 2 to decode: "))  
a = input("Enter the text: ")

match x:
    case 1:
        result = encode(a)
        print("Encoded a:", result)
    case 2:
        result = decode(a)
        print("Decoded a:", result)
    case _:
        print("Invalid option. Please type 1 or 2.")
