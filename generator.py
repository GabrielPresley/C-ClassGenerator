name = input("CLASS NAME: ")
libs = input("DEFAULT LIBS? (bool): ")
gets = input("GETS FOR ALL VARS? (bool): ")
sets = input("SETS FOR ALL VARS? (bool): ")

vars = input("NUMBER OF VARS: ")
varsList = []
for i in range(0, int(vars)):
    varsList.append(input("VARIABLE NAME: "))

functions = input("NUMBER OF FUNCTIONS: ")
funcList = []
for i in range(0, int(functions)):
    funcList.append(input("FUNCTION NAME: "))

test = input("TEST (bool): ")
if test:
    testCount = input("NUMBER OF TESTS: ")

#PRINTING

if(libs):
    print("#include <iostream>")
    print("#include <string>")
    print("using namespace std;\n\n")

print("class ", name, "{")
print("\tpublic:")

for x in range(0, int(vars)):
    print("\t\t (//TODO TYPE)",varsList[x])

print("\n\n")

if(gets):
    for x in range(0, int(vars)):
        print("\tvoid get" + varsList[x].capitalize() + "(){")
        print("\t\treturn ", varsList[x])
        print("\t}")

if(sets):
    for x in range(0, int(vars)):
        print("\t//TODO TYPE set" + varsList[x].capitalize() + "(//TODO TYPE INPUT){")
        print("\t\t", varsList[x]," = INPUT")
        print("\t}")

for i in range(0, int(functions)):
    print("\t",funcList[i]+"(){")
    print("\t\t//TODO FUNCTION BODY")
    print("\t}")

print("\n\nint main(){")
if test:
    for i in range(0, int(testCount)):
        print("\t", name, name+str(i))

print("\n\n")
if sets:
    for i in range(0, int(vars)):
        print("\t",name+str(i)+".set"+varsList[i]+"();")

print("\n\n")

if gets:
    for i in range(0, int(vars)):
        print("\tcout <<", name+str(i)+".get"+varsList[i]+"();")
print("\n\n")

for i in range(0, int(functions)):
    print("\t"+funcList[i]+"();")


print("}")
