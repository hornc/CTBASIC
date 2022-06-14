# Commands

### REM
Comments. Ignored by the compiler.

### PRINT "_s_"
Write (and then remove) STX / ETX bounded string, with start=1 and end=0 bits (10 bits per frame) to DATA (output data convention).

### DATA
Write binary / boolean / integer / string to DATA.

### BIN
Write binary to DATA.

### ASM
Include raw cyclic tag `{0, 1, ;}` in the compiled output.

### CLEAR _n_
Deletes _n_ bits from datastring DATA. (Borrowed from ZX Spectrum BASIC).


### INPUT _v_
Assign the next bit of input data to variable _v_. Can only be used one at the beginning of the program. Special variable `_` can be used to consume the first input bit which always has to be one to allow a CT program to get started. (Borrowed from the Python convention).

### END
Completely consume datastring DATA to trigger the cyclic tag system halt condition.
