
channels = ["BBC", "Discovery", "TV1000"]
class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel = 0

    def first_channel(self):
        self.current_channel = 0
        return self.channels[self.current_channel]


    def last_channel(self):
        self.current_channel = -1
        return self.channels[self.current_channel]


    def turn_channel(self, x):
        self.current_channel = x
        return self.channels[self.current_channel]

    def next_channel(self):
        self.current_channel += 1
        return self.channels[self.current_channel % len(self.channels)]

    def previous_channel(self):
        self.current_channel -= 1
        return self.channels[self.current_channel % len(self.channels)]

    def is_exist(self, search):
        if isinstance(search, int) and search <= len(self.channels) and search >= 0:
            print("Yes")
        elif isinstance(search, str) and search in self.channels:
            print("Yes")
        else:
            print("No")




my_controller = TVController(channels)
# print(my_controller.first_channel())

#print(my_controller.last_channel())
#print(my_controller.turn_channel(2))
print(my_controller.next_channel())
#print(my_controller.previous_channel())
#print(my_controller.is_exist("BBC2"))
