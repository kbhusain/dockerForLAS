# a simple docker setup for processing LAS files

Run the program with the "python" container. 
The command "docker pull python" gets you the container. 

The command below with run the command: 
docker run -it -v`pwd`:/work/ python work/t.bash sample.las 

The bash file is shown as follows:

#!/bin/bash
cd /work
python lasLogger.py $1

The LAS format is relatively easy to decipher. I am only collecting 
two fields in this example; the real world example actually examined 
the incoming data before formatting and loading it into a database. 
Had there been any errors, the log file would list the next course of
action for the user. 

The idea behind using docker instead of a batch file was to divide the 
processing across several processes intead of a long monolithic batch
file. For this demo, it looks like an overkill but as the size or 
complexity of the input files grows, you can see how segregating the 
code into small, executable containers begins to make sense. 


