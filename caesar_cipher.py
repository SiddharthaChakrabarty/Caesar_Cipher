def caesar(text,s):
    output = ""
    for num in range(len(text)):
        if(text[num] == " "):
            output += " "
        elif(text[num].isupper()):
            change = ((ord(text[num])-65+s)%26) + 65
            output += str(chr(change))
        else:
            change = ((ord(text[num])-97+s)%26) + 97
            output += str(chr(change))
        
    return output

def decode(text):
    print("\n")
    for s in range(26):
        output = ""
        for num in range(len(text)):
            if(text[num] == " "):
                output += " "
            elif(text[num].isupper()):
                change = ((ord(text[num])-65-s)%26) + 65
                output += str(chr(change))
            else:
                change = ((ord(text[num])-97-s)%26) + 97
                output += str(chr(change))
        print(f"Hacking Key {s} : {output}")
    
print("\n\nWELCOME TO THE CAESAR CIPHER!!!!\n")
cont = True
while cont:
    opt = input("\nDo you want to encode or decode a string : ")
    if (opt[0].lower() == "e"):
        text = input("\nEnter the string to be encoded : ")
        s = int(input("\nEnter the shift that you want : "))
        print("\nEncoded string is : ",caesar(text,s))
    elif(opt[0].lower() == "d"):
        text = input("\nEnter the string to be decoded : ")
        decode(text)
    else:
        print("\nWrong input!!!")
    check = input("\nDo you want to try again(Y or N) : ")
    if (check[0].upper() == "Y"):
        cont = True
    else:
        cont = False
print("\nTHANK YOU FOR VISITING THE CAESAR CIPHER!!!")