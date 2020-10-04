"""

This program converts a given sentence into a sequnce of digits which represent its ASCII value

"""
value=list(map(str,input().split()))
for i in range(len(value)):
    for a in value[i]:
        print(ord(a),end="")
    print("32",end="")
