
s=input()
#ans=s
if s==s.capitalize()and len(s)!=1 or s==s.lower() and len(s)!=1:
    print(s)
else:

    if s==s.upper():
        print(s.lower())
    elif len(s)==1:
        print(s.upper() if s.islower() else s.lower())
         
    else:
        #print("fuckoff")
        if s[0].islower() and s[1:].isupper() and len(s)!=1:
            print(s.capitalize())
        else:
            if len(s)!=1:
                 print(s)