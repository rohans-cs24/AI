rooms = {"A":0,"B":1,"C":1,"D":0}
just_rooms = ["A","B","C","D"]

room = input("Enter initial room to place vacuum cleaner: ")

visited = 0;
rooms_count = len(just_rooms)
cur = just_rooms.index(room)

while visited < rooms_count:
    visited += 1
    if rooms[(just_rooms[cur])] == 0:
        rooms[(just_rooms[cur])] = 1
        print("Cleaning" , just_rooms[cur])
    cur = (cur+1)  % rooms_count
    if visited == rooms_count:
        break
    print("Moving to ", just_rooms[cur] )
print("All rooms cleaned")