#Revese string using revesed function

def revString(s):
    p=reversed(s)
    for ch in p:
        print(ch)

s=input("Enter the string:\n")       #input-> Kunal
ans=revString(s)                     #output->  l
#                                               a
#                                               n
#                                               u
#                                               k


def revString(s):
    p=reversed(s)
    output=''.join(p)
    return output
    

s=input("Enter the string:\n")       #input-> Kunal
ans=revString(s)                     #output-> lanuk
print(ans)