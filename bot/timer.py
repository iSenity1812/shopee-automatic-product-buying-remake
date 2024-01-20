import datetime
import time

def format_time_delta(delta):
    minutes, seconds = divmod(delta.seconds, 60)
    return f"{minutes:02d}:{seconds:02d}"

def get_countdown_duration():
    print("Choose countdown duration:")
    print("1. 1min\n2. 1min 30sec\n3. 3min\n4. 5min\n5. 10min\n6. 30min\n7. 1h\n8. Custom")

    choice = int(input("Enter your choice (1-8): "))
    
    if choice == 8:
        # Custom countdown
        custom_duration = int(input("Enter custom duration in minutes: "))
        return custom_duration * 60
    elif choice in [1, 2, 3, 4, 5, 6, 7]:
        # Predefined durations
        durations = [60, 90, 180, 300, 600, 1800, 3600]
        return durations[choice - 1]
    else:
        print("Invalid choice.")
        return None

def execute_countdown(countdown_seconds):
    current_time = datetime.datetime.now()
    target_time = current_time + datetime.timedelta(seconds=countdown_seconds)

    print(f"Countdown started. Target time: {target_time.strftime('%Y-%m-%d %H:%M:%S')}")

    while datetime.datetime.now() < target_time:
        remaining_time = target_time - datetime.datetime.now()
        print(f"Time remaining: {format_time_delta(remaining_time)}", end='\r')
        time.sleep(1)

    print("\nCountdown finished!")

# def set_countdown():
#     countdown_seconds = get_countdown_duration()

#     if countdown_seconds is not None:
#         execute_countdown(countdown_seconds)

# # Example usage
# set_countdown()
