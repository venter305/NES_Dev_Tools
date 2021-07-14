#! /usr/bin/python3

import sys

ipsFilePath = sys.argv[1]
romFilePath = sys.argv[2]
outFilePath = sys.argv[3]

with open(ipsFilePath,"rb") as ipsFile:
    rawIps = ipsFile.read()
with open(romFilePath,"rb") as romFile:
    rawRom = romFile.read()

rawIps = rawIps[:-3]
rawRom = bytearray(rawRom)

index = 5
while index < len(rawIps):
    offset = rawIps[index]*0x10000+rawIps[index+1]*0x100+rawIps[index+2]
    index += 3
    size = rawIps[index]*0x100+rawIps[index+1]
    index += 2
    if size == 0:
        rleSize = rawIps[index]*0x100+rawIps[index+1]
        size = rleSize
        index += 2
        data = [rawIps[index]]*rleSize
        data = bytearray(data)
        index += 1
    else:
        data = rawIps[index:index+size]
        index += size

    rawRom[offset:offset+size] = data

with open(outFilePath,"wb") as outFile:
    outFile.write(rawRom)
