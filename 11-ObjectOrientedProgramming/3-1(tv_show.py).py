# tv_show.py file
# main program
from tv import TV


def main():
   # object creation
   my_tv = TV(1, 0)

   # object usage
   my_tv.show_status()

   my_tv.turn_on()

   my_tv.show_status()

   #my_tv.channels_list = []
   print(my_tv.channels_list)

   my_tv.volume_up()

   my_tv.show_status()

   my_tv.volume_down()

   my_tv.show_status()

   my_tv.set_channels(my_tv.channels_list)

   my_tv.show_channels()

   my_tv.show_status()

   my_tv.turn_off()

   my_tv.show_status()

if __name__ == "__main__":
   main()