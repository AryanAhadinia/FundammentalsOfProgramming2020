room_length = float(input())
room_width = float(input())
tile_length = float(input())
tile_width = float(input())
c = (room_length * room_width) / (tile_length * tile_width)
if c == int(c):
    print(int(c))
else:
    print(int(c) + 1)
