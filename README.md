# CT-BASIC

A [Cyclic Tag](https://esolangs.org/wiki/Cyclic_tag_system) BASIC compiler.

Compiles a reduced dialect of BASIC into one of the following compilation targets:

* [CT](https://esolangs.org/wiki/Bitwise_Cyclic_Tag#The_language_CT) (Cyclic Tag)
* [BCT](https://esolangs.org/wiki/Bitwise_Cyclic_Tag) (Bitwise Cyclic Tag)
* [ABCT](https://github.com/hornc/abctag) (Arithmetic Bitwise Cyclic Tag)
* [Rule 110](https://en.wikipedia.org/wiki/Rule_110), using the ["blocks of bits" construction developed and described by Matthew Cook](https://doi.org/10.4204/eptcs.1.4)

Experimental / work in progress. Details and usabilty are still being worked out.

The idea is to capture something of the early days of programming while using low level cyclic tag systems
for 'useful' programs.


### Design Notes
Line numbers don't add anything for a cyclic tag implementation since everything is run inside an implicit loop. Line numbers are not required.

Indentation is optional, but helpful.

Using ZX Spectrum BASIC as a rough starting point, and adding from other BASICs (or BASIC likes) as required (e.g. `ELSE`, `ENDIF`, and `ASM`).

### Commands

See the [Command list](COMMANDS.md) for implemented and aspirational commands and syntax.


### Example usage

Compile Hello, World! example to cyclic tag:

    ./CTBASIC.py examples/HELLOWORLD.BAS

Use the included cyclic tag interpreter [ct.py](ct.py) to dispay output (input data = `1`):

    ./ct.py <(./CTBASIC.py examples/HELLOWORLD.BAS) 1
    Hello, World!

Compile to arithmetic cyclic tag:

    ./CTBASIC.py -tABCT examples/HELLOWORLD.BAS

Compile to rule 110 'blocks':

    ./CTBASIC.py -t110 examples/HELLOWORLD.BAS

