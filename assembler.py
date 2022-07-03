def returnRegister(reg):
    if reg == "R0":
        return "000"
    if reg == "R1":
        return "001"
    if reg == "R2":
        return "010"
    if reg == "R3":
        return "011"
    if reg == "R4":
        return "100"
    if reg == "R5":
        return "101"
    if reg == "R6":
        return "110"
    else:
        return 0

        
def decimalToBinary(decimal):
    binrep = bin(decimal)[2:]
    return binrep.zfill(8)
    
# hardcoding codes
R0 = "000"
R1 = "001"
R2 = "010"
R3 = "011"
R4 = "100"
R5 = "101"
R6 = "110"
FLAGS = "111"
Addition = "10000"
Subtraction = "10001"
MoveImmediate = "10010"
MoveRegister = "10011"
Load = "10100"
Store = "10101"
Multiply = "10110"
Divide = "10111"
RightShift = "11000"
LeftShift = "11001"
ExclusiveOR = "11010"
Or = "11011"
And = "11100"
Invert = "11101"
Compare = "11110"
UnconditionalJump = "11111"
JumpIfLessThan = "01100"
JumpIfGreaterThan = "01101"
JumpIfEqual = "01111"
Halt = "01010"

#returning binary code for each line

def returnCode(opCode, reg1, reg2, reg3, mem, imm ):
    final = ""
    if(opCode == Addition):
        final = opCode +"00"+ reg1+ reg2+ reg3
    elif(opCode == Subtraction):
        final = opCode +"00"+ reg1+ reg2+ reg3
    elif(opCode == MoveImmediate):
        pass
    elif(opCode == MoveRegister):
        pass
    elif(opCode == Load):
        final = opCode + reg1+ mem
    elif(opCode == Store):
        final = opCode + reg1+ mem
    elif(opCode == Multiply):
        final = opCode +"00"+ reg1+ reg2+ reg3
    elif(opCode == Divide):
        final = opCode + "00000" + reg1+ reg2
    elif(opCode == RightShift):
        final = opCode + reg1 + imm
    elif(opCode == LeftShift):
        final = opCode + reg1 + imm
    elif(opCode == ExclusiveOR):
        final = opCode +"00"+ reg1+ reg2+ reg3
    elif(opCode == Or):
        final = opCode +"00"+ reg1+ reg2+ reg3
    elif(opCode == And):
        final = opCode +"00"+ reg1+ reg2+ reg3
    elif(opCode == Invert):
        final = opCode + "00000" + reg1+ reg2
    elif(opCode == Compare):
        final = opCode + "00000" + reg1+ reg2
    elif(opCode == UnconditionalJump):
        final = opCode + "000" + mem
    elif(opCode == JumpIfLessThan):
        final = opCode + "000" + mem
    elif(opCode == JumpIfGreaterThan):
        final = opCode + "000" + mem
    elif(opCode == JumpIfEqual):
        final = opCode + "000" + mem
    elif(opCode == Halt):
        final = opCode + "00000000000"
    
    return final


#reading input line by line
with open("data_file.txt") as f:
    content_list = f.readlines()
g = open("binary.txt", "x")
instructionCounter = 0
varCounter = 0
listOfVar = []
addressOfVar = []
halt_checker = int(0)    
    
# checking presence of halt
for line in content_list:
    listA = line.split()
    if (listA[0] == "hlt"):
        halt_checker=int(1)
if (halt_checker!=1):
    print("syntax error: halt instruction missing")


# checking if halt is last instruction or not
main_lst = []
for i in range(len(content_list)):
    a = content_list[i].split()
    main_lst.append(a)
if (main_lst[len(content_list)-1][0]!="hlt"):
    print("syntax error: last instruction is not halt")

    
#finding the starting memory address of variables
for line in content_list:
    listA = line.split() 
    if (listA [0] == "var" and len(listA)==2):
        listOfVar.append(listA[1])
        varCounter = varCounter + 1
    elif(listA [0] == "var" and len(listA)!=2):
        print("syntax error: invalid variable name")
    else:
        instructionCounter = instructionCounter + 1
for i in range(varCounter):
    bi = decimalToBinary(instructionCounter)
    addressOfVar.append(bi)
    instructionCounter = instructionCounter + 1


#dealing each input one by one
for line in content_list:
    listA = line.split() 
    
    #addition
    if listA [0] == "add": 
        try: 
            len(listA)==4
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
            re3 = returnRegister(listA[3])
            if (re1!=0 and re2!=0 and re3!=0):
                returnCode(Addition, re1, re2, re3, 0, 0)
        except:
            print("syntax error: invalid input for addition")
        
    #subtraction
    if listA [0] == "sub":  
        try: 
            len(listA)==4
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
            re3 = returnRegister(listA[3])
            if (re1!=0 and re2!=0 and re3!=0):
                returnCode(Subtraction, re1, re2, re3, 0, 0)
        except:
            print("syntax error: invalid input for subtraction")
        

    #moving value
    if listA [0] == "mov":  
        
        if listA[2] == "R0" or listA[2] == "R1" or listA[2] == "R2" or listA[2] == "R3" or listA[2] == "R4" or listA[2] == "R5" or listA[2] == "R6":
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
            returnCode(MoveRegister, re1, re2, 0, 0, 0)
        else:
            re1 = returnRegister(listA[1])
            val = listA[2]
            val = val[1:]
            if (val<=255 and val>=0):
                num = int(val)
                bi = decimalToBinary(num)
                returnCode(MoveImmediate, re1, 0, 0, 0, bi)
            else:
                print("syntax error: invalid input of imm value")
        
    #load value
    if listA [0] == "ld": 
        try:
            len(listA)==3
            re1 = returnRegister(listA[1])
            if (re1!=0 and len(listOfVar)!=0):
                for i in range (len(listOfVar)):
                    if (listA[2]==listOfVar[i]):
                        returnCode(Load, re1, 0, 0, addressOfVar[i], 0)
        except:
            print("syntax error: error in load instruction")
    
    #store
    if listA [0] == "st": 
        try:
            len(listA)==3
            re1 = returnRegister(listA[1]) 
            if (re1!=0 and len(listOfVar)!=0):
                for i in range (len(listOfVar)):
                    if (listA[2]==listOfVar[i]):
                        returnCode(Store, re1, 0, 0, addressOfVar[i], 0)
        except:
            print("syntax error: error in store instruction")
        
    
    #multiply
    if listA [0] == "mul":  
        try: 
            len(listA)==4
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
            re3 = returnRegister(listA[3])
            if (re1!=0 and re2!=0 and re3!=0):
                returnCode(Multiply, re1, re2, re3, 0, 0)
        except:
            print("syntax error: invalid input for multiplication")
        

    #divide
    if listA [0] == "div":  
        try:
            len(listA==3)
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
            if (re1!=0 and re2!=0):
                returnCode(Divide, re1, re2, 0, 0, 0)
        except:
            print("syntax error: invalid input for divide")
        

    #rightShift
    if listA [0] == "rs":  
        try:
            len(listA==3)
            re1 = returnRegister(listA[1])
            if (re1!=0):
                val = listA[2]
                val = val[1:]
                num = int(val)
                if (num<=255 and num>=0):
                    bi = decimalToBinary(num)
                    returnCode(RightShift, re1, 0, 0, 0, bi)
                else:
                    print("syntax error: invalid input of imm value")
        except:
            print("syntax error: invalid input of right shift")


    #leftShift
    if listA [0] == "ls":  
        try:
            len(listA==3)
            re1 = returnRegister(listA[1])
            if (re1!=0):
                val = listA[2]
                val = val[1:]
                num = int(val)
                if (num<=255 and num>=0):  
                    bi = decimalToBinary(num)
                    returnCode(LeftShift, re1, 0, 0, 0, bi)
                else:
                    print("syntax error: invalid input of imm value")
        except:
            print("syntax error: invalid input of left shift")
            
            
    #exclusive OR
    if listA [0] == "xor":  
        try: 
            len(listA)==4
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
            re3 = returnRegister(listA[3])
            if (re1!=0 and re2!=0 and re3!=0):
                returnCode(ExclusiveOR, re1, re2, re3, 0, 0)
        except:
            print("syntax error: invalid input for ExclusiveOR")
        


    #OR
    if listA [0] == "or":  
        try: 
            len(listA)==4
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
            re3 = returnRegister(listA[3])
            if (re1!=0 and re2!=0 and re3!=0):
                returnCode(Or, re1, re2, re3, 0, 0)
        except:
            print("syntax error: invalid input for OR")
       


    #AND
    if listA [0] == "and":  
        try: 
            len(listA)==4
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
            re3 = returnRegister(listA[3])
            if (re1!=0 and re2!=0 and re3!=0):
                returnCode(And, re1, re2, re3, 0, 0)
        except:
            print("syntax error: invalid input for And")
        

    #invert
    if listA [0] == "not":  
        try:
            len(listA==3)
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
            if (re1!=0 and re2!=0):
                returnCode(Invert, re1, re2, 0, 0, 0)
        except:
            print("syntax error: invalid input for Invert")
        
        
        

    #compare
    if listA [0] == "cmp":  
        try:
            len(listA==3)
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
            if (re1!=0 and re2!=0):
                returnCode(Compare, re1, re2, 0, 0, 0)
        except:
            print("syntax error: invalid input for Invert")
        
        

    #unconditional jump
    if listA [0] == "jmp":
        try:
            len(listA==2)
            mem_addr = listA[1]
            returnCode(UnconditionalJump, 0, 0, 0, mem_addr, 0)
        except:
            print("syntax error: invalid input for UnconditionalJump")
        

    #jump if less than
    if listA [0] == "jlt":  
        try:
            len(listA==2)
            mem_addr = listA[1]
            returnCode(JumpIfLessThan, 0, 0, 0, mem_addr, 0)
        except:
            print("syntax error: invalid input for JumpIfLessThan")
        
    
    # jump if greater than 
    if listA [0] == "jgt":  
        try:
            len(listA==2)
            mem_addr = listA[1]
            returnCode(JumpIfGreaterThan, 0, 0, 0, mem_addr, 0)
        except:
            print("syntax error: invalid input for JumpIfGreaterThan")
       
    
    #jump if equal
    if listA [0] == "je":  
        try:
            len(listA==2)
            mem_addr = listA[1]
            returnCode(JumpIfEqual, 0, 0, 0, mem_addr, 0)
        except:
            print("syntax error: invalid input for JumpIfEqualThan")
        

    #halt
    if listA [0] == "hlt": 
        returnCode(Halt, 0, 0, 0, 0, 0)
        
    #incorrect opCode
    else:
        print("syntax error: incorrect opCode")
