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
    if reg == "FLAGS":
        return "111"
    else:
        return 0

        
def decimalToBinary(decimal):
    binrep = bin(decimal)[2:]
    return binrep.zfill(8)
    
    
def typeAerrors(listA):
    if(len(listA)==4):
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        if (re1!=0 and re1!="111" and re2!=0 and re2!= "111" and re3!=0 and re3!= "111") :
            return 1
        else:
            if (re1==0):
                print("syntax error: " + listA[1] + "is an invalid input for register")
                quit()
            if (re2==0):
                print("syntax error: " + listA[2] + "is an invalid input for register")
                quit()
            if (re3==0):
                print("syntax error: " + listA[3] + "is an invalid input for register")
                quit()
            if (re1=="111"):
                print("syntax error: FLAGS have been used instead of reg1")
                quit()
            if (re2=="111"):
                print("syntax error: FLAGS have been used instead of reg2")
                quit()
            if (re3=="111"):
                print("syntax error: FLAGS have been used instead of reg3")
                quit()
    else:
        print("syntax error: incorrect number of operands. required operands are 3 and given are " + str(len(listA)-1))
        quit()
       
        
def typeBerrors(listA):
    if(len(listA)==3):
        re1 = returnRegister(listA[1])
        if (re1!=0 and re1!="111"):
            val = listA[2]
            val = val[1:]
            num = int(val)
            if (num<=255 and num>=0):
                return 1
            else:
                print("syntax error: invalid input of imm value. the range should be 0 to 255")
                quit()
        else:
            if(re1==0):
                print("syntax error: " + listA[1] + "is an invalid input for register")
                quit()
            if (re1=="111"):
                print("syntax error: FLAGS have been used instead of reg1")
                quit()
    else:
        print("syntax error: incorrect number of operands. required operands are 2 and given are " + str(len(listA)-1))
        quit()
    
            
def typeCerrors(listA):
    if(len(listA)==3):
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        if (re1!=0 and re1!="111" and re2!=0 and re2!="111"):
            return 1
        else:
            if (re1==0):
                print("syntax error: " + listA[1] + "is an invalid input for register")
                quit()
            if (re2==0):
                print("syntax error: " + listA[2] + "is an invalid input for register")
                quit()
            if (re1=="111"):
                print("syntax error: FLAGS have been used instead of reg1")
                quit()
            if (re2=="111"):
                print("syntax error: FLAGS have been used instead of reg2")
                quit()
    else:
        print("syntax error: incorrect number of operands. required operands are 2 and given are " + str(len(listA)-1))
        quit()
        
        
def typeDerrors(listA, listOfVar, label_dict, addressOfVar):
    check_var = 0
    if(len(listA)==3):
        re1 = returnRegister(listA[1])
        if (re1!=0 and re1!="111" and len(listOfVar)!=0):
            for i in range (len(listOfVar)):
                if (listA[2]==listOfVar[i]):
                    check_var=1
                    return addressOfVar[i]
            if(check_var==0):
                print("syntax error: wrong variable " + listA[2] + " has been used ")
                quit()
            if (listA[2] in label_dict):
                print("syntax error: label is being used as a variable")
                quit()
        else:
            if(re1==0):
                print("syntax error: " + listA[1] + "is an invalid input for register")
                quit()
            if (re1=="111"):
                print("syntax error: FLAGS have been used instead of reg1")
                quit()
            if(len(listOfVar)==0):
                print("syntax error: no variable declaration but variable " + listA[2] + " has been used")
                quit()
    else:
        print("syntax error: incorrect number of operands. required operands are 2 and given are " + str(len(listA)-1))
        quit()

    
def typeEerrors(listA, listOfVar , label_dict):
    if(len(listA)==2):
        if (listA[1] in listOfVar):
            print("syntax error: variable is being used as a label")
            quit()
        elif (listA[1] in label_dict):
            print("syntax error: label " + listA[1] + " does not exist" )
            quit()
        else:
            mem_addr = label_dict[listA[1]] 
            return mem_addr
    else:
        print("syntax error: incorrect number of operands. required operand is 1 and given are " + str(len(listA)-1))
        quit()
        

def mov_error(listA):
    if(len(listA)==3):
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        if (re1!=0 and re1!= "111" and re2!=0):
            return 1
        else:
            if (re1==0):
                print("syntax error: " + listA[1] + "is an invalid input for register")
                quit()
            if (re2==0):
                print("syntax error: " + listA[2] + "is an invalid input for register")
                quit()
            if (re1=="111"):
                print("syntax error: FLAGS have been used instead of reg1")
                quit()
    else:
        print("syntax error: incorrect number of operands. required operands are 2 and given are " + str(len(listA)-1))
        quit()
    
        
def check_valid_label(label_name, var_dict):
    # if label not valid print error and quit program
    if(label_name in var_dict):
        print("syntax error: variable cannot be used as a label" + str(label_name))
        quit()


def extract_label(content_list, i, label_dict, var_dict):
    list1 = (content_list[i]).split(":")
    if (len(list1)==2):
        check_valid_label(list1[0], var_dict)
        label_dict[list1[0]]=i 
    elif (len(list1)>2):
        print("syntax error")
        quit()
    # else:
    #     print("syntax error: input label is not correct")
    #     quit()

    
def check_halt(content_list):
    # checking presence of halt
    for line in content_list:
        listA = line.split()
        if (listA[0] == "hlt"):
            halt_checker=int(1)
    if (halt_checker!=1):
        print("syntax error: halt instruction missing")
        quit()
    # checking if halt is last instruction or not
    main_lst = []
    for i in range(len(content_list)):
        a = content_list[i].split()
        main_lst.append(a)
    if (main_lst[len(content_list)-1][0]!="hlt"):
        print("syntax error: last instruction is not halt")
        quit()       
     
#returning binary code for each line
def returnCode(opCode, reg1, reg2, reg3, mem, imm ):
    final = ""
    if(opCode == Addition):
        final = opCode +"00"+ reg1+ reg2+ reg3
    elif(opCode == Subtraction):
        final = opCode +"00"+ reg1+ reg2+ reg3
    elif(opCode == MoveImmediate):
        final = opCode + reg1 + imm
    elif(opCode == MoveRegister):
        final = opCode + reg1 + reg2
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

         
label_dict = {}
var_dict = {}


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

#reading input line by line
with open("data_file.txt") as f:
    content_list = f.readlines()
    while "" in content_list:
        content_list.remove("")
binary_output = []
instructionCounter = 0
varCounter = 0
listOfVar = []
addressOfVar = []
halt_checker = int(0)    
    


#checking if variabe name is correct or not
for line in content_list:
    if line != "\n":
        listA = line.split() 
        if (listA [0] == "var" and len(listA)==2):
            listOfVar.append(listA[1])
            var_dict[listA[1]]=0
            varCounter = varCounter + 1
        elif(listA [0] == "var" and len(listA)!=2):
            print("syntax error: invalid variable name , variable name cannot include spaced characters ")
            quit()
        else:
            instructionCounter = instructionCounter + 1
    else:
        pass

        
    
for i in range(varCounter):
    bi = decimalToBinary(instructionCounter)
    addressOfVar.append(bi)
    instructionCounter = instructionCounter + 1

program_len = len(content_list)

for i in range(varCounter , program_len):
    extract_label(content_list, i-varCounter, label_dict, var_dict)
    

#dealing each input one by one
for line in range(varCounter,len(content_list)):
    if content_list[line] == "\n":
        pass
    else:
        listA = content_list[line].split() 
        
        
        #addition
        if listA[0] == "add":
            typeAerrors(listA) 
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
            re3 = returnRegister(listA[3])
            
            binary_output.append(returnCode(Addition, re1, re2, re3, 0, 0))
            
                
        #subtraction
        elif listA[0] == "sub": 
            typeAerrors(listA) 
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
            re3 = returnRegister(listA[3])
            
            binary_output.append(returnCode(Subtraction, re1, re2, re3, 0, 0))
            
            
        #moving value
        elif listA[0] == "mov":
            char = listA[2]
            char = char[:1]     
            if(char == "$"):
                typeBerrors(listA) 
                re1 = returnRegister(listA[1])
                val = listA[2]
                val = val[1:]
                num = int(val)
                bi = decimalToBinary(num)
                binary_output.append(returnCode(MoveImmediate, re1, 0, 0, 0, bi))         
            else:
                mov_error(listA)
                re1 = returnRegister(listA[1])
                re2 = returnRegister(listA[2])
                
                binary_output.append(returnCode(MoveRegister, re1, re2, 0, 0, 0) )
            
            
        #load value
        elif listA[0] == "ld":
            typeDerrors(listA, listOfVar, label_dict, addressOfVar)
            re1 = returnRegister(listA[1])
            
            binary_output.append(returnCode(Load, re1, 0, 0, typeDerrors(listA, listOfVar, label_dict, addressOfVar) , 0))
            
        
        #store
        elif listA[0] == "st": 
            typeDerrors(listA, listOfVar, label_dict, addressOfVar)
            re1 = returnRegister(listA[1])
            
            binary_output.append(returnCode(Store, re1, 0, 0, typeDerrors(listA, listOfVar, label_dict, addressOfVar), 0))

            
        #multiply
        elif listA[0] == "mul":  
            typeAerrors(listA)
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
            re3 = returnRegister(listA[3])
            
            binary_output.append(returnCode(Multiply, re1, re2, re3, 0, 0))

        #divide
        elif listA[0] == "div":
            typeCerrors(listA) 
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
                
            binary_output.append(returnCode(Divide, re1, re2, 0, 0, 0)  )
                

        #rightShift
        elif listA[0] == "rs":  
            typeBerrors(listA)
            re1 = returnRegister(listA[1])
            val = listA[2]
            val = val[1:]
            num = int(val)
            bi = decimalToBinary(num)
            binary_output.append(returnCode(RightShift, re1, 0, 0, 0, bi) )   

        #leftShift
        elif listA [0] == "ls":
            typeBerrors(listA)
            re1 = returnRegister(listA[1])
            val = listA[2]
            val = val[1:]
            num = int(val)
            bi = decimalToBinary(num)
            binary_output.append(returnCode(LeftShift, re1, 0, 0, 0, bi) )   
                
                
        #exclusive OR
        elif listA[0] == "xor":  
            typeAerrors(listA)
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
            re3 = returnRegister(listA[3])
            
            binary_output.append(returnCode(ExclusiveOR, re1, re2, re3, 0, 0))
            

        #OR
        elif listA[0] == "or":  
            typeAerrors(listA)
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
            re3 = returnRegister(listA[3])
            
            binary_output.append(returnCode(Or, re1, re2, re3, 0, 0))
        

        #AND
        elif listA[0] == "and":  
            typeAerrors(listA)
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
            re3 = returnRegister(listA[3])
            
            binary_output.append(returnCode(And, re1, re2, re3, 0, 0))

        #invert
        elif listA[0] == "not":  
            typeCerrors(listA)
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
                
            binary_output.append(returnCode(Invert, re1, re2, 0, 0, 0) )
            

        #compare
        elif listA[0] == "cmp":  
            typeCerrors(listA)
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
                
            binary_output.append(returnCode(Compare, re1, re2, 0, 0, 0) )
            

        #unconditional jump
        elif listA [0] == "jmp":
            typeEerrors(listA, listOfVar , label_dict)
            
            binary_output.append(returnCode(UnconditionalJump, 0, 0, 0, typeEerrors(listA, listOfVar , label_dict), 0))
            

        #jump if less than
        elif listA [0] == "jlt":  
            typeEerrors(listA, listOfVar , label_dict)
            
            binary_output.append(returnCode(JumpIfLessThan, 0, 0, 0, typeEerrors(listA, listOfVar , label_dict), 0))
            
        
        # jump if greater than 
        elif listA [0] == "jgt":  
            typeEerrors(listA, listOfVar , label_dict)
            
            binary_output.append(returnCode(JumpIfGreaterThan, 0, 0, 0, typeEerrors(listA, listOfVar , label_dict), 0))
        
        
        #jump if equal
        elif listA [0] == "je":
            typeEerrors(listA, listOfVar , label_dict) 
            
            binary_output.append(returnCode(JumpIfEqual, 0, 0, 0, typeEerrors(listA, listOfVar , label_dict), 0))
            

        #halt
        elif listA [0] == "hlt": 
            binary_output.append(returnCode(Halt, 0, 0, 0, 0, 0))
            
        #incorrect opCode
        else:
            if(listA[0]=="var"):
                print("syntax error: variable declaration has been done in middle of the code. it should be done at the start")
                quit()
            else:
                print("syntax error: incorrect opCode input " + listA[0])
                quit()
                
g = open("binary.txt", "w+")
strI = ""
for output in binary_output:
    strI = strI + output + "\n"
g.write(strI)
g.close()