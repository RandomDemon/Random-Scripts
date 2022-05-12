import time 

def encypt_func(txt, s):  
    result = ""  
    for i in range(len(txt)):  
        char = txt[i]   
        if (char.isupper()):  
            result += chr((ord(char) + s - 64) % 26 + 65)  
        else:  
            result += chr((ord(char) + s - 96) % 26 + 97)  
    return result
    
txt = input("What would you like to encrypt?")  
s = 4

time.sleep(1)
print("Plain txt : " + txt)  
time.sleep(1)
print("Shift pattern : " + str(s))  
time.sleep(1)
print("Cipher: " + encypt_func(txt, s))  
time.sleep(3)
