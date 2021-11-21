def CNFtoDict(file):
    R = {}
    filehasil = open(file,"r")
    filehasil2 = open(file,"r")
    hasil = filehasil.read()    
    hasil = hasil.split("\n")
    for i in range (0,len(hasil)):
        temp = filehasil2.readline()
        temp2 = temp.split(" -> ")
        temp2[1] = temp2[1].replace(" \n","")
        a = temp2[0]
        b = temp2[1]
        b2 = b.split("|")
        for j in range (0,len(b2)):
            b3 = b2[j].split()
            if R.get(a) == None:
                R.update({a : [b3]})
            else :
                (R.get(a)).append(b3)
    return R



R = CNFtoDict("out.txt")
for i in range (0,50):
    print(list(R.items())[i])
