""" A Electronic Assisted manual for the game Keep talking nobody explodes"""

import json

import cutie
import rich
import rich.console
import texttable

from find_path import solve_maze

console = rich.console.Console()


def data_input():  # collects misc data abound the bomb for other defusing steps
    # data input
    serial_number = list(input("Please Enter the Serial Number : "))
    battery_numbers = int(input("Please enter the number of batteries on the bomb : "))
    parallel = cutie.prompt_yes_or_no("Does the bomb have a parallel port: ")
    indicator_light_frk = cutie.prompt_yes_or_no("Does the bomb have a lit FRK Indicator: ")
    indicator_light_car = cutie.prompt_yes_or_no("Does the bomb have a lit CAR Indicator: ")

    return serial_number, battery_numbers, parallel, indicator_light_frk, indicator_light_car


def wires(serial_num):  # Simple wires
    # var creation
    yellow = 0
    red = 0
    blue = 0
    black = 0
    white = 0

    # data input
    wire_input = console.input(
        "Please enter the wires in order from top to bottom in order ([bold red]Yellow=Y,Red=R,Blue=B,Black=K,"
        "White=W[/bold red]) EG [RBy] "
        ": "
    )

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
    answer = ""
    if wire_num == 3:
        if red == 0:
            answer = "Cut The Second Wire"
        elif wire_list[-1] == 'W':
            answer = "Cut The Last Wire"
        elif blue > 1:
            answer = "Cut The Last Blue Wire"
        else:
            answer = "Cut Last Wire"

    elif wire_num == 4:
        if red > 1 and (int(serial_num[-1]) % 2 == 0):
            answer = "Cut The Last Red Wire"
        elif wire_list[-1] == 'Y' and red == 0:
            answer = "Cut The First Wire"
        elif blue == 1:
            answer = "Cut The First Wire"
        elif yellow > 1:
            answer = "Cut The Last Wire"
        else:
            answer = "Cut The Second Wire"

    elif wire_num == 5:
        if wire_list[-1] and (int(serial_num[-1]) % 2 != 0) == "K":
            answer = "Cut The Fourth Wire"
        elif red == 1 and yellow > 1:
            answer = "Cut The First Wire"
        elif black == 0:
            answer = "Cut The Second Wire"
        else:
            answer = "Cut The First Wire"

    elif wire_num == 6:
        if yellow == 0 and (int(serial_num[-1]) % 2 != 0):
            answer = "Cut The Third Wire"
        elif yellow == 1 and white > 1:
            answer = "Cut The Fourth Wire"
        elif red == 0:
            answer = "Cut The Last Wire"
        else:
            answer = "Cut The Forth Wire"

    rich.print("[bold green]" + answer + "[/bold green]")
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
    print("Please Select the color: ")
    button_color_input = cutie.select(button_color_list)
    print("Please select the label: ")
    button_label_input = cutie.select(button_label_list)
    print("\n")

    # data formatting
    # colors
    if button_color_input == 0:
        blue = True
    elif button_color_input == 1:
        red = True
    elif button_color_input == 2:
        white = True
    elif button_color_input == 3:
        yellow = True
        # labels
    if button_label_input == 0:
        abort = True
    elif button_label_input == 1:
        detonate = True
    elif button_label_input == 2:
        hold = True

    # solving
    # main section
    answer = ""
    releasing_held_button = False
    if blue is True and abort is True:
        releasing_held_button = True
    elif battery_num > 1 and detonate is True:
        answer = "Press and Immediately Release"
    elif white is True and indicator_car is True:
        releasing_held_button = True
    elif indicator_frk is True and battery_num > 2:
        answer = "Press and Immediately Release"
    elif yellow is True:
        releasing_held_button = True
    elif red is True and hold is True:
        answer = "Press and Immediately Release"
    else:
        releasing_held_button = True

        # releasing held button section
    if releasing_held_button is True:
        answer = "Hold the Button\nStrip Color:\nBlue = 4 any position\nYellow = 5 any position\nOtherwise 1 in any " \
                 "position "
    rich.print("[bold green]" + answer + "[/bold green]")


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
    if commands[-1] != commands[-2]:
        commands_condensed.append(
            str(commands[-1]) + str(1))  # appends the last item as this cannot be added like the rest of them.

    # output and formatting
    for k in range(len(commands_condensed)):
        rich.print("[bold green]" + commands_condensed[k] + "[/bold green]")


def simon_says(serial_number):  # simon says module
    Vowels = False
    for i in range(len(serial_number)):
        temp = str(serial_number[i])
        temp = temp.upper()
        if temp == "A" or temp == "E" or temp == "I" or temp == "O" or temp == "U":
            Vowels = True
            continue
    if Vowels:  # vowel simon says
        answer = "+-------------------------------+--------+-------+--------+--------+\n" \
                 "|                               | Red    | Blue  | Green  | Yellow |\n" \
                 "+==================+============+========+=======+========+========+\n" \
                 "|                  | No Strikes | Blue   | Red   | Yellow | Green  |\n" \
                 "|                  +------------+--------+-------+--------+--------+\n" \
                 "| Button to press: | 1 Strike   | Yellow | Green | Blue   | Red    |\n" \
                 "|                  +------------+--------+-------+--------+--------+\n" \
                 "|                  | 2 Strike   | Green  | Red   | Yellow | Blue   |\n" \
                 "+------------------+------------+--------+-------+--------+--------+"
    else:  # no vowel simon says
        answer = "+-------------------------------+--------+--------+--------+--------+\n" \
                 "|                               | Red    | Blue   | Green  | Yellow |\n" \
                 "+==================+============+========+========+========+========+\n" \
                 "|                  | No Strikes | Blue   | Yellow | Green  | Red    |\n" \
                 "|                  +------------+--------+--------+--------+--------+\n" \
                 "| Button to press: | 1 Strike   | Red    | Blue   | Yellow | Green  |\n" \
                 "|                  +------------+--------+--------+--------+--------+\n" \
                 "|                  | 2 Strike   | Yellow | Green  | Blue   | Red    |\n" \
                 "+------------------+------------+--------+--------+--------+--------+"
    rich.print("[bold green]" + answer + "[/bold green]")


def memory():  # Memory module
    # Var creation
    position_list = []
    label_list = []
    label_input_required = False
    label = 0
    position = 0
    answer = ""
    position_word_dictionary = {
        1: "Press the button in the first position",
        2: "Press the button in the second position",
        3: "Press the button in the third position",
        4: "Press the button in the fourth position"
    }
    label_word_dictionary = {
        1: "Press the button labeled '1'",
        2: "Press the button labeled '2'",
        3: "Press the button labeled '3'",
        4: "Press the button labeled '4'"
    }

    for i in range(5):  # 5 levels of memory section
        display_num = int(input("\nWhat is the number displayed on the module: "))
        if i == 0:  # Stage 1
            if display_num == 1 or display_num == 2:
                label_input_required = True
                position = 2  # Second position
                answer = position_word_dictionary[position]
            elif display_num == 3:
                label_input_required = True
                position = 3  # Third position
                answer = position_word_dictionary[position]
            elif display_num == 4:
                label_input_required = True
                position = 4  # Forth position
                answer = position_word_dictionary[position]

        elif i == 1:  # Stage 2
            if display_num == 1:
                label_input_required = False
                label = 4  # Labeled 4
                answer = label_word_dictionary[label]
            elif display_num == 2 or display_num == 4:
                label_input_required = True
                position = position_list[0]  # Same position as stage 1
                answer = position_word_dictionary[position]
            elif display_num == 3:
                label_input_required = True
                position = 1  # First position
                answer = position_word_dictionary[position]

        elif i == 2:  # Stage 3
            if display_num == 1:
                label_input_required = False
                label = label_list[1]  # Same label as stage 2
                answer = label_word_dictionary[label]
            elif display_num == 2:
                label_input_required = False
                label = label_list[0]  # Same label as stage 1
                answer = label_word_dictionary[label]
            elif display_num == 3:
                label_input_required = True
                position = 3  # Third position
                answer = position_word_dictionary[position]
            elif display_num == 4:
                label_input_required = False
                label = 4  # Labeled 4
                answer = label_word_dictionary[4]

        elif i == 3:  # Stage 4
            if display_num == 1:
                label_input_required = True
                position = position_list[0]  # Same position as stage 1
                answer = position_word_dictionary[position]
            elif display_num == 2:
                label_input_required = True
                position = 1  # First position
                answer = position_word_dictionary[position]
            elif display_num == 3 or display_num == 4:
                label_input_required = True
                position = position_list[1]  # Same position as stage 2
                answer = position_word_dictionary[position]

        else:  # Stage 5
            if display_num == 1:
                label_input_required = False
                label = label_list[0]  # Same label as stage 1
                answer = label_word_dictionary[label]
            elif display_num == 2:
                label_input_required = False
                label = label_list[1]  # Same label as stage 2
                answer = label_word_dictionary[label]
            elif display_num == 3:
                label_input_required = False
                label = label_list[3]  # Same label as stage 4
                answer = label_word_dictionary[label]
            elif display_num == 4:
                label_input_required = False
                label = label_list[2]  # Same label as stage 3
                answer = label_word_dictionary[label]

        rich.print("[bold green]" + answer + "[/bold green]")

        if i < 4:  # Before stage 5
            if label_input_required is True:
                position_list.append(position)
                label_list.append(int(input("What is the label of the button you pressed: ")))
            else:
                label_list.append(label)
                position_list.append(int(input("What is the position of the button you pressed: ")))

    # Function end


def complex_wires(serial_number, parallel_port, battery_num):
    if (int(serial_number[-1]) % 2) != 0 and parallel_port is False and battery_num < 2:  # all false
        answer = "+------+-------+-------+-------+-------+\n" \
                 "|      | White | Red   | Blue  | Both  |\n" \
                 "+======+=======+=======+=======+=======+\n" \
                 "| None | Cut   | Don't | Don't | Don't |\n" \
                 "+------+-------+-------+-------+-------+\n" \
                 "| Star | Cut   | Cut   | Don't | Don't |\n" \
                 "+------+-------+-------+-------+-------+\n" \
                 "| LED  | Don't | Don't | Don't | Don't |\n" \
                 "+------+-------+-------+-------+-------+\n" \
                 "| Both | Don't | Don't | Don't | Don't |\n" \
                 "+------+-------+-------+-------+-------+"
    elif (int(serial_number[-1]) % 2) != 0 and parallel_port is False and battery_num >= 2:  # battery
        answer = "+------+-------+-------+-------+----------+\n" \
                 "|      | White | Red   | Blue  | Both     |\n" \
                 "+======+=======+=======+=======+==========+\n" \
                 "| None | Cut   | Don't | Don't | Don't    |\n" \
                 "+------+-------+-------+-------+----------+\n" \
                 "| Star | Cut   | Cut   | Don't | Don't    |\n" \
                 "+------+-------+-------+-------+----------+\n" \
                 "| LED  | Don't | Cut   | Don't | Don't    |\n" \
                 "+------+-------+-------+-------+----------+\n" \
                 "| Both | Cut   | Cut   | Don't | Don't    |\n" \
                 "+------+-------+-------+-------+----------+"
    elif (int(serial_number[-1]) % 2) != 0 and parallel_port is True and battery_num < 2:  # parallel
        answer = "+------+-------+-------+-------+-------+\n" \
                 "|      | White | Red   | Blue  | Both  |\n" \
                 "+======+=======+=======+=======+=======+\n" \
                 "| None | Cut   | Don't | Don't | Don't |\n" \
                 "+------+-------+-------+-------+-------+\n" \
                 "| Star | Cut   | Cut   | Don't | Cut   |\n" \
                 "+------+-------+-------+-------+-------+\n" \
                 "| LED  | Don't | Don't | Cut   | Don't |\n" \
                 "+------+-------+-------+-------+-------+\n" \
                 "| Both | Don't | Don't | Cut   | Don't |\n" \
                 "+------+-------+-------+-------+-------+"
    # parallel and battery
    elif (int(serial_number[-1]) % 2) != 0 and parallel_port is True and battery_num >= 2:
        answer = "+------+-------+-------+-------+-------+\n" \
                 "|      | White | Red   | Blue  | Both  |\n" \
                 "+======+=======+=======+=======+=======+\n" \
                 "| None | Cut   | Don't | Don't | Don't |\n" \
                 "+------+-------+-------+-------+-------+\n" \
                 "| Star | Cut   | Cut   | Don't | Cut   |\n" \
                 "+------+-------+-------+-------+-------+\n" \
                 "| LED  | Don't | Cut   | Cut   | Don't |\n" \
                 "+------+-------+-------+-------+-------+\n" \
                 "| Both | Cut   | Cut   | Cut   | Don't |\n" \
                 "+------+-------+-------+-------+-------+"
    elif (int(serial_number[-1]) % 2) == 0 and parallel_port is False and battery_num < 2:  # even serial
        answer = "+------+-------+-------+-------+-------+\n" \
                 "|      | White | Red   | Blue  | Both  |\n" \
                 "+======+=======+=======+=======+=======+\n" \
                 "| None | Cut   | Cut   | Cut   | Cut   |\n" \
                 "+------+-------+-------+-------+-------+\n" \
                 "| Star | Cut   | Cut   | Don't | Don't |\n" \
                 "+------+-------+-------+-------+-------+\n" \
                 "| LED  | Don't | Don't | Don't | Cut   |\n" \
                 "+------+-------+-------+-------+-------+\n" \
                 "| Both | Don't | Don't | Don't | Don't |\n" \
                 "+------+-------+-------+-------+-------+"
    # even serial and battery
    elif (int(serial_number[-1]) % 2) == 0 and parallel_port is False and battery_num >= 2:
        answer = "+------+-------+-----+-------+-------+\n" \
                 "|      | White | Red | Blue  | Both  |\n" \
                 "+======+=======+=====+=======+=======+\n" \
                 "| None | Cut   | Cut | Cut   | Cut   |\n" \
                 "+------+-------+-----+-------+-------+\n" \
                 "| Star | Cut   | Cut | Don't | Don't |\n" \
                 "+------+-------+-----+-------+-------+\n" \
                 "| LED  | Don't | Cut | Don't | Cut   |\n" \
                 "+------+-------+-----+-------+-------+\n" \
                 "| Both | Cut   | Cut | Don't | Don't |\n" \
                 "+------+-------+-----+-------+-------+"
    # even serial and parallel
    elif (int(serial_number[-1]) % 2) == 0 and parallel_port is True and battery_num < 2:
        answer = "+------+-------+-------+-------+-------+\n" \
                 "|      | White | Red   | Blue  | Both  |\n" \
                 "+======+=======+=======+=======+=======+\n" \
                 "| None | Cut   | Cut   | Cut   | Cut   |\n" \
                 "+------+-------+-------+-------+-------+\n" \
                 "| Star | Cut   | Cut   | Don't | Cut   |\n" \
                 "+------+-------+-------+-------+-------+\n" \
                 "| LED  | Don't | Don't | Cut   | Cut   |\n" \
                 "+------+-------+-------+-------+-------+\n" \
                 "| Both | Don't | Don't | Cut   | Don't |\n" \
                 "+------+-------+-------+-------+-------+"
    else:  # all
        answer = "+------+-------+-----+-------+-------+\n" \
                 "|      | White | Red | Blue  | Both  |\n" \
                 "+======+=======+=====+=======+=======+\n" \
                 "| None | Cut   | Cut | Cut   | Cut   |\n" \
                 "+------+-------+-----+-------+-------+\n" \
                 "| Star | Cut   | Cut | Don't | Cut   |\n" \
                 "+------+-------+-----+-------+-------+\n" \
                 "| LED  | Don't | Cut | Cut   | Cut   |\n" \
                 "+------+-------+-----+-------+-------+\n" \
                 "| Both | Cut   | Cut | Cut   | Don't |\n" \
                 "------+-------+-----+-------+-------+"
    rich.print("[bold green]" + answer + "[/bold green]")


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

    # return answer
    rich.print("[bold green]" + str(answers_list_3) + "[/bold green]")


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

    # solver
    print("Please select the color of the wire or exit to exit")
    wire_color_list = ["Exit", "Red", "Blue", "Black"]
    answer = ""
    while 1 == 1:
        wire_color = cutie.select(wire_color_list, selected_index=1)
        print("\n")
        if wire_color == 1:
            red += 1
            answer = "Cut the wire if it is connected to " + red_options[red]
        elif wire_color == 2:
            blue += 1
            answer = "Cut the wire if it is connected to " + blue_options[blue]
        elif wire_color == 3:
            black += 1
            answer = "Cut the wire if it is connected to " + black_options[black]
        elif wire_color == 0:
            break
        rich.print("[bold green]" + answer + "[/bold green]")


def morse():  # morse table
    rich.print("[bold green]+-----------------------+--------+-----------+\n"
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
               "+-----------------------+--------+-----------+\n[/bold green]")


def whose_on_first():
    display_word_dictionary = {
        "BLANK": "Middle Right",
        "C": "Top Right",
        "CEE": "Bottom Right",
        "DISPLAY": "Bottom Right",
        "FIRST": "Top Right",
        "HOLD ON": "Bottom Right",
        "LEAD": "Bottom Right",
        "LED": "Middle Left",
        "LEED": "Bottom Left",
        "NO": "Bottom Right",
        "NOTHING": "Middle Left",
        "OKAY": "Top Right",
        "READ": "Middle Right",
        "RED": "Middle Right",
        "REED": "Bottom Left",
        "SAYS": "Bottom Right",
        "SEE": "Bottom Right",
        "THEIR": "Middle Right",
        "THERE": "Bottom Right",
        "THEY ARE": "Middle Left",
        "THEY'RE": "Bottom Left",
        "UR": "Top Left",
        "YES": "Middle Left",
        "YOU": "Middle Right",
        "YOU ARE": "Bottom Right",
        "YOU'RE": "Middle Right",
        "YOUR": "Middle Right",
        "": "Bottom Left"}

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
        corresponding_word = word_corresponding_list[
            input("Please enter the word in the box that is located in the " + displayed_word + " : ").upper()]
        rich.print("[bold green]" + str(corresponding_word) + "[/bold green]")


def symbols():  # todo coment
    file = open(r"Symbols/Symbols_Data.json", "r")
    data = json.load(file)
    NAMES_LIST = data["NAMES_LIST"]
    file.close()
    main_list = []
    symbols_dictionary = {
        1: [28, 13, 30, 12, 7, 9, 23],  # positions of the users selected words based off of the labels of the images
        2: [16, 28, 23, 26, 3, 9, 20],
        3: [1, 8, 26, 5, 15, 30, 3],
        4: [11, 21, 31, 7, 5, 20, 4],
        5: [24, 4, 31, 22, 21, 19, 2],
        6: [11, 16, 27, 14, 24, 18, 6]
    }

    for j in range(6):
        temp_list = []
        dict_list = symbols_dictionary[j + 1]
        for i in range(7):
            num = dict_list[i] - 1
            temp_list.append(NAMES_LIST[num])
        main_list.append(temp_list)
    table_list = [["Sequence 1", "Sequence 2", "Sequence 3", "Sequence 4", "Sequence 5", "Sequence 6"]]
    for j in range(7):
        temp_row = []
        for i in range(6):
            temp = main_list[i]
            temp_row.append(str(temp[j]))
        table_list.append(temp_row)

    table = texttable.Texttable()
    table.set_cols_align(["c", "c", "c", "c", "c", "c"])
    table.set_cols_width([20, 20, 20, 20, 20, 20])
    table.add_rows(table_list)
    table_ouput = table.draw()
    rich.print("[bold green]" + table_ouput + "[/bold green]")


def module_select(serial_number, battery_numbers, parallel, indicator_light_frk,
                  indicator_light_car, all_mazes, display_help):  # function for all of the questions to be asked
    options_list = ["New Bomb", "Wires", "Buttons", "Maze", "Simon says", "Memory", "Complex wires", "Passwords",
                    "Wire Sequences", "Morse", "On The Subject Of Whose First", "Symbols"]
    print("\n \nPlease Select the module you want to solve")

    selection_input = cutie.select(options_list, selected_index=1)
    print("\n")
    help_modules(display_help, selection_input)
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
        elif selection == 11:
            symbols()
        elif selection == 0:
            return True
        else:
            pass


def help_required_function(first_time_asking, help_required):  # function to ask if person is in need of help
    word_dict = {
        True: "",
        False: " still"
    }
    if help_required is True:  # help module
        help_required = cutie.prompt_yes_or_no(
            "Do you" + word_dict[first_time_asking] + " require help(if Yes Type 1): ")

    return help_required


def help_modules(help_required, module):
    help_dictionary = {
        1: "The Wires module (sometimes known as Simple Wires) contains 3-6 wires of different solid "
           "colors.\nWires may be colored in yellow, red, blue, black, or white.\nOnly one of the wires of "
           "the module must be cut in order to disarm the module.\n",

        2: "The Button is a large button of one solid color, a one-word label on it, and a strip to the "
           "right of it that lights up when the button is held.\nThe button must be pressed and released at "
           "the right time based on information on the button, as well as on batteries and some indicators "
           "on the bomb.\n",

        3: "The Maze module is a module that consists of a 6x6 grid of squares with two of the squares "
           "containing green indicator circles,\none square containing a white square, and one square "
           "containing a red triangle as well as four directional buttons around the maze.\nIn order to "
           "disarm the module, the Defuser must guide the white light to the red triangle without running "
           "into any of the walls shown in the manual.\n",

        4: "One of the four colored buttons will flash.\n"
           "Using the table below, press the button with the corresponding color.\n"
           "The original button will flash, followed by another. Repeat this sequence in order using the "
           "color mapping.\n"
           "The sequence will lengthen by one each time you correctly enter a sequence until the module is "
           "disarmed.\n",

        5: "The Memory module features a display with a number from 1-4 and four buttons, with the labels "
           "1-4,\nbut not necessarily in that order. To disarm the module, the defuser must press the "
           "correct buttons to fill the stage indicator five times in a row.\n",

        6: "The Complicated Wires module contains up to six wires arranged vertically with an LED above each "
           "wire and a space for a pencil-drawn ★ below it.\nTo disarm the module, the defuser must cut the "
           "correct wires, in any order, based on instructions laid out below.\n",

        7: "The Password module consists of a five lettered display with arrows above and below them.\nThe "
           "expert must then find a word that has a letter in all five slots.\nOnly one word is present in "
           "the module.\n",

        8: "The Wire Sequence module consists of four panels, each with 1 to 3 wires.\nDepending on the "
           "occurrence number of the wire color and the letter it is connected to,\nthe expert must determine "
           "if each should be cut or not. Wire occurrences are indicated in their order from the left side.\n",

        9: "The Morse Code module consists of a light flashing in Morse Code, a radio with a displayed "
           "frequency and a TX button.\nThe defuser must interpret the flashing Morse Light as dots and "
           "dashes to form a word in Morse Code.\nThis word corresponds to a radio frequency that the expert "
           "must tell the defuser to transmit.\nThe defuser must scroll to that frequency, and press the TX "
           "button to solve the module.\n",

        10: "The aim of the Who's on First module is to press the correct labelled button for three stages.\n"
            "For each stage, the Defuser must read the label of a particular button based on the display.\nThe "
            "Expert then finds a list of words, and the first word on the list is the correct one to press.\n"
    }
    if help_required is True:
        rich.print("[bold red]" + help_dictionary[module] + "[/bold red]")


def main():
    rich.print("[bold]https://www.bombmanual.com/print/KeepTalkingAndNobodyExplodes-BombDefusalManual-v1.pdf"
               "\n Open the pages on symbols\n"
               "Also run the program called [reverse]'Knobs.exe'[/reverse] from the same file this needs to run "
               "separately from the main code.[/bold]\n"
               "Use the arrow keys to navigate the menus.")
    ALL_MAZES = json.load(open("data.json"))

    help_required = help_required_function(True, True)
    serial_number, battery_numbers, parallel, indicator_light_frk, indicator_light_car = data_input()
    module_select(serial_number, battery_numbers, parallel,
                  indicator_light_frk, indicator_light_car, ALL_MAZES, help_required)
    escape = False
    while escape is False:
        try:
            new_bomb = module_select(serial_number, battery_numbers, parallel,
                                     indicator_light_frk, indicator_light_car, ALL_MAZES, help_required)
            if new_bomb is True:
                serial_number, battery_numbers, parallel, indicator_light_frk, indicator_light_car = data_input()

                help_required = help_required_function(False, help_required)

        except:
            rich.print(
                "[reverse]There was an error."
                "\nIf you think there is no error in your input raise an issue at:"
                "\nhttps://github.com/Theproccy/Keep_Typing_And_Nobody_Explodes__/issues/new[/reverse]")


if __name__ == "__main__":
    main()
