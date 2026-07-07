while True:
    user_input = input("Enter command for s/w (start/stop/pause) : ")

    match user_input:
        case "start":
            print("S/w starting.......")
        case "stop":
            print("S/w is stopped")
        case "pause":
            print("S/w paused")
        case _: 
            print("Unknow command, please enter valid command again")
            
    sw_stop = input("Do you want to stop the program? (yes/no): ")
    if sw_stop == "yes":
        break