env = {
    'A': 'Clean',
    'B': 'Clean'
}
mem = {
    'A': 'Unknown',
    'B': 'Unknown'
}

initial = "A"

print(f"Agent starts in Room {initial}\n")
rooms = ['A', 'B']
for room in rooms:
    print()
    current = room
    print(f"--- Now in Room {current} ---")
    state = env[current]
    print(f"Perceived: Room {current} is {state}")
    mem[current] = state
    print(f"Memory updated: {mem}")
    if state == 'Dirty':
        print(f"Action: Clean Room {current}")
        env[current] = 'Clean'  
        mem[current] = 'Clean'   
    else:
        print(f"Action: Room {current} is already Clean. Move.")

print()

print("Final Check from Memory:")
print(f"Memory: {mem}")

if all(state == 'Clean' for state in env.values()):
    print("\nTask Complete: All rooms are Clean!")
else:
    print("\nTask Incomplete: Some rooms are still Dirty.")

