"""

This program converts a sequnce of ASCII values to its corresponding character

"""
msg=str(input())
temp=0
for i in range(len(msg)):
    temp=temp*10+int(msg[i])
    if 126>=temp>=32:
        print(chr(temp),end="")
        temp=0
    
    
        
        
    
        
