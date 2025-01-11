class TV:
    def __init__(self, channel_number, volume):
        self.is_on = False
        self.channel_number = channel_number
        self.volume = volume
        self.channels_list = []


    def turn_on(self):
        self.is_on = True


    def turn_off(self):
        self.is_on = False

    
    def set_channel(self):
        self.channel_number = int(input("Switch the channel (1-10): "))
        print(f"Your channel is now set to: {self.channel_number}")


    def set_channels(self, channels_list):
        self.channels_list = channels_list
        while True:
            input_of_channels = input("What channel do you want to add?: ")
            channels_list.append(input_of_channels)
            indicator = int(input("Do you want to continue adding channels? 0 for no, 1 for yes: "))
            if indicator == 0:
                break

    
    def show_channels(self):
        for number, index in enumerate(self.channels_list, 1):
            print(number, index)

    
    def volume_up(self):
        self.volume += 1
        if self.volume > 10:
            self.volume -= 1
            print("The volume cannot be above 10")


    def volume_down(self):
        self.volume -= 1
        if self.volume < 0:
            self.volume +=1
            print("The volume cannnot be below 0")


    def show_status(self):
        if self.is_on:
            if self.channels_list == []:
                print(f"The tv is on, there are no channels yet, current volume is {self.volume}")
            else:
                print(f"The tv is on, channel {self.channel_number} ({self.channels_list[self.channel_number - 1]}), current volume is {self.volume}")
        else:
            print("The tv is off")