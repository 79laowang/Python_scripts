from mmap import mmap

def get_lines(fp):
    with open(fp,"r+") as f:
        m = mmap(f.fileno(), 0)
        tmp = 0
        for i, char in enumerate(m):
            if char==b"\n":
                #  yield m[tmp:i+1].decode()
                yield m[tmp:i+1]
                tmp = i+1
def main():
    for i in get_lines("/var/log/messages-20190922"):
        print(i)

if __name__ == '__main__':
    main()
