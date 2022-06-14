# CT-BASIC

A [Cyclic Tag](https://esolangs.org/wiki/Cyclic_tag_system) BASIC compiler.

Compiles a reduced dialect of BASIC into [CT](https://esolangs.org/wiki/Bitwise_Cyclic_Tag#The_language_CT), [BCT](https://esolangs.org/wiki/Bitwise_Cyclic_Tag), or [ABCT](https://github.com/hornc/abctag).

Experimental / work in progress. Details and usabilty are still being worked out.

The idea is to capture something of the early days of programming while using low level cyclic tag systems
for 'useful' programs.


### Design Notes
Line numbers don't add anything for a cyclic tag implementation since everything is run inside an implicit loop. Line numbers are not required.

Indentation is optional, but helpful.

Using ZX Spectrum BASIC as a rough starting point, and adding from other BASICs (or BASIC likes) as required (e.g. `ELSE`, `ENDIF`, and `ASM`).

### Commands

See the [Command list](COMMANDS.md) for implemented and aspirational commands and syntax.

