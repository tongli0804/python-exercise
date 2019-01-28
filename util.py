
import os,sys
class Util():
    file = 'C:\\Users\\weishao\Desktop\\test_input.txt'
    def lines(file):
        for line in file: yield line
        yield '\n'

    def blocks(file):
        block = []
        for line in Util.lines(file):
            if line.strip():
                block.append(line)
            elif block:
                yield ''.join(block).strip()
                block = []

