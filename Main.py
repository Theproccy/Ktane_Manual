# import multiprocessing
import graphics


def data_input():  # collects misc data abound the bomb for other defusing steps
    # var creation
    indicator_light_frk = False
    indicator_light_car = False
    parallel = False

    # data input
    serial_number = list(input("Please Enter the Serial Number : "))
    battery_numbers = int(input("Please enter the number of batteries on the bomb : "))
    parallel_input = int(input("Dose the bomb have a parallel port (if Yes Type 1) : "))
    indicator_light_frk_input = int(input("Dose the bomb have a lit FRK Indicator (if Yes Type 1) : "))
    indicator_light_car_input = int(input("Dose the bomb have a lit CAR Indicator (if Yes Type 1) : "))

    if indicator_light_frk_input == 1:  # converts the input into a bool
        indicator_light_frk = True
    if indicator_light_car_input == 1:
        indicator_light_car = True
    if parallel_input == 1:
        parallel = True

    return serial_number, battery_numbers, parallel, indicator_light_frk, indicator_light_car


def wires(serial_num):  # Simple wires
    # var creation
    yellow = 0
    red = 0
    blue = 0
    black = 0
    white = 0

    # data input
    wire_input = str(input(
        "Please enter the wires in order from top to bottom in order (Yellow=Y,Red=R,Blue=B,Black=K,White=W) EG [RBy] "
        ": "
    ))

    # data gathering from input
    wire_num = len(wire_input)  # the number of wires
    wire = wire_input.upper()  # converts wires to uppercase
    wire_list = wire.strip()  # splits the wires to individual values and stores them as a list

    # converts input into the number of each color of wire
    for i in range(wire_num):
        temp = wire_list[i]
        if temp == 'Y':
            yellow += 1

        elif temp == 'R':
            red += 1

        elif temp == 'B':
            blue += 1

        elif temp == 'K':
            black += 1

        elif temp == 'W':
            white += 1

    # solver
    # print(yellow,red,blue,black,white)

    if wire_num == 3:
        if red == 0:
            print("Cut The Second Wire")
        elif wire_list[-1] == 'W':
            print("Cut The Last Wire")
        elif blue > 1:
            print("Cut The Last Blue Wire")
        else:
            print("Cut Last Wire")

    elif wire_num == 4:
        if red > 1 and (int(serial_num[-1]) % 2 == 0):
            print("Cut The Last Red Wire")
        elif wire_list[-1] == 'Y' and red == 0:
            print("Cut The First Wire")
        elif blue == 1:
            print("Cut The First Wire")
        elif yellow > 1:
            print("Cut The Last Wire")
        else:
            print("Cut The Second Wire")

    elif wire_num == 5:
        if wire_list[-1] and (int(serial_num[-1]) % 2 != 0) == "K":
            print("Cut The Fourth Wire")
        elif red == 1 and yellow > 1:
            print("Cut The First Wire")
        elif black == 0:
            print("Cut The Second Wire")
        else:
            print("Cut The First Wire")

    elif wire_num == 6:
        if yellow == 0 and (int(serial_num[-1]) % 2 == 0):
            print("Cut The Third Wire")
        elif yellow == 1 and white > 1:
            print("Cut The Fourth Wire")
        elif red == 0:
            print("Cut The Last Wire")
        else:
            print("Cut The Forth Wire")
    # End function


def button(battery_num, indicator_car, indicator_frk):  # The Button
    # var creation
    button_color_list = ["BLUE", "RED", "WHITE", "YELLOW", "BLACK"]  # all color options for the button
    button_label_list = ["Abort", "Detonate", "Hold", "Press"]  # all the label Options for the button
    # colors
    blue = False
    red = False
    white = False
    yellow = False
    # labels
    abort = False
    detonate = False
    hold = False

    # data input
    print(button_color_list)
    button_color_input = int(
        input("Please select the color of the button by entering the place in the list (e.g. Blue = 1) : "))
    print(button_label_list)
    button_label_input = int(
        input("Please select the label of the button by entering the place in the list (e.g. Abort = 1) : "))

    # data formatting
    # colors
    if button_color_input == 1:
        blue = True
    elif button_color_input == 2:
        red = True
    elif button_color_input == 3:
        white = True
    elif button_color_input == 4:
        yellow = True
        # labels
    if button_label_input == 1:
        abort = True
    elif button_label_input == 2:
        detonate = True
    elif button_label_input == 3:
        hold = True
    else:
        pass

    # solving
    # main section
    releasing_held_button = False
    if blue is True and abort is True:
        releasing_held_button = True
    elif battery_num > 1 and detonate:
        print("Press and Immediately Release")
    elif white is True and indicator_car is True:
        releasing_held_button = True
    elif indicator_frk is True and battery_num > 2:
        print("Press and Immediately Release")
    elif yellow is True:
        releasing_held_button = True
    elif red is True and hold is True:
        print("Press and Immediately Release")
    else:
        releasing_held_button = True

        # releasing held button section
    if releasing_held_button is True:
        print("Strip Color\n"
              "Blue = 4 any position\n"
              "Yellow = 5 any position\n"
              "Else 1 in any position")


def maze():  # pathfinds moves to complet
    pass


def simon_says(serial_number):
    Vowels = False
    for i in range(len(serial_number)):
        temp = str(serial_number[i])
        temp = temp.upper()
        if temp == "A" or temp == "E" or temp == "I" or temp == "O" or temp == "U":
            Vowels = True
            continue
    if Vowels:
        print(  # vowel simon says
            "+-------------------------------+--------+-------+--------+--------+\n"
            "|                               | Red    | Blue  | Green  | Yellow |\n"
            "+==================+============+========+=======+========+========+\n"
            "|                  | No Strikes | Blue   | Red   | Yellow | Green  |\n"
            "|                  +------------+--------+-------+--------+--------+\n"
            "| Button to press: | 1 Strike   | Yellow | Green | Blue   | Red    |\n"
            "|                  +------------+--------+-------+--------+--------+\n"
            "|                  | 2 Strike   | Green  | Red   | Yellow | Blue   |\n"
            "+------------------+------------+--------+-------+--------+--------+")
    else:
        print(  # no vowel simon says
            "+-------------------------------+--------+--------+--------+--------+\n"
            "|                               | Red    | Blue   | Green  | Yellow |\n"
            "+==================+============+========+========+========+========+\n"
            "|                  | No Strikes | Blue   | Yellow | Green  | Red    |\n"
            "|                  +------------+--------+--------+--------+--------+\n"
            "| Button to press: | 1 Strike   | Red    | Blue   | Yellow | Green  |\n"
            "|                  +------------+--------+--------+--------+--------+\n"
            "|                  | 2 Strike   | Yellow | Green  | Blue   | Red    |\n"
            "+------------------+------------+--------+--------+--------+--------+")


def memory():
    position_list = []
    number_list = []
    display_num = int(input("what is the number displayed on the module : "))
    # Stage 1
    if display_num == 3:
        print("Press the button in the Third position")
        position_list.append(3)
        number_list.append(input("What is the number of the button you pressed : "))
    elif display_num == 4:
        print("Press the button in the Fourth position")
        position_list.append(4)
        number_list.append(input("What is the number of the button you pressed : "))
    else:
        print("Press the button in the Second position")
        position_list.append(2)
        number_list.append(input("What is the number of the button you pressed : "))

    # Stage 2
    display_num = int(input("what is the number displayed on the module : "))
    if display_num == 1:
        print("Press the button Labeled '4'")
        number_list.append(4)
        position_list.append(input("What is the position of the button you pressed : "))
    elif display_num == 3:
        print("Press the button in the First position")
        position_list.append(1)
        number_list.append(input("What is the number of the button you pressed : "))
    else:
        print("Press the button in the ", position_list[0], " position")
        position_list.append(position_list[0])
        number_list.append(input("What is the number of the button you pressed : "))

    # Stage 3
    display_num = int(input("what is the number displayed on the module : "))
    if display_num == 1:
        print("Press the button Labeled ", number_list[1])
        number_list.append(number_list[1])
        position_list.append(input("What is the position of the button you pressed : "))
    elif display_num == 2:
        print("Press the button Labeled ", number_list[0])
        number_list.append(number_list[0])
        position_list.append(input("What is the position of the button you pressed : "))
    elif display_num == 3:
        print("Press the button in the Third position")
        position_list.append(3)
        number_list.append(input("What is the number of the button you pressed : "))
    else:
        print("Press the button Labeled '4'")
        number_list.append(4)
        position_list.append(input("What is the position of the button you pressed : "))

    # Stage 4
    display_num = int(input("what is the number displayed on the module : "))
    if display_num == 1:
        print("Press the button in position ", position_list[0])
        position_list.append(position_list[0])
        number_list.append(input("What is the label of the button you pressed : "))
    elif display_num == 2:
        print("Press the button in the First position")
        position_list.append(1)
        number_list.append(input("What is the number of the button you pressed : "))
    else:
        print("Press the button in the ", position_list[1], " position")
        position_list.append(position_list[1])
        number_list.append(input("What is the number of the button you pressed : "))

    # Stage 5
    display_num = int(input("what is the number displayed on the module : "))
    if display_num == 1:
        print("Press the button Labeled ", number_list[0])
        number_list.append(number_list[0])
    elif display_num == 2:
        print("Press the button Labeled ", number_list[1])
        number_list.append(number_list[1])
    elif display_num == 3:
        print("Press the button Labeled ", number_list[3])
        number_list.append(number_list[3])
    else:
        print("Press the button labeled ", number_list[2])
        number_list.append(number_list[2])
    # Function end


def complex_wires(serial_number, parallel_port, battery_num):
    if (int(serial_number[-1]) % 2) != 0 and parallel_port is False and battery_num < 2:  # all false
        print("+------+-------+-------+-------+-------+\n"
              "|      | White | Red   | Blue  | Both  |\n"
              "+======+=======+=======+=======+=======+\n"
              "| None | Cut   | Don't | Don't | Don't |\n"
              "+------+-------+-------+-------+-------+\n"
              "| Star | Cut   | Cut   | Don't | Don't |\n"
              "+------+-------+-------+-------+-------+\n"
              "| LED  | Don't | Don't | Don't | Don't |\n"
              "+------+-------+-------+-------+-------+\n"
              "| Both | Don't | Don't | Don't | Don't |\n"
              "+------+-------+-------+-------+-------+")
    elif (int(serial_number[-1]) % 2) != 0 and parallel_port is False and battery_num >= 2:  # battery
        print("+------+-------+-------+-------+----------+\n"
              "|      | White | Red   | Blue  | Both     |\n"
              "+======+=======+=======+=======+==========+\n"
              "| None | Cut   | Don't | Don't | Don't    |\n"
              "+------+-------+-------+-------+----------+\n"
              "| Star | Cut   | Cut   | Don't | Don't    |\n"
              "+------+-------+-------+-------+----------+\n"
              "| LED  | Don't | Cut   | Don't | Don't    |\n"
              "+------+-------+-------+-------+----------+\n"
              "| Both | Cut   | Cut   | Don't | Don't    |\n"
              "+------+-------+-------+-------+----------+")
    elif (int(serial_number[-1]) % 2) != 0 and parallel_port is True and battery_num < 2:  # parallel
        print("+------+-------+-------+-------+-------+\n"
              "|      | White | Red   | Blue  | Both  |\n"
              "+======+=======+=======+=======+=======+\n"
              "| None | Cut   | Don't | Don't | Don't |\n"
              "+------+-------+-------+-------+-------+\n"
              "| Star | Cut   | Cut   | Don't | Cut   |\n"
              "+------+-------+-------+-------+-------+\n"
              "| LED  | Don't | Don't | Cut   | Don't |\n"
              "+------+-------+-------+-------+-------+\n"
              "| Both | Don't | Don't | Cut   | Don't |\n"
              "+------+-------+-------+-------+-------+")
    elif (int(serial_number[-1]) % 2) != 0 and parallel_port is True and battery_num >= 2:  # parallel and battery
        print("+------+-------+-------+-------+-------+\n"
              "|      | White | Red   | Blue  | Both  |\n"
              "+======+=======+=======+=======+=======+\n"
              "| None | Cut   | Don't | Don't | Don't |\n"
              "+------+-------+-------+-------+-------+\n"
              "| Star | Cut   | Cut   | Don't | Cut   |\n"
              "+------+-------+-------+-------+-------+\n"
              "| LED  | Don't | Cut   | Cut   | Don't |\n"
              "+------+-------+-------+-------+-------+\n"
              "| Both | Cut   | Cut   | Cut   | Don't |\n"
              "+------+-------+-------+-------+-------+")
    elif (int(serial_number[-1]) % 2) == 0 and parallel_port is False and battery_num < 2:  # even serial
        print("+------+-------+-------+-------+-------+\n"
              "|      | White | Red   | Blue  | Both  |\n"
              "+======+=======+=======+=======+=======+\n"
              "| None | Cut   | Cut   | Cut   | Cut   |\n"
              "+------+-------+-------+-------+-------+\n"
              "| Star | Cut   | Cut   | Don't | Don't |\n"
              "+------+-------+-------+-------+-------+\n"
              "| LED  | Don't | Don't | Don't | Cut   |\n"
              "+------+-------+-------+-------+-------+\n"
              "| Both | Don't | Don't | Don't | Don't |\n"
              "+------+-------+-------+-------+-------+")
    elif (int(serial_number[-1]) % 2) == 0 and parallel_port is False and battery_num >= 2:  # even serial and battery
        print("+------+-------+-----+-------+-------+\n"
              "|      | White | Red | Blue  | Both  |\n"
              "+======+=======+=====+=======+=======+\n"
              "| None | Cut   | Cut | Cut   | Cut   |\n"
              "+------+-------+-----+-------+-------+\n"
              "| Star | Cut   | Cut | Don't | Don't |\n"
              "+------+-------+-----+-------+-------+\n"
              "| LED  | Don't | Cut | Don't | Cut   |\n"
              "+------+-------+-----+-------+-------+\n"
              "| Both | Cut   | Cut | Don't | Don't |\n"
              "+------+-------+-----+-------+-------+")
    elif (int(serial_number[-1]) % 2) == 0 and parallel_port is True and battery_num < 2:  # even serial and parallel
        print("+------+-------+-------+-------+-------+\n"
              "|      | White | Red   | Blue  | Both  |\n"
              "+======+=======+=======+=======+=======+\n"
              "| None | Cut   | Cut   | Cut   | Cut   |\n"
              "+------+-------+-------+-------+-------+\n"
              "| Star | Cut   | Cut   | Don't | Cut   |\n"
              "+------+-------+-------+-------+-------+\n"
              "| LED  | Don't | Don't | Cut   | Cut   |\n"
              "+------+-------+-------+-------+-------+\n"
              "| Both | Don't | Don't | Cut   | Don't |\n"
              "+------+-------+-------+-------+-------+")
    else:  # all
        print("+------+-------+-----+-------+-------+\n"
              "|      | White | Red | Blue  | Both  |\n"
              "+======+=======+=====+=======+=======+\n"
              "| None | Cut   | Cut | Cut   | Cut   |\n"
              "+------+-------+-----+-------+-------+\n"
              "| Star | Cut   | Cut | Don't | Cut   |\n"
              "+------+-------+-----+-------+-------+\n"
              "| LED  | Don't | Cut | Cut   | Cut   |\n"
              "+------+-------+-----+-------+-------+\n"
              "| Both | Cut   | Cut | Cut   | Don't |\n"
              "------+-------+-----+-------+-------+")


def passwords():
    # var creation
    password_list = ["about", "after", "again", "below", "could",
                     "every", "first", "found", "great", "house",
                     "large", "learn", "never", "other", "place",
                     "plant", "point", "right", "small", "sound",
                     "spell", "still", "study", "their", "there",
                     "these", "thing", "think", "three", "water",
                     "where", "which", "world", "would", "write"]
    answers_list_1 = []
    answers_list_2 = []
    answers_list_3 = []
    # data input
    first_letter_input = str(input("Enter all of the letters in the first column (E.G. aelzx) : "))
    second_letter_input = str(input("Enter all of the letters in the Second column (E.G. aelzx) : "))
    third_letter_input = str(input("Enter all of the letters in the third column (E.G. aelzx) : "))

    # data formatting
    first_letter_list = first_letter_input.strip()
    second_letter_list = second_letter_input.strip()
    third_letter_list = third_letter_input.strip()

    # first char search
    for i in range(len(password_list)):
        temp_word = password_list[i]
        for j in range(len(first_letter_list)):
            temp_search = first_letter_list[j]
            temp_search = temp_search.lower()
            if temp_word[0] == temp_search:
                answers_list_1.append(temp_word)

    # second char search
    for i in range(len(answers_list_1)):
        temp_word = answers_list_1[i]
        for j in range(len(second_letter_list)):
            temp_search = second_letter_list[j]
            temp_search = temp_search.lower()
            if temp_word[1] == temp_search:
                answers_list_2.append(temp_word)

    # third char search
    for i in range(len(answers_list_2)):
        temp_word = answers_list_2[i]
        for j in range(len(third_letter_list)):
            temp_search = third_letter_list[j]
            temp_search = temp_search.lower()
            if temp_word[2] == temp_search:
                answers_list_3.append(temp_word)

    print(answers_list_3)  # return answer


def wire_sequences():
    # var creation
    red = 0
    blue = 0
    black = 0

    red_options = {
        1: "C",
        2: "B",
        3: "A",
        4: "A or C",
        5: "B",
        6: "A or C",
        7: "A, B or C",
        8: "A or B",
        9: "B"
    }

    blue_options = {
        1: "B",
        2: "A or C",
        3: "B",
        4: "A",
        5: "B",
        6: "B or C",
        7: "C",
        8: "A or C",
        9: "A"
    }

    black_options = {
        1: "A, B or C",
        2: "A or C",
        3: "B",
        4: "A or C",
        5: "B",
        6: "B or C",
        7: "A or B",
        8: "C",
        9: "C"
    }
    # exit button
    print("leave blank to exit this routine")

    # solver

    while 1 == 1:
        wire_color = input("\nPlease enter the color of the wire (Red=r,Blue=b,Black=k) : ")
        wire_color.lower()
        if wire_color == "r":
            red += 1
            print("Cut the wire if it is connected to ", red_options[red])

        elif wire_color == "b":
            blue += 1
            print("Cut the wire if it is connected to ", blue_options[blue])
        elif wire_color == "k":
            black += 1
            print("Cut the wire if it is connected to ", black_options[black])
        else:
            break


def module_select(serial_number, battery_numbers, parallel, indicator_light_frk,
                  indicator_light_car):  # function for all of the questions to be asked
    print("\n"
          "modules : Wires(1), Buttons(2), Maze(3), Simon says(4), Memory(5), Complex wires(6), Passwords(7), "
          "Wire Sequences(8)")
    selection_input = str(input("Please press the key for what you want to do (E.G. wires=1) : "))
    print("\n")

    if selection_input != "":
        selection = int(selection_input)
        if selection == 1:
            wires(serial_number)
        elif selection == 2:
            button(battery_numbers, indicator_light_car, indicator_light_frk)
        elif selection == 3:
            maze()
        elif selection == 4:
            simon_says(serial_number)
        elif selection == 5:
            memory()
        elif selection == 6:
            complex_wires(serial_number, parallel, battery_numbers)
        elif selection == 7:
            passwords()
        elif selection == 8:
            wire_sequences()
        else:
            pass


def main_window():
    main_win = graphics.GraphWin("Keep Talking Nobody Explods Automated Manual", 800, 600)
    main_win.setBackground("blue")
    main_win.getMouse()


def main():
    serial_number, battery_numbers, parallel, indicator_light_frk, indicator_light_car = data_input()
    escape = False
    while escape is False:
        module_select(serial_number, battery_numbers, parallel, indicator_light_frk, indicator_light_car)

        # is_bomb_defused = int(input("Is Bomb Defused (1 for yes)"))
        # if is_bomb_defused == 1:
        # escape = True


main()
