# CT-BASIC

CTBASIC is a compiled [Sinclair BASIC](https://en.wikipedia.org/wiki/Sinclair_BASIC) insipred language targeting a "fantasy console" architecture using the [cyclic tag system](https://esolangs.org/wiki/Cyclic_tag_system) computational model.

It compiles a reduced dialect of BASIC into one of the following compilation targets:

* [CT](https://esolangs.org/wiki/Bitwise_Cyclic_Tag#The_language_CT) (Cyclic Tag)
* [BCT](https://esolangs.org/wiki/Bitwise_Cyclic_Tag) (Bitwise Cyclic Tag)
* [ABCT](https://github.com/hornc/abctag) (Arithmetic Bitwise Cyclic Tag)
* [Rule 110](https://en.wikipedia.org/wiki/Rule_110), using the ["blocks of bits" construction developed and described by Matthew Cook](https://doi.org/10.4204/eptcs.1.4)

This is an experimental project / work in progress. Details and usabilty are being worked out as features are added.

The idea is to capture something of the early days of programming while using low level cyclic tag systems for 'useful' programs.

### Cyclic Tag Interpreter

CTBASIC comes with a simple [Cyclic Tag interpreter](ct.py) to test CTBASIC programs behave as intended when compiled to the default Cyclic Tag dialect.

### Commands

See the [Command list](COMMANDS.md) for implemented and aspirational commands and syntax.


### Example usage

Compile Hello, World! example to cyclic tag:

    ./CTBASIC.py examples/HELLOWORLD.BAS

Use the included cyclic tag interpreter [ct.py](ct.py) to dispay output (input data = `1`):

    ./ct.py <(./CTBASIC.py examples/HELLOWORLD.BAS) 1

**output:** `Hello, World!`

Compile to arithmetic cyclic tag:

    ./CTBASIC.py -tABCT examples/HELLOWORLD.BAS

Compile to rule 110 'blocks':

    ./CTBASIC.py -t110 examples/HELLOWORLD.BAS

