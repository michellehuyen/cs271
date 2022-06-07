import parser
import symbolTable
import assemble
import sys

def main():
    # python main.py ../project6/max/Max.asm
    if len(sys.argv) > 1:
        fileName = ''.join(sys.argv[1])
        table = symbolTable.Table()
        myParser = parser.Parser(fileName, table)

        while myParser.hasMoreLines():
            myParser.advance(fileName, table)
            if myParser.instruction_type() == "A_INSTRUCTION":
                aInstruction(myParser, table)
            elif myParser.instruction_type() == "L_INSTRUCTION":
                LInstruction(myParser, table)
            else:
                cInstruction(myParser)


def aInstruction(parse, t):
    print("\nInstruction: " + parse.currInst())
    print("Binary #: " + format(parse.Asymbol(t), '016b'))

def LInstruction(parse, t):
    print("\nInstruction: " + parse.currInst())
    print("Binary #: " + format(parse.Asymbol(t), '016b'))

def cInstruction(parse):
    asm = assemble.Assemble()

    cmp = str(asm.findComp(parse.comp))
    dest = str(asm.findDest(parse.dest))
    jmp = str(asm.findJump(parse.jump))

    print("\nInstruction: " + parse.currInst())

    print("Dest: " + dest)
    print("Comp: " + cmp)
    print("Jump: " + jmp)

    binary_num = '111' + cmp + dest + jmp
    print("Binary #: " + binary_num)

# if __name__ == "__main__":
main()