import os
import time
import sys

try:
    conv = open(str(sys.argv[1]), 'r')
except:
    raise Exception("File doesn't exist or no file argument.")

convert = 0

for line in conv:
    convert += 1
    if line[0] == "#":
        pass
    elif line == "HELLOWORLD":
        print("Hello world!")
    elif line == "HELLOWORLD\n":
        print("Hello world!")
    elif line == "PAUSE":
        time.sleep(3)
    elif line == "PAUSE\n":
        time.sleep(3)
    elif 'PRINT ' in line:
        syn = line.replace('PRINT ', '')
        print(syn)
    elif 'PAUSE ' in line:
        syn = line.replace('PAUSE ', '')
        time.sleep(int(syn))
    elif 'TERMINAL ' in line:
        syn = line.replace('TERMINAL ', '')
        os.system(syn)
    elif line == "END":
        exit()
    elif line == "END\n":
        exit()
    else:
        raise SyntaxError("An unknown SyntaxError occurred, try looking at your code.")
            
            
        