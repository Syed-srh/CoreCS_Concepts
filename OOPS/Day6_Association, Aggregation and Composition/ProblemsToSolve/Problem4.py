#Compostion Problem
class Room:
    def __init__(self, room_type):
        self.room_type = room_type
    def display_room(self):
        print(f"Room Type: {self.room_type}")

class House:
    def __init__(self, rooms):
        self.rooms = rooms
    def show_rooms(self):
        print("House has the following rooms:")
        for room in self.rooms:
            room.display_room()

#     Additional Requirements
# Create Room objects only inside House
# Do not create Room objects externally
# Demonstrate that rooms are tightly coupled with house