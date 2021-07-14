#! /bin/python3

import sys

inFilePath = sys.argv[1]
outFilePath = sys.argv[2]

with open(inFilePath,"rb") as inFile:
    rawData = inFile.read()

patternTable = [0]*(256*16)

for i in range(256):
    for y in range(8):
        byte = 0
        for x in range(8):
            dataIndX = (i%16)*8+x
            dataIndY = int((i/16))*8+y
            byte += int(rawData[dataIndY*128+dataIndX]/255)<<(7-x)
        patternTable[i*16+y] = byte
        patternTable[i*16+y+8] = byte

with open(outFilePath,"wb") as outFile:
    for byte in patternTable:
        outFile.write(byte.to_bytes(1,"little"))
