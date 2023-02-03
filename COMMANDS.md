# Commands

### REM
_0 frames_

Comments. Ignored by the compiler.

### PRINT "_s_"
_chars + 3 frames_

Write STX / ETX bounded string, with start=1 and end=0 bits (10 bits per frame) to DATA (output data convention).

### CHR$ _n_
_1 frame_

Convert number _n_ into its ASCII character (8bit). Useful for sending ASCII control characters using `PRINT`.

### DATA
Write binary / boolean / integer / string to DATA.

### BIN
Write binary to DATA.

### ASM
Include raw cyclic tag `{0, 1, ;}` in the compiled output.

### CLEAR _n_
Deletes _n_ bits from datastring DATA. (Borrowed from ZX Spectrum BASIC).

### FILL _n_
Appends _n_ set bits (`1`) to datastring DATA, if leftmost databit is set.

### ZFILL _n_
Appends _n_ unset bits (`0`) to datastring DATA, if leftmost databit is set.

### INPUT _v_
Assign the next bit of input data to variable _v_. Can only be used one at the beginning of the program. Special variable `_` can be used to consume the first input bit which always has to be one to allow a CT program to get started. (Borrowed from the Python convention).

### END
Completely consume datastring DATA to trigger the cyclic tag system halt condition.

## Graphics

CT-BASIC can produce Tektronix 401x graphical output using the following ZX Spectrum borrowed commands:

### CLS
_6 frames_

Clear screen. Writes Tektronix 401x control sequence `ESC` + `FF`.

### DRAW _Δx_, _Δy_
_4 frames_

Draws a line from the last pixel of the previous `PLOT` or `DRAW` using relative offsets.

### INK _n_
_2 frames_

Sets the ink (foreground) colour of the line drawing pen.

0. Normal (solid)
1. Dotted
2. Dot-dashed
3. Short-dash
4. Long-dash
5. Defocused, normal
6. Defocused, dotted
7. Defocused, dot-dashed

### PLOT _x_, _y_
_9 frames_

Plots a point at absolute coordinate _x_, _y_.
* _x_ range: 0–1023.
* _y_ range: 0–779.

`0, 0` represents the bottom-left corner of the screen.
