#!/usr/bin/env python

import sys

try:
    log = sys.argv[1]
except:
    log = 0
finally:

    out = sys.stdout
    err = sys.stderr
    fa = sys.stdin

    for line in fa:
        if "@" in line:
            curr = str(line)
        else:
            wline = line.rstrip().upper()
            G = wline.count('G')
            C = wline.count('C')
            GC = (G+C)/len(wline)

            if GC < 0.50 and GC > 0.45:
                out.write(curr+line)
                if log:
                    err.write("Done! Sequence has processed.\n")
            else:
                if log:
                    err.write('Warrning! GC-COMPOSITION DOES NOT BELONG TO THE RANGE.\n')

