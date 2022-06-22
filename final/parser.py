# i used the skeleton code from lecture and added code to the advance function for
# the label instruction. i also changed and added some stuff to the skeleton code
# bc for some reason using the raw skeleton code would cause my code to break :(
# also I have a bunch of rando code commented out bc my code kept breaking so those rando
# codes were just there to help me figure out where and why my code broke

class Parser:
    # open file for future parsing
    def __init__(self, inputFileName, labels):
        self.inputFileLines = open(inputFileName).readlines()

        # print("inputFileLines:", self.inputFileLines)
        self.currentLineNum = 0
        self.ACinstructionCounter = -1
        self.currentInstruction = ""
        self.symbol = None
        self.dest = None
        self.comp = None
        self.jump = None

        self.skippables = ["//", "\n", ")"]

        self.searchLine = 0    
        self.increment = 16

        self.skippable_line = True
        searchEnd = self.currentInstruction.find(")")

        # Read all lines in the file one by one
        for line in self.inputFileLines:
            for skippable in self.skippables:
                # print("Line.strip(): " + str(line.strip()))
                # print("line.strip().startswith(skippable): " + str(line.strip().startswith(skippable)))
                
                if line.strip().startswith(skippable) or not line.strip():
                    break

            else:
                self.skippable_line = False
                
            self.searchLine += 1

            # For each line, check if line contains the string
            if line.strip().startswith("("):
                # print("line #: " + str(self.searchLine))
                self.searchLine -= 1
                # print("line: " + line)
                # print("self.symbol: " + self.symbol)
                labels.get(line[1:searchEnd-2])
                labels.add(line[1:searchEnd-2], self.searchLine+1)

        for line in self.inputFileLines:
            # print("==================line.strip()[1:] " + line.strip()[1:])
            if line.strip().startswith("@"):
                # print("==================line.strip()[1:] " + line.strip()[1:])
                if line.strip()[1:].isdigit() == False:
                    labels.get(line.strip()[1:])
                    if not labels.isInTable(line.strip()[1:]):
                        # print("YEs")
                        labels.add(line.strip()[1:],self.increment)
                        self.increment += 1
                    # labels.printTable()
                else:
                    continue
            else:
                continue
    
    # returns whether there are more lines in inputFile to be parsed
    def hasMoreLines(self):
        return self.currentLineNum < len(self.inputFileLines)

    # move to the next valid instruction in inputFile
    def advance(self, inputFileName, labels):
        # labels = symbolTable.Table()
        skippable_line = True
        while self.hasMoreLines() and skippable_line:
            self.currentInstruction = self.inputFileLines[self.currentLineNum].strip()
            # print("self.currentInstruction: ", self.currentInstruction)
            # self.currentLineNum += 1
            # print("self.currentLineNum: ", self.currentLineNum)

            # check for each skippable condition and either break to continue advancing or set skippable to false and stop advancing
            for skippable in self.skippables:
                if self.currentInstruction.startswith(skippable) or self.currentInstruction == "":
                    break
                elif self.currentInstruction.startswith("("):
                    labelEnd = self.currentInstruction.find(")")
                    labels.get(self.currentInstruction[1:labelEnd])
                    labels.add(self.currentInstruction[1:labelEnd],self.ACinstructionCounter+1)
                    # labels.printTable()

                    self.symbol = None
                    self.dest = None
                    self.comp = None
                    self.jump = None
                    break
            else:
                skippable_line = False

            # I either ran out of lines in my file or I found a good instruction
            if self.hasMoreLines():
                self.currentLineNum += 1
                # parse instruction

                # check for @
                if self.currentInstruction.startswith("@"):
                    # should check for bad symbol, but assuming a valid asm file
                    self.ACinstructionCounter += 1
                    self.symbol = self.currentInstruction[1:]
                    
                elif self.currentInstruction.startswith(('A', 'D', 'M', '0')):
                    # now parse either dest = comp or dest = comp;jump or D;jump or 0;JMP
                    self.ACinstructionCounter += 1
                    compEnd = self.currentInstruction.find(';')
                    self.symbol = None  # All C instruction have no symbol

                    for skip in self.skippables:
                        i = self.currentInstruction.find(skip)
                        x = self.currentInstruction.find(" ")
                        if x >= 0:
                            self.currentInstruction = self.currentInstruction[:x]
                        elif i >= 0:
                            self.currentInstruction = self.currentInstruction[:i]

                    # dest = 
                    # check for equal sign
                    if '=' in self.currentInstruction:
                        destEnd = self.currentInstruction.find('=')
                        self.dest = self.currentInstruction[0:destEnd]

                        if compEnd == -1:
                            self.comp = self.currentInstruction[destEnd + 1:]
                            self.jump = None
                        else:
                            self.comp = self.currentInstruction[destEnd + 1:compEnd]
                            self.jump = self.currentInstruction[compEnd+1:]
                    else:
                        # D;jump where jump is one of []
                        # 0;JMP
                        self.dest = None
                        self.comp = self.currentInstruction[:compEnd]
                        self.jump = self.currentInstruction[compEnd+1:]

            else:
                # ran out of lines, set default values
                self.currentInstruction = ""
                self.symbol = None
                self.dest = None
                self.comp = None
                self.jump = None
                exit()

    # return instruction type of the current instruction
    def instruction_type(self):
        # should update to include the L_INSTRUCTION
        if self.symbol != None:
            if self.symbol.isdigit() == True:
                return "A_INSTRUCTION"
            else:
                return "L_INSTRUCTION"
        # elif self.symbol == None and self.currentInstruction.startswith("("):
        #     return "L_INSTRUCTION"
        else:
            return "C_INSTRUCTION"

    # for A_INSTRUCTION and L_INSTRUCTION returns the symbol associated with the @-instruction
    def symbol(self):
        return self.symbol

    # returns the dest part of a C_INSTRUCTION
    def dest(self):
        return self.dest

    # returns the comp part of a C_INSTRUCTION
    def comp(self):
        return self.comp

    # returns the jump part of a C_INSTRUCTION
    def jump(self):
        return self.jump
    
    def currInst(self):
        return str(self.currentInstruction)

    def Asymbol(self, label):
        if self.symbol.isdigit() == True:
            return int(self.symbol)
        else:
            # print(self.symbol)
            # print(label.get(self.symbol))
            return label.get(self.symbol)