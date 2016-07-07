

def draw_menu(options):
    print("")
    for i in range(1, len(options)+1):
        print(str(i) + ".: " + options[i-1])
    print("")

elements = ["elso", "masodik", "harmadik", "negyedik"]


while True:
    draw_menu(elements)
    user_input = input("Please specify which picture should be drawn. ")

    if user_input == "x":
        exit()

    elif user_input == "1":
        pass

    elif user_input == "2":
        pass

    elif user_input == "3":
        pass

    elif user_input == "4":
        pass
