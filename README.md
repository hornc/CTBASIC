# CT-BASIC

CTBASIC is a compiled [Sinclair BASIC](https://en.wikipedia.org/wiki/Sinclair_BASIC) insipred language targeting a "fantasy console" architecture using the [cyclic tag system](https://esolangs.org/wiki/Cyclic_tag_system) computational model.

It compiles a reduced dialect of BASIC into one of the following compilation targets:

* [CT](https://esolangs.org/wiki/Bitwise_Cyclic_Tag#The_language_CT) (Cyclic Tag)
* [BCT](https://esolangs.org/wiki/Bitwise_Cyclic_Tag) (Bitwise Cyclic Tag)
* [ABCT](https://github.com/hornc/abctag) (Arithmetic Bitwise Cyclic Tag)
* [Rule 110](https://en.wikipedia.org/wiki/Rule_110), using the ["blocks of bits" construction developed and described by Matthew Cook](https://doi.org/10.4204/eptcs.1.4)

This is an experimental project / work in progress. Details and usabilty are being worked out as features are added.

The idea is to capture something of the early days of programming while using low level cyclic tag systems for 'useful' programs.


### The Fantasy Console

CTBASIC compiles to standard versions of the above cyclic-tag families, so any compiled program _will_ run on all of them.
However, in order to provide some user feedback, the CTBASIC architecture assumes a particular set of output conventions, which distiguish a CTBASIC 'machine' from a plain cyclic-tag interpreter.

These differences _only_ apply to I/O, where the output conventions are side-effects (not affecting the underlying computation, and the input conventions only affect starting (and re-starting) states, so also don't affect the fundamental computational process.

The CTBASIC machine I/O conventions are as follows:

1) Byte strings can be encoded and recognised within the datastring:
   * 8 bit bytes are encoded within a 10 bit dataframe with a start-bit `1` and end-bit `0`.
   * A string is a series of 10-bit frames begining with the ASCII `STX` character (0x02), and terminated by the `ETX` character (0x03).
   * When a valid string is completed, (i.e. the stop-bit `0` of the `ETX` is appended to the right of the datastring) the complete string is sent to output.

2) Output is a serial byte-stream, with flexible destinations.
   * The CTBASIC language has drawing commands which when compiled produce serial byte output that can be recongised by Tektronix 4010/4 compatible terminals.
   * Non-graphical serial terminals are also intended to be supported for character output.
   * Other byte-based output targets are also a possibility (e.g. audio, serial input to other devices).

3) Interactive mode:
   * An optional execution mode whereby when the datastring becomes empty (the standard **halt** condition) the user is prompted for more input to replenish the datastring. Previous program output could perhaps give the user some guidance on how to binary-encode an appropriate input response.
   * If a new datastring input is provided, the program resumes with the next cyclic production.
   * If no new input is provided, the program halts.


### General cyclic-tag input considerations

A standard feature of Cyclic Tag family of languages is that they require a non-empty, non-zero, data string to begin execution.

If the initial data string is empty, or does not contain _any_ `1` symbols, a program _cannot possibly_ modify the data string, so no computation will occur.

This means that for any CT family program to perform a computation, an appropriate input data string MUST be provided.
At minimum, this input data string can be a single `1`. From this, a program can bootstrap any required data structure to allow it to accomplish its computation.

Specifc user supplied variable input will need to be encoded in some fashion into the initial data string, the instructions for which will depend on the specific program being run.
In general, there will need to be at least one `1` symbol for the program to have a chance of regognising the full range of user supplied inputs, including 'blank' input.
Providing an input datastring begining with a `0` symbol will in general prevent a program from functioning correctly (unless the expected behaviour is "do nothing").


### Cyclic Tag Interpreter

CTBASIC comes with a simple [Cyclic Tag interpreter](ct.py) to test CTBASIC programs behave as intended when compiled to the default Cyclic Tag dialect. It supports the input and output conventions, and will execute CTBASIC examples as intended (assuming correct mode flags and terminals are used).


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

