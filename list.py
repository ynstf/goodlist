print("passwords posibility !")
print(">empty + enter to exit<")
cw=0
words = list()
wordls = list()
mult = list()
while True:
    cw+=1
    word = input(f"word N°:{cw} >> ")
    if word == "":
        break
    words.append(word)


for w in words:
    wordls.append(w.lower())
    wordls.append(w.upper())
    wordls.append(w.capitalize())
#print(wordls)
def unique(list1):
    # initialize a null list
    unique_list = []
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    return unique_list
words = unique(wordls)
#print(words)
for i in words:
    mult.append(i)
    for j in range(len(words)-1,0,-1):
        mult.append(i+words[j])
        for k in range(len(words)):
            mult.append(i+words[j]+words[k])
#print(mult)
with open("BESTLIST.txt","w") as file:
    for word in unique(mult):
        file.write(word)
        file.write("\n")
    file.close
    print("your posible passwords has saved in BESTLIST.txt ")
