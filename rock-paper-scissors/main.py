import random

def cpu():
    ls = ["R", "P", "S"]
    cpu_coice = random.choice(ls)
    return cpu_coice
    
def check(choice, cpu_choice, user_count, cpu_count):
    if choice.upper() == cpu_choice.upper():
        return(f"it's a Tie, scores: player-{user_count}, cpu-{cpu_count}")
    elif choice == "P" and cpu_choice=="R":
        user_count = user_count+1
        return(f"scores: player-{user_count}, cpu-{cpu_count}")
    elif choice == "S" and cpu_choice == "P":
        user_count = user_count+1
        return(f"scores: player-{user_count}, cpu-{cpu_count}")
    elif choice == "R" and cpu_choice == "S":
        user_count = user_count+1
        return(f"scores: player-{user_count}, cpu-{cpu_count}")
    elif choice == "P" and cpu_choice=="S":
        cpu_count = cpu_count+1
        return(f"scores: player-{user_count}, cpu-{cpu_count}")
    elif choice == "R" and cpu_choice == "P":
        cpu_count = cpu_count+1
        return(f"scores: player-{user_count}, cpu-{cpu_count}")
    elif choice == "S" and cpu_choice == "R":
        cpu_count = cpu_count+1
        return(f"scores: player-{user_count}, cpu-{cpu_count}")