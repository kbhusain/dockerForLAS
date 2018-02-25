#  A very simple LAS file logger
import os, sys
fname = sys.argv[1];
print("Filename" + fname); 
xln = open(fname).readlines();
logs = []
for x in xln: 
	xl = x.upper().strip();
	if xl.find("NAME") == 0: logs.append(xl)
	if xl.find("DATE") == 0: logs.append(xl)
with open(os.path.splitext(fname)[0] + ".log","w") as fd: 
	fd.write("\n".join(logs))
	fd.write("\n")

