import os

bloomFilter = None


def lookFor(username):
    if (bloomFilter.revisar(username)):
        cmd = f"grep '{username}' L.txt"
        a = os.system(cmd)


def setBloomFilter(filtro):
    global bloomFilter
    bloomFilter = filtro
