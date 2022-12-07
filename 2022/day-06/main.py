def main():
    def uniqueList(list, amount):
        """
        Find out if a list have amount of unique items
        """
        seen = set()
        unique = []
        for elem in list:
            if elem not in seen:
                unique.append(elem)
                seen.add(elem)
        if (len(unique) == amount):
            return True
    def findMarker(string, amount):
        """
        Returns the id where amount of characters is unique in row
        """
        for i in range(amount, len(string)):
            markers = []
            for j in reversed(range(0,amount)):
                markers.append(string[i-j])
            if (uniqueList(markers, amount)):
                return i+1
        return "No marker found"

    input = open("./input.txt").read()

    print(f"Answer Part 1: {findMarker(input, 4)}")
    print(f"Answer Part 2: {findMarker(input, 14)}")
    

if __name__=="__main__":
    main()