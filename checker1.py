import sys
import simpanparse
import lexer_1
import CNFtoDict

simpan = sys.argv[1]
R = CNFtoDict.CNFtoDict("cnf.txt")
w = lexer_1.lexer(simpan)

finale = simpanparse.cykParse(w,R)

if finale:
    print("Accepted")
else:
    print("Syntax Error")