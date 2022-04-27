// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(KEYBOARD_CHECK)
@KBD // 24576
D = M // D = M[24576] D = value at RAM[24576]
@WHITE
D;JEQ // if D = 0 then jump to WHITE else continue to BLACK

@BLACK
0;JMP 

(WHITE)
@SCREEN // 16384
D = A // D = 16384

@0
M = D // M[0] = 16384

(WHITE_LOOP)
@0
D = M // D = M[0] -> D = 16384

A = D // A = 16384
M = 0

D = D + 1 // D = 16385

@0
M = D // M[0] = 16385

@24576
D = D - A // D = 18191

@KEYBOARD_CHECK
D;JEQ // if D = 0 jump to KEYBOARD_CHECK

@WHITE_LOOP
0;JMP



(BLACK)
@SCREEN
D = A

@0
M = D

(BLACK_LOOP)
@0
D = M

A = D
M = -1

D = D + 1

@0
M = D

@24576
D = D - A 

@KEYBOARD_CHECK
D;JEQ

@BLACK_LOOP
0;JMP



(EXIT)
@EXIT
0;JMP