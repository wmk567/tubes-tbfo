def lexer(file):
    hasil = open(file,"r")
    simpan = open(file,"r")
    temp = hasil.read()
    temp2 = temp.split("\n")
    temp3 = len(temp2)


    result = [[] for x in range (temp3)]
    operator = ['!','+','-','*','/','%','(',')','=','<','>',',','"','\'','==','<=','>=','!=',':','[',']']
    keyword = ["False","None","True","and","as","assert","break","class","continue","def","del","elif","else","except","finally",
            "for","from","global","if","import","in","is","lambda","nonlocal","not","or","pass","raise","return","try",
            "while","with","yield","range","print"]
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    number = ["1","2","3","4","5","6","7","8","9","0"]
    word = ""
    i = 0
    j = 0

    while (j<temp3):
        hasil2 = simpan.readline()
        i = 0
        while (i < len(hasil2)):
            if hasil2[i] in operator: 
                if word != "" : 
                    result[j].append(word)
                    word = ""
                if i+1<len(hasil2):
                    if hasil2[i+1] in operator:
                        word = ""
                        word = hasil2[i] + hasil2[i+1]
                        if word in operator :
                            result[j].append(word)
                            word = ""
                            i = i + 1
                        else : 
                            result[j].append(hasil2[i])
                            result[j].append(hasil2[i+1])
                            i = i+1
                            word = ""
                    elif hasil2[i+1] not in operator:
                        result[j].append(hasil2[i])
                elif i+1>=len(hasil2):
                    result[j].append(hasil2[i])
            
            elif hasil2[i] == "\n" :
                if word != "" :
                    result[j].append(word)
                    word = ""

            elif i == (len(hasil2)-1) :
                word = word + hasil2[i]
                result[j].append(word)
                word = ""
            
            elif hasil2[i] not in operator and hasil2[i] != " ": 
                word = word + hasil2[i]
            
            elif hasil2[i] == " " :
                if word != "" :
                    result[j].append(word)
                    word = ""
        
            i += 1
        j += 1

    j = 0
    y = 0
    
    while(y<len(result)):
        j = 0
        while(j<len(result[y])):
            if (j+2<len(result[y])):
                if ((result[y][j] == "'" and result[y][j+1] == "'" and result[y][j+2] == "'") or (result[y][j] == '"' and result[y][j+1] == '"' and result[y][j+2] == '"')):
                    if (result[y][j] == "'" and result[y][j+1] == "'" and result[y][j+2] == "'"):
                        k = j+3
                        stop = False
                        while (y<len(result) and stop == False):
                            if (k+2<len(result[y]) and result[y][k] == "'" and result[y][k+1] == "'" and result[y][k+2] == "'"):
                                stop = True
                            elif (k > len(result[y])-1 and stop == False and y < len(result)):
                                y += 1
                                k = 0
                                j = 0
                            else :
                                result[y][k] = "word"
                                k += 1
                        j = k+1
                    elif (result[y][j] == "\"" and result[y][j+1] == "\"" and result[y][j+2] == "\""):
                        k = j+3
                        stop = False
                        while (k<len(result[y]) and stop == False):
                            if (result[y][k] == "\"" and result[y][k+1] == "\"" and result[y][k+2] == "\""):
                                stop = True
                            elif (k > len(result[y])-1 and stop == False and y < len(result)):
                                y += 1
                                k = 0
                                j = 0
                            else :
                                result[y][k] = "word"
                                k += 1
                        j = k+1
            
            if (j<len(result[y])):
                if (result[y][j] == '\"' or result[y][j] == "\'"):
                    l = j+1
                    stop3 = False
                    if result[y][j] == '\"' :
                        while(l<len(result[y]) and stop3 == False):
                            if (result[y][l] == '\"'):
                                stop3 = True
                            else :
                                result[y][l] = "word"
                                l += 1
                        j = l
                    elif result[y][j] == '\'' :
                        while(l<len(result[y]) and stop3 == False):
                            if (result[y][l] == '\''):
                                stop3 = True
                            else :
                                result[y][l] = "word"
                                l += 1
                        j = l
                
                
                elif result[y][j] not in keyword and result[y][j] not in operator:
                    temp = result[y][j]
                    if temp[0] in alphabet:
                        result[y][j] = "var"
                    if temp[0] in number:
                        isNum = True
                        for k in temp:
                            if k in alphabet or k in operator:
                                isNum = False
                        if isNum:
                            result[y][j] = "num"
                        else : 
                            result[y][j] = "NaN"

            j += 1
        y += 1

    m = 0
    z = 0
    while (z<len(result)):
        m = 0
        while (m+1<len(result[z])):
            if (result[z][m] == "word" and result[z][m+1] == "word"):
                del result[z][m+1]
            elif result[z][m] == " ":
                del result[z][m]
            else:
                m+=1

        if(m != 0):
            if result[z][m-1] == " ":
                del result[z][m-1]
        z += 1

    q = 0
    while (q<len(result)):
        if result[q] == [] or result[q] == ["word"]:
            del result[q]
        q += 1

    w = 0
    while (w<len(result)-1):
        if result[w][len(result[w])-1] == "word" and result[w+1][0] == "word":
            del result[w+1][0]
        w+=1
    
    return result

