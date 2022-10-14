phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
# for i in range(4):
#     plist.pop() # Don't pa
# plist.remove("D") # on't pa
# plist.remove("'") # [o , n , t, "", p, a]
# plist.extend([plist.pop(), plist.pop()]) # [o,n,t," ",a,p]
# plist.insert(2,plist.pop(3))
# new_phrase = "".join(plist)
new_phrase = "".join(plist[1:3:1])
new_phrase = new_phrase + " " + "".join([plist[4],plist[7],plist[6]])

print(new_phrase)
#print(plist)
# on tap