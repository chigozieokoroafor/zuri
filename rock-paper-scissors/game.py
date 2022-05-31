from main import cpu, check



user_count = 0
cpu_count = 0
count = 0

while count <3:
    cpu_choice = cpu()
    choice = input("your choice: ").upper()
    if choice.upper() == cpu_choice.upper():
        print(cpu_choice)
        print(f"it's a Tie, scores: player-{user_count}, cpu-{cpu_count}")
    elif choice == "P" and cpu_choice=="R":
        user_count = user_count+1
        print(cpu_choice)
        print(f"scores: player-{user_count}, cpu-{cpu_count}")
    elif choice == "S" and cpu_choice == "P":
        user_count = user_count+1
        print(cpu_choice)
        print(f"scores: player-{user_count}, cpu-{cpu_count}")
    elif choice == "R" and cpu_choice == "S":
        user_count = user_count+1
        print(cpu_choice)
        print(f"scores: player-{user_count}, cpu-{cpu_count}")
    elif choice == "P" and cpu_choice=="S":
        cpu_count = cpu_count+1
        print(cpu_choice)
        print(f"scores: player-{user_count}, cpu-{cpu_count}")
    elif choice == "R" and cpu_choice == "P":
        cpu_count = cpu_count+1
        print(cpu_choice)
        print(f"scores: player-{user_count}, cpu-{cpu_count}")
    elif choice == "S" and cpu_choice == "R":
        cpu_count = cpu_count+1
        print(cpu_choice)
        print(f"scores: player-{user_count}, cpu-{cpu_count}")
    count = count+1
    