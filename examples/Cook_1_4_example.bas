REM Appendant example given in section 1.4 of
REM M. Cook (2009) "A Concrete View of Rule 110 Computation"
REM doi: 10.4204/EPTCS.1.4
REM p. 37
REM Original cyclic appendant list: {YN, NYYN, 0, 0}

ASM 10;
ASM 0110;
ASM ;
ASM ;

REM Modified slightly to give the required multiple of 6 appendants:
REM i.e.: {YN, NYYN, 0, 0, 0, 0}
ASM ;
ASM ;

REM Expected RHS: HIIJKHJIIIIIJLLLLK
