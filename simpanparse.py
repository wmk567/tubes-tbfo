def cykParse(w,R):
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
    

        if "START" in tabel[0][0] :
            return True
        else:
            return False
    
    else :
        return True