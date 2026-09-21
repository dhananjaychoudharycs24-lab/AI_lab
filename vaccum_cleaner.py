def reflex_agent(location, status):
    if status.lower() == 'dirty':
        return 'Suck'
    elif location.upper() == 'A':
        return 'Right'
    elif location.upper() == 'B':
        return 'Left'
    

def run_vacuum_simulation():
    
    room_states = {
        'A': input("Enter status for Room A (Clean/Dirty): "),
        'B': input("Enter status for Room B (Clean/Dirty): ")
    }
    current_location = input("Enter initial vacuum location (A or B): ").upper()
    
    print("\n--- Starting Simulation ---")
    for step in range(1, 3):
        current_status = room_states[current_location]
        print(f"\nStep {step}:")
        print(f"Vacuum is in Room {current_location}. Room is {current_status}.")
        
        action = reflex_agent(current_location, current_status)
        
        if action == 'Suck':
            print(f"Action: Clean (Suck dirt in Room {current_location})")
            room_states[current_location] = 'Clean'
        elif action == 'Right':
            print("Action: Move Right to Room B")
            current_location = 'B'
        elif action == 'Left':
            print("Action: Move Left to Room A")
            current_location = 'A'
            
    print("\n--- Simulation Finished ---")
    print("Final Room Statuses:")
    print(f"Room A: {room_states['A']}")
    print(f"Room B: {room_states['B']}")
if __name__ == "__main__":
    run_vacuum_simulation()

