def expandsix(ct):
    """
    Expand CT appendants / productions to be a multiple of 6.
    Using technique described in Cook 2009, 1.0.
    """
    # TODO: short cut -- if the CT is simple and isn't meant to loop (ends with an END of many CLEARs)
    # pad the many ';' to a multiple of 6.
    exp = ''
    for c in ct:
        if c == ';':
            exp += ';' * 6
        elif c in '01':
            exp += c + '0' * 5
    return exp


def rule110(ct, data='1'):
    """
    Compile to Rule 110 'blocks' following the algorithm in 1.4 of:
      Cook, Matthew (2009). "A Concrete View of Rule 110 Computation". In Neary, T.; Woods, D.; Seda, A. K.; Murphy, N. (eds.).
      Electronic Proceedings in Theoretical Computer Science. Vol. 1. pp. 31–55.
      doi: 10.4204/EPTCS.1.4 (https://doi.org/10.4204/EPTCS.1.4)
    """
    appendants = ct.split(';')[:-1]
    count = len(appendants)
    if (count % 6) != 0:
        return rule110(expandsix(ct), data)

    central = 'C' + data.replace('0', 'ED').replace('1', 'FD')
    central = central[:-1] + 'G'
    right = ''
    empty = 0
    for a in appendants:
        if not a:
            empty += 1
            right += 'L'
            continue
        d = a.replace('0', 'IJ').replace('1', 'II')
        d = 'KH' + d[1:]
        right += d
    right = right[1:] + right[0]
    v = (76 * ct.count('1') +
         + 80 * ct.count('1')
         + 60 * (count - empty)
         + 43 * empty)
    left = 'A' * v + 'B' + 'A' * 13 + 'B' + 'A' * 11 + 'B' + 'A' * 12 + 'B'
    return left, central, right
