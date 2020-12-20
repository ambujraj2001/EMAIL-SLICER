#email slicer

import random
print("ENTER EMAIL eg- abc@gmail.com")
s=input()
t=int(s.index("@"))
l=len(s)
print("USERNAME IS ",s[0:t])
t=t+1
print("DOMAIN NAME IS ",s[t:l])

