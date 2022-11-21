def c0(words):
    for i in words:
        mult.append(i)
def c1(words):
    for i in words:
        mult.append(i)
        for j in range(len(words)-1,0,-1):
            mult.append(i+words[j])
def c2(words):
    for i in words:
        mult.append(i)
        for j in range(len(words)-1,0,-1):
            mult.append(i+words[j])
            for k in range(len(words)):
                mult.append(i+words[j]+words[k])
def c3(words):
    for i in words:
        mult.append(i)
        for j in range(len(words)-1,0,-1):
            mult.append(i+words[j])
            for k in range(len(words)):
                mult.append(i+words[j]+words[k])
                for l in range(len(words)-1,0,-1):
                    mult.append(i+words[j]+words[k]+words[l])
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

print("passwords posibility !")

c = int(input("level of complexity (0->3) : "))
while True:

    if c==0 or c==1 or c==2 or c==3:
        break
    else:
        c = int(input("pleae the level of complexity between 0 and 3 : "))

print(">empty + enter to exit<")

words = list()
wordls = list()
mult = list()
cw=0

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

words = unique(wordls)
#print(words)

if c==0:
    c0(words)
elif c==1:
    c1(words)
elif c==2:
    c2(words)
elif c==3:
    c3(words)

#print(mult)
with open("BESTLIST.txt","w") as file:
    for word in unique(mult):
        file.write(word)
        file.write("\n")
    file.close
    print("your possible passwords has saved in BESTLIST.txt ")
