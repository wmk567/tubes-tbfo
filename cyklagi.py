def lexer(file):
    hasil = open(file,"r")
    hasil2 = hasil.read()

    result = []
    operator = ['!','+','-','*','/','%','(',')','=','<','>',',','"','\'','==','<=','>=','!=',':']
    keyword = ["False","None","True","and","as","assert","break","class","continue","def","del","elif","else","except","finally",
            "for","from","global","if","import","in","is","lambda","nonlocal","not","or","pass","raise","return","try",
            "while","with","yield","range"]
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    number = ["1","2","3","4","5","6","7","8","9","0"]
    word = ""
    i = 0
    while (i < len(hasil2)):
        if hasil2[i] in operator: 
            if word != "" : 
                result.append(word)
                word = ""
            if i+1<len(hasil2):
                if hasil2[i+1] in operator:
                    word = ""
                    word = hasil2[i] + hasil2[i+1]
                    if word in operator :
                        result.append(word)
                        word = ""
                        i = i + 1
                    else : 
                        result.append(hasil2[i])
                        result.append(hasil2[i+1])
                        i = i+1
                        word = ""
                elif hasil2[i+1] not in operator:
                    result.append(hasil2[i])
            elif i+1>=len(hasil2):
                result.append(hasil2[i])
        
        elif hasil2[i] == "\n" :
            if word != "" :
                result.append(word)
                word = ""
        elif i == (len(hasil2)-1) :
            word = word + hasil2[i]
            print(word)
            result.append(word)
            word = ""
        elif hasil2[i] not in operator and hasil2[i] != " ": 
            word = word + hasil2[i]
        elif hasil2[i] == " " :
            if word != "" :
                result.append(word)
                word = ""
       
        i += 1
    print(hasil2)
    print(len(hasil2))

    j = 0
    while(j<len(result)):
        if ((j+2)<len(result)):
            if ((result[j] == "'" and result[j+1] == "'" and result[j+2] == "'") or (result[j] == '"' and result[j+1] == '"' and result[j+2] == '"')):
                if (result[j] == "'" and result[j+1] == "'" and result[j+2] == "'"):
                    k = j+3
                    stop = False
                    while (k<len(result) and stop == False):
                        if (result[k] == "'" and result[k+1] == "'" and result [k+2] == "'"):
                            stop = True
                        else :
                            result[k] = "word"
                            k += 1
                    j = k+1
                elif (result[j] == '"' and result[j+1] == '"' and result[j+2] == '"'):
                    k = j+3
                    stop = False
                    while (k<len(result) and stop == False):
                        if (result[k] == '"' and result[k+1] == '"' and result [k+2] == '"'):
                            stop = True
                        else :
                            result[k] = "word"
                            k += 1
                    j = k+1
        
        if (j<len(result)):
            if (result[j] == '\"' or result[j] == "\'"):
                l = j+1
                stop3 = False
                if result[j] == '\"' :
                    while(l<len(result) and stop3 == False):
                        if (result[l] == '\"'):
                            stop3 = True
                        else :
                            result[l] = "word"
                            l += 1
                    j = l
                elif result[j] == '\'' :
                    while(l<len(result) and stop3 == False):
                        if (result[l] == '\''):
                            stop3 = True
                        else :
                            result[l] = "word"
                            l += 1
                    j = l
            
            
            elif result[j] not in keyword and result[j] not in operator:
                temp = result[j]
                if temp[0] in alphabet:
                    result[j] = "var"
                if temp[0] in number:
                    isNum = True
                    for k in temp:
                        if k in alphabet or k in operator:
                            isNum = False
                    if isNum:
                        result[j] = "num"
                    else : 
                        result[j] = "NaN"

        j += 1
    m = 0
    while (m+1<len(result)):
        if (result[m] == "word" and result[m+1] == "word"):
            del result[m+1]
        else:
            m+=1
    print(result)
    return result

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

def cykParse3(w,R):
    length = len(w)
    tabel = [[[] for j in range (0,length)] for i in range (0,length)]

    if length != 0 :
        for i in range (0,length):
            for rule,value in R.items():
                for var in value:
                    if len(var) == 1 and var[0] == w[i]:
                        tabel[0][i].append(rule)
        for j in range (1,length):
            for k in range (0,length-j):
                for l in range (0,j):
                    for rule,value in R.items():
                        for var in value:
                            if len(var)==2 and var[0] in tabel[l][k] and var[1] in tabel[j-l-1][k+l+1]:
                                tabel[j][k].append(rule)
    
        for i in range (0,length):
            print(tabel[i])

        if "START" in tabel[length-1][0] :
            print("True")
        else:
            print("False")

    else :
        print("True")

def cykParse4(w,R):
    length = len(w)
    tabel = [[[] for j in range (0,length)] for i in range (0,length)]

    if length != 0 :
        for i in range (0,length):
            for rule,value in R.items():
                for var in value:
                    if len(var) == 1 and var[0] == w[i]:
                        tabel[length-1][i].append(rule)
        for j in range (length-2,-1,-1):
            for k in range (0,j+1):
                for l in range (j,length):
                    for rule,value in R.items():
                        for var in value:
                            if len(var)==2 and var[0] in tabel[l][k] and var[1] in tabel[length-l+j][length-l+k]:
                                tabel[j][k].append(rule)
    
        for i in range (0,length):
            print(tabel[i])

        if "START" in tabel[0][0] :
            print("True")
        else:
            print("False")

    else :
        print("True")

R = CNFtoDict("isi_nama.txt")
import sys
simpan = sys.argv[1]
w = lexer(simpan)
cykParse3(w,R)
cykParse4(w,R)