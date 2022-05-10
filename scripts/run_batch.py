#!/usr/bin/env python
import os


# create multiple job scripts
for x in range(15,24):
    with open("scripts/myjob.script", "r") as inf:
        with open("scripts/test.script_" + str(x), "w") as ouf:
            data = inf.readlines()
            for line in data:
                ouf.write(line)
            ouf.write('srun -n 32 ../src/graph500_reference_bfs ' + str(x))
   # os.system("sbatch test.script_" + str(x))
