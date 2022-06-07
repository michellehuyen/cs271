class Assemble:
    def __init__(self):
        self.comp = {
                    '0': '0101010',
                    '1': '0111111',
                    '-1': '1111010',
                    'D': '1001100',
                    'A': '0110000',
                    '!D': '0001101',
                    '!A': '0110001',
                    '-D': '0001111',
                    '-A': '0110011',
                    'D+1': '0011111',
                    'A+1': '0110111',
                    'D-1': '0001110',
                    'A-1': '0110010',
                    'D+A': '0000010',
                    'D-A': '0010011',
                    'A-D': '0000111',
                    'D&A': '0000000',
                    'D|A': '0010101',
                    'M': '1110000',
                    '!M': '1110001',
                    '-M': '1110011',
                    'M+1': '1110111',
                    'M-1': '1110010',
                    'D+M': '1000010',
                    'D-M': '1010011',
                    'M-D': '1000111',
                    'D&M': '1000000',
                    'D|M': '1010101',
                    }
        
        self.dest = {
                    'null': '000',
                    'M': '001',
                    'D': '010',
                    'DM': '011',
                    'A': '100',
                    'AM': '101',
                    'AD': '110',
                    'ADM': '111'
                    }
        
        self.jump = {
                    'null': '000',
                    'JGT': '001',
                    'JEQ': '010',
                    'JGE': '011',
                    'JLT': '100',
                    'JNE': '101',
                    'JLE': '110',
                    'JMP': '111'
                    }

    # def findComp(self):
    def findComp(self, cmp):
        if cmp in self.comp:
            return self.comp.get(cmp)
            # return "cmp: " + cmp + " val: " + self.comp.get(cmp)

    def findDest(self, d):
        if d in self.dest:
            return self.dest.get(d)
        else:
            return self.dest.get('null')

    def findJump(self, jmp):
        if jmp in self.jump:
            return self.jump.get(jmp)
        else:
            return self.jump.get('null')