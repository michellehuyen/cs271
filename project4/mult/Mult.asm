// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

@R2
M = 0 // Memory[2] = 0 setting the value of RAM[2] to 0

@R0 //load address of R0 into A-register
D = M // D = Memory[0] (getting the value of RAM[0] and putting into D)
@EXIT
D;JEQ // if D = 0 goto EXIT

@R1 //load address of R1 into A-register
D = M // D = Memory[1] (getting the value of RAM[1] and putting into D)
@EXIT
D;JEQ // if D = 0 goto EXIT

@R0
D = M // D = Memory[0] (getting the value of RAM[0] and putting into D)
@R3
M = D // Memory[3] = D (getting the value of D and putting it in RAM[3])

// loop through until R3 is 0
(LOOP)
@R1
D = M // D = Memory[1] (getting the value of RAM[1] and putting into D)

@R2
M = D + M // Memory[2] = Memmory[1] + Memory[2]

@R3
M = M - 1 // Memory[3] = Memory[3] - 1 (getting the value at RAM[3] and subtracting by 1 to decrement the loop)
D = M

@LOOP
D;JGT // if D > 0 keep looping

(EXIT)
@EXIT
0;JMP