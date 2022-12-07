def main():
    commands = []

    with open("./input.txt") as f:
        for row in f.readlines():
            if row[0] == "$":
                print(row.rstrip()) 
    print(commands)

if __name__=="__main__":
    main()

