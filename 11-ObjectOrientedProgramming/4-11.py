class Stadium:
    def __init__(self, stadium_dict):
        self.sector_data = stadium_dict 

    def change_number_of_fans(self, sector, number_of_fans):
        self.sector_data[sector] = number_of_fans

    def display_values(self):
        for key, value in self.sector_data.items():
            print(f"{key}: {value}", end="; ")
        
        print()

    def sum_of_fans(self, sector_str):
        result = 0
        for char in sector_str:
            if char in self.sector_data:
                result += self.sector_data[char]
        return result    


# n = number of fans
# s = sector

def main():
    stadium = Stadium({"A":120,"D":150,"G":90,"K":110})
    stadium.display_values()
    stadium.change_number_of_fans("B", 500)
    stadium.display_values()
    stadium.change_number_of_fans("A", 150)
    stadium.display_values()
    res = stadium.sum_of_fans("KEJ")
    print(f"Sum of fans: {res}")





if __name__ == "__main__":
    main()