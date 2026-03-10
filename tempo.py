import time

def initial_input():
    global error
    global hours
    global minutes
    global seconds
    error = 0
    hours = int(input("\nHow much hours?: "))
    minutes = int(input("\nHow much minutes?: "))
    seconds = int(input("\nHow much seconds?: "))
    try:
        hours, minutes, seconds = int(hours), int(minutes), int(seconds)
    except:
        print("Error in input")
        error = 1
        initial_input()
    if hours > 99 or minutes > 60 or seconds > 60:
        print("\nERROR!!! Please input correct numbers")
        initial_input()
        error = 1
error = 0
initial_input()
if error == 0:
    max_range = hours*3600 + minutes*60 + seconds
    end_range = 0
    while end_range <= max_range -1:
        if minutes <= 0 and seconds <= 0:
            hours -= 1
            minutes = 60
        if seconds <= 0:
            minutes -= 1
            seconds = 59
        else:
            seconds -= 1
        print(f"\rThere is {hours} hours, {minutes} minutes, {seconds} seconds left!", end="")
        max_range -= 1
        time.sleep(1)
    print("\nNo time left!")