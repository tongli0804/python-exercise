
if __name__ == "__main__":
    with open('E:\Test_Framework\Initialization\Tuser_name.txt') as f:
        while True:
            line = f.readline()
            if not line: break
            print(line)