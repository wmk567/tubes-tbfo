import lexer_2
import sys
import CNFtoDict
import simpanparse2

simpan = sys.argv[1]
R = CNFtoDict.CNFtoDict("cnf.txt")
w = lexer_2.lexer(simpan)

finale = simpanparse2.parseAkhir(w,R)

if finale:
    print("Accepted")
else:
    print("Syntax Error")






