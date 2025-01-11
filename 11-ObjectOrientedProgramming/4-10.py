class Coordinates:
    def __init__(self, array):
        self.array = array

    def m(self, n):
        counter = 0
        for value in self.array:
            if value[0] > 0 and value[1] > 0:
                counter += 1
        return counter >= n

def main():
    coordinates = Coordinates([[2,3],[1,8],[-6,4],[3,-7]])

    print(coordinates.m(2))


if __name__ == "__main__":
    main()

