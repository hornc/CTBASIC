# Commands

### REM
_0 frames_

Comments. Ignored by the compiler.

### PRINT "_str_"
_chars + 4 frames (chars + 3 frames if no newline)_

Write `STX` / `ETX` bounded string, with start=1 and end=0 bits (10 bits per frame) to data-string (output data convention).

### CHR$ _n_
_1 frame_

Convert number _n_ into its ASCII character (8bit). Useful for sending ASCII control characters using `PRINT`.

### DATA _bitstring|bool|int|str_
Write binary / boolean / integer / string to data-string.

### BIN _bitstring_
Write binary to data-string.

### ASM _code_
Include raw cyclic tag `{0, 1, ;}` in the compiled output.

### CLEAR _n_
Deletes _n_ bits from data-string. (Borrowed from ZX Spectrum BASIC).

### FILL _n_
Appends _n_ set bits (`1`) to data-string, if leftmost data-bit is set.

### ZFILL _n_
Appends _n_ unset bits (`0`) to data-string, if leftmost data-bit is set.

### INPUT _v_
_UNIMPLEMENTED_
Assign the next bit of input data to variable _v_. Can only be used one at the beginning of the program. Special variable `_` can be used to consume the first input bit which always has to be one to allow a CT program to get started. (Borrowed from the Python convention).

### END
An alias for `CLEAR 10`, which clears the data-string frame by frame, which if _all_ data is correctly aligned on `0` stop-bits, can allow the program to cycle as many times as needed to clear the entire data-string without triggering any further output or effects.

## Graphics
_3 frames + graphics command frame total_

CT-BASIC can produce Tektronix 401x graphical output using the following ZX Spectrum borrowed commands:

### CLS
_8 frames_

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
