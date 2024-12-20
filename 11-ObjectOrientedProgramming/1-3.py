class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        return f"The distance: {self.distance}, the rate per km is {self.rate_per_km}, and the final fare is {self.fare}"


def main():
    # your program
    taxi = TaxiRide(2)
    taxi.calculate_fare(50)
    print(taxi.print_receipt())

if __name__ == "__main__":
    main()