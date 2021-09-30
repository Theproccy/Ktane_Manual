""" A Electronic Assisted manual for the game Keep talking nobody explodes"""

import json

from find_path import solve_maze


def data_input():  # collects misc data abound the bomb for other defusing steps
    # var creation
    indicator_light_frk = False
    indicator_light_car = False
    parallel = False

    # data input
    serial_number = list(input("Please Enter the Serial Number : "))
    battery_numbers = int(
        input("Please enter the number of batteries on the bomb : "))
    parallel_input = int(
        input("Does the bomb have a parallel port (if Yes Type 1) : "))
    indicator_light_frk_input = int(
        input("Does the bomb have a lit FRK Indicator (if Yes Type 1) : "))
    indicator_light_car_input = int(
        input("Does the bomb have a lit CAR Indicator (if Yes Type 1) : "))

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
        if yellow == 0 and (int(serial_num[-1]) % 2 != 0):
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
    button_color_dictionary = {
        1: "BLUE",
        2: "RED",
        3: "WHITE",
        4: "YELLOW",
        5: "BLACK"
    }  # all color options for the button
    button_label_dictionary = {
        1: "Abort",
        2: "Detonate",
        3: "Hold",
        4: "Press"
    }  # all the label Options for the button
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
    print(button_color_dictionary)
    button_color_input = int(
        input("Please select the color of the button by entering the place in the list (e.g. Blue = 1) : "))
    print(button_label_dictionary)
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


def maze(mazes):  # a pathfinder that calculates moves to complete
    # var creation
    word_num = 1
    temp_list = []
    num = 0
    maze_map = {}

    # data input
    print("All Coordinates are to be entered like so : x,y  (e.g. (3,5) would be 3,5 )"
          "\n Top Left (1,1)")
    green_1_input = input("Please enter the coordinate of the green circle : ")
    green_2_input = input("Please enter the coordinate of the other green circle : ")
    start_position_input = input("Please enter the coordinate of the white dot : ")
    end_position_input = input("Please enter the coordinate of the red triangle : ")
    print("\n")  # quality of life new line

    # formatting
    green_1 = green_1_input.split(",")
    green_2 = green_2_input.split(",")
    start_position = start_position_input.split(",")
    end_position = end_position_input.split(",")

    # str to int
    green_1 = list(map(int, green_1))
    green_2 = list(map(int, green_2))
    start_position = list(map(int, start_position))
    end_position = list(map(int, end_position))
    # subtracts 1 so that the maze pathfinding works
    for i in range(len(start_position)):
        start_temp = start_position.pop(i)
        end_temp = end_position.pop(i)
        start_position.insert(i, start_temp - 1)
        end_position.insert(i, end_temp - 1)

    # maze selection
    test = False
    for i in range(9):
        if test is False:
            temp = mazes[str(i + 1)]

            temp_green_1 = temp["Green_circle_1"]
            temp_green_2 = temp["Green_circle_2"]

            if green_1 == temp_green_1[0] or green_1 == temp_green_2[0]:
                if green_2 == temp_green_1[0] or green_2 == temp_green_2[0]:
                    maze_map = temp
    # pathfinding
    route = solve_maze(start_position, start_position, end_position, [], maze_map)

    # conversion from coordinate route to instructions
    commands = []
    commands_condensed = []
    for i in range(len(route) - 1):
        temp_1 = route[i]
        temp_2 = route[i + 1]
        if temp_1[0] == temp_2[0]:  # if the x values are the same:
            if temp_1[1] > temp_2[1]:  # up
                commands.append("UP : ")
            if temp_1[1] < temp_2[1]:  # down
                commands.append("DOWN : ")
        if temp_1[1] == temp_2[1]:  # if the y values are the same:
            if temp_1[0] > temp_2[0]:  # left
                commands.append("LEFT : ")
            if temp_1[0] < temp_2[0]:  # right
                commands.append("RIGHT : ")

    # output formatting
    while num <= (len(commands) - 2):
        repeated_word = False
        if commands[num] == commands[num + 1]:  # if there are multiple in order of instructions
            word_num += 1
            repeated_word = True
        if repeated_word is False or num == (len(commands) - 2):  # when the multiples come to an end
            temp_list.append(commands[num])
            temp_list.append(word_num)
            commands_condensed.append(str(commands[num]) + str(word_num))
            temp_list = []
            word_num = 1
        num += 1
    commands_condensed.append(
        str(commands[-1]) + str(1))  # appends the last item as this cannot be added like the rest of them.

    # output and formatting
    for k in range(len(commands_condensed)):
        print(commands_condensed[k])


def simon_says(serial_number):  # simon says module
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


def memory():  # Memory module
    # Var creation
    position_list = []
    number_list = []
    display_num = int(input("\nwhat is the number displayed on the module : "))
    # Stage 1
    if display_num == 3:
        print("Press the button in the Third position")
        position_list.append(3)
        number_list.append(
            input("What is the number of the button you pressed : "))
    elif display_num == 4:
        print("Press the button in the Fourth position")
        position_list.append(4)
        number_list.append(
            input("What is the number of the button you pressed : "))
    else:
        print("Press the button in the Second position")
        position_list.append(2)
        number_list.append(
            input("What is the number of the button you pressed : "))

    # Stage 2
    display_num = int(input("\nwhat is the number displayed on the module : "))
    if display_num == 1:
        print("Press the button Labeled '4'")
        number_list.append(4)
        position_list.append(
            input("What is the position of the button you pressed : "))
    elif display_num == 3:
        print("Press the button in the First position")
        position_list.append(1)
        number_list.append(
            input("What is the number of the button you pressed : "))
    else:
        print("Press the button in the ", position_list[0], " position")
        position_list.append(position_list[0])
        number_list.append(
            input("What is the number of the button you pressed : "))

    # Stage 3
    display_num = int(input("\nwhat is the number displayed on the module : "))
    if display_num == 1:
        print("Press the button Labeled ", number_list[1])
        number_list.append(number_list[1])
        position_list.append(
            input("What is the position of the button you pressed : "))
    elif display_num == 2:
        print("Press the button Labeled ", number_list[0])
        number_list.append(number_list[0])
        position_list.append(
            input("What is the position of the button you pressed : "))
    elif display_num == 3:
        print("Press the button in the Third position")
        position_list.append(3)
        number_list.append(
            input("What is the number of the button you pressed : "))
    else:
        print("Press the button Labeled '4'")
        number_list.append(4)
        position_list.append(
            input("What is the position of the button you pressed : "))

    # Stage 4
    display_num = int(input("\nwhat is the number displayed on the module : "))
    if display_num == 1:
        print("Press the button in position ", position_list[0])
        position_list.append(position_list[0])
        number_list.append(
            input("What is the label of the button you pressed : "))
    elif display_num == 2:
        print("Press the button in the First position")
        position_list.append(1)
        number_list.append(
            input("What is the number of the button you pressed : "))
    else:
        print("Press the button in the ", position_list[1], " position")
        position_list.append(position_list[1])
        number_list.append(
            input("What is the number of the button you pressed : "))

    # Stage 5
    display_num = int(input("\nwhat is the number displayed on the module : "))
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
    # parallel and battery
    elif (int(serial_number[-1]) % 2) != 0 and parallel_port is True and battery_num >= 2:
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
    # even serial and battery
    elif (int(serial_number[-1]) % 2) == 0 and parallel_port is False and battery_num >= 2:
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
    # even serial and parallel
    elif (int(serial_number[-1]) % 2) == 0 and parallel_port is True and battery_num < 2:
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
    first_letter_input = str(
        input("Enter all of the letters in the first column (E.G. aelzx) : "))
    second_letter_input = str(
        input("Enter all of the letters in the Second column (E.G. aelzx) : "))
    third_letter_input = str(
        input("Enter all of the letters in the third column (E.G. aelzx) : "))

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
        wire_color = input(
            "\nPlease enter the color of the wire (Red=r,Blue=b,Black=k) : ")
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


def morse():  # morse table
    print("+-----------------------+--------+-----------+\n"
          "| Morse                 | Word   | Frequency |\n"
          "+=======================+========+===========+\n"
          "| .../...././.-../.-..  | shell  | 3.505     |\n"
          "+-----------------------+--------+-----------+\n"
          "| ..../.-/.-../.-../... | halls  | 3.515     |\n"
          "+-----------------------+--------+-----------+\n"
          "| .../.-../../.-.-/-.-  | slick  | 3.522     |\n"
          "+-----------------------+--------+-----------+\n"
          "| -/.-./../-.-./-.-     | trick  | 3.532     |\n"
          "+-----------------------+--------+-----------+\n"
          "| -.../---/-..-/./...   | boxes  | 3.535     |\n"
          "+-----------------------+--------+-----------+\n"
          "| .-.././.-/-.-/...     | leaks  | 3.542     |\n"
          "+-----------------------+--------+-----------+\n"
          "| .../-/.-./---/-.../.  | strobe | 3.545     |\n"
          "+-----------------------+--------+-----------+\n"
          "| -.../../.../-/.-./--- | bistro | 3.552     |\n"
          "+-----------------------+--------+-----------+\n"
          "| ..-./.-../../-.-./-.- | flick  | 3.555     |\n"
          "+-----------------------+--------+-----------+\n"
          "| -.../---/--/-.../...  | bombs  | 3.565     |\n"
          "+-----------------------+--------+-----------+\n"
          "| -.../.-././.-/-.-     | break  | 3.572     |\n"
          "+-----------------------+--------+-----------+\n"
          "| -.../.-./../-.-./-.-  | brick  | 3.575     |\n"
          "+-----------------------+--------+-----------+\n"
          "| .../-/./.-/-.-        | steak  | 3.582     |\n"
          "+-----------------------+--------+-----------+\n"
          "| .../-/../-./--.       | sting  | 3.592     |\n"
          "+-----------------------+--------+-----------+\n"
          "| ...-/./-.-./-/---/.-. | vector | 3.595     |\n"
          "+-----------------------+--------+-----------+\n"
          "| -..././.-/-/...       | beats  | 3.600     |\n"
          "+-----------------------+--------+-----------+\n")


def whose_on_first():
    display_word_dictionary = {
        "BLANK": "MR",
        "C": "TR",
        "CEE": "BR",
        "DISPLAY": "BR",
        "FIRST": "TR",
        "HOLD ON": "BR",
        "LEAD": "BR",
        "LED": "ML",
        "LEED": "BL",
        "NO": "BR",
        "NOTHING": "ML",
        "OKAY": "TR",
        "READ": "MR",
        "RED": "MR",
        "REED": "BL",
        "SAYS": "BR",
        "SEE": "BR",
        "THEIR": "MR",
        "THERE": "BR",
        "THEY ARE": "ML",
        "THEY'RE": "BL",
        "UR": "TL",
        "YES": "ML",
        "YOU": "MR",
        "YOU ARE": "BR",
        "YOU'RE": "MR",
        "YOUR": "MR",
        "": "BL"}
    word_corresponding_list = {
        "READY": ["YES", "OKAY", "WHAT", "MIDDLE", "LEFT", "PRESS", "RIGHT", "BLANK", "READY", "NO", "FIRST", "UHHH",
                  "NOTHING", "WAIT"],
        "FIRST": ["LEFT", "OKAY", "YES", "MIDDLE", "NO", "RIGHT", "NOTHING", "UHHH", "WAIT", "READY", "BLANK", "WHAT",
                  "PRESS", "FIRST"],
        "NO": ["BLANK", "UHHH", "WAIT", "FIRST", "WHAT", "READY", "RIGHT", "YES", "NOTHING", "LEFT", "PRESS", "OKAY",
               "NO", "MIDDLE"],
        "BLANK": ["WAIT", "RIGHT", "OKAY", "MIDDLE", "BLANK", "PRESS", "READY", "NOTHING", "NO", "WHAT", "LEFT", "UHHH",
                  "YES", "FIRST"],
        "NOTHING": ["UHHH", "RIGHT", "OKAY", "MIDDLE", "YES", "BLANK", "NO", "PRESS", "LEFT", "WHAT", "WAIT", "FIRST",
                    "NOTHING", "READY"],
        "YES": ["OKAY", "RIGHT", "UHHH", "MIDDLE", "FIRST", "WHAT", "PRESS", "READY", "NOTHING", "YES", "LEFT", "BLANK",
                "NO", "WAIT"],
        "WHAT": ["UHHH", "WHAT", "LEFT", "NOTHING", "READY", "BLANK", "MIDDLE", "NO", "OKAY", "FIRST", "WAIT", "YES",
                 "PRESS", "RIGHT"],
        "UHHH": ["READY", "NOTHING", "LEFT", "WHAT", "OKAY", "YES", "RIGHT", "NO", "PRESS", "BLANK", "UHHH", "MIDDLE",
                 "WAIT", "FIRST"],
        "LEFT": ["RIGHT", "LEFT", "FIRST", "NO", "MIDDLE", "YES", "BLANK", "WHAT", "UHHH", "WAIT", "PRESS", "READY",
                 "OKAY", "NOTHING"],
        "RIGHT": ["YES", "NOTHING", "READY", "PRESS", "NO", "WAIT", "WHAT", "RIGHT", "MIDDLE", "LEFT", "UHHH", "BLANK",
                  "OKAY", "FIRST"],
        "MIDDLE": ["BLANK", "READY", "OKAY", "WHAT", "NOTHING", "PRESS", "NO", "WAIT", "LEFT", "MIDDLE", "RIGHT",
                   "FIRST", "UHHH", "YES"],
        "OKAY": ["MIDDLE", "NO", "FIRST", "YES", "UHHH", "NOTHING", "WAIT", "OKAY", "LEFT", "READY", "BLANK", "PRESS",
                 "WHAT", "RIGHT"],
        "WAIT": ["UHHH", "NO", "BLANK", "OKAY", "YES", "LEFT", "FIRST", "PRESS", "WHAT", "WAIT", "NOTHING", "READY",
                 "RIGHT", "MIDDLE"],
        "PRESS": ["RIGHT", "MIDDLE", "YES", "READY", "PRESS", "OKAY", "NOTHING", "UHHH", "BLANK", "LEFT", "FIRST",
                  "WHAT", "NO", "WAIT"],
        "YOU": ["SURE", "YOU ARE", "YOUR", "YOU'RE", "NEXT", "UH HUH", "UR", "HOLD", "WHAT?", "YOU", "UH UH", "LIKE",
                "DONE", "U"],
        "YOU ARE": ["YOUR", "NEXT", "LIKE", "UH HUH", "WHAT?", "DONE", "UH UH", "HOLD", "YOU", "U", "YOU'RE", "SURE",
                    "UR", "YOU ARE"],
        "YOUR": ["UH UH", "YOU ARE", "UH HUH", "YOUR", "NEXT", "UR", "SURE", "U", "YOU'RE", "YOU", "WHAT?", "HOLD",
                 "LIKE", "DONE"],
        "YOU'RE": ["YOU", "YOU'RE", "UR", "NEXT", "UH UH", "YOU ARE", "U", "YOUR", "WHAT?", "UH HUH", "SURE", "DONE",
                   "LIKE", "HOLD"],
        "UR": ["DONE", "U", "UR", "UH HUH", "WHAT?", "SURE", "YOUR", "HOLD", "YOU'RE", "LIKE", "NEXT", "UH UH",
               "YOU ARE", "YOU"],
        "U": ["UH HUH", "SURE", "NEXT", "WHAT?", "YOU'RE", "UR", "UH UH", "DONE", "U", "YOU", "LIKE", "HOLD", "YOU ARE",
              "YOUR"],
        "UH HUH": ["UH HUH", "YOUR", "YOU ARE", "YOU", "DONE", "HOLD", "UH UH", "NEXT", "SURE", "LIKE", "YOU'RE", "UR",
                   "U", "WHAT?"],
        "UH UH": ["UR", "U", "YOU ARE", "YOU'RE", "NEXT", "UH UH", "DONE", "YOU", "UH HUH", "LIKE", "YOUR", "SURE",
                  "HOLD", "WHAT?"],
        "WHAT?": ["YOU", "HOLD", "YOU'RE", "YOUR", "U", "DONE", "UH UH", "LIKE", "YOU ARE", "UH HUH", "UR", "NEXT",
                  "WHAT?", "SURE"],
        "DONE": ["SURE", "UH HUH", "NEXT", "WHAT?", "YOUR", "UR", "YOU'RE", "HOLD", "LIKE", "YOU", "U", "YOU ARE",
                 "UH UH", "DONE"],
        "NEXT": ["WHAT?", "UH HUH", "UH UH", "YOUR", "HOLD", "SURE", "NEXT", "LIKE", "DONE", "YOU ARE", "UR", "YOU'RE",
                 "U", "YOU"],
        "HOLD": ["YOU ARE", "U", "DONE", "UH UH", "YOU", "UR", "SURE", "WHAT?", "YOU'RE", "NEXT", "HOLD", "UH HUH",
                 "YOUR", "LIKE"],
        "SURE": ["YOU ARE", "DONE", "LIKE", "YOU'RE", "YOU", "HOLD", "UH HUH", "UR", "SURE", "U", "WHAT?", "NEXT",
                 "YOUR", "UH UH"],
        "LIKE": ["YOU'RE", "NEXT", "U", "UR", "HOLD", "DONE", "UH UH", "WHAT?", "UH HUH", "YOU", "LIKE", "SURE",
                 "YOU ARE", "YOUR"]
    }
    for i in range(3):
        displayed_word = display_word_dictionary[input("Please enter the word displayed : ").upper()]
        print(displayed_word)
        corresponding_word = word_corresponding_list[
            input("Please enter the word in the box that was indicated by the word above").upper()]
        print(corresponding_word)


# TODO ADD OTHER LIST
# TODO ADD METHOD TO FIND WORDS

def module_select(serial_number, battery_numbers, parallel, indicator_light_frk,
                  indicator_light_car, all_mazes):  # function for all of the questions to be asked
    print("\nFor New Bomb (0)"
          "\nModules : Wires(1), Buttons(2), Maze(3), Simon says(4), Memory(5), Complex wires(6), Passwords(7), "
          "Wire Sequences(8), Morse(9), On The Subject Of Whose First(10)"
          )

    selection_input = str(
        input("Please press the key for what you want to do (E.G. wires=1) : "))
    print("\n")

    if selection_input != "":
        selection = int(selection_input)
        if selection == 1:
            wires(serial_number)
        elif selection == 2:
            button(battery_numbers, indicator_light_car, indicator_light_frk)
        elif selection == 3:
            maze(all_mazes)
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
        elif selection == 9:
            morse()
        elif selection == 10:
            whose_on_first()
        elif selection == 0:
            return True
        else:
            pass


def main():
    print("https://www.bombmanual.com/print/KeepTalkingAndNobodyExplodes-BombDefusalManual-v1.pdf"
          "\n Open the pages on symbols and the needy Knob module")
    ALL_MAZES = json.load(open("data.json"))
    serial_number, battery_numbers, parallel, indicator_light_frk, indicator_light_car = data_input()
    module_select(serial_number, battery_numbers, parallel,
                  indicator_light_frk, indicator_light_car, ALL_MAZES)
    escape = False
    while escape is False:
        try:
            new_bomb = module_select(serial_number, battery_numbers, parallel,
                                     indicator_light_frk, indicator_light_car, ALL_MAZES)
            if new_bomb is True:
                serial_number, battery_numbers, parallel, indicator_light_frk, indicator_light_car = data_input()

        except:
            print(
                "There was an error in the input."
                "\nIf you think there is no error in your input raise an issue at:"
                "\nhttps://github.com/Theproccy/Keep_Typing_And_Nobody_Explodes__/issues/new")

    # is_bomb_defused = int(input("Is Bomb Defused (1 for yes)"))
    # if is_bomb_defused == 1:
    # escape = True


if __name__ == "__main__":
    main()
