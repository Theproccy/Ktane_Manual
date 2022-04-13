""" A Library of solvers for the included modules in the game Keep talking nobody explodes"""

import find_path as pathfinder


def wires(serial_num: list, wire_list: list):  # Module for Simple wires

    """
    args:
    :param serial_num:  List form of the serial number ['A','L','5','0','F','2']
    :param wire_list:   The colors of the of the wires in list form e.g. ['red','blue','black','white']
    :return: A int of the wire to be cut
    """
    # Variable creation
    number_of_yellow_wires = 0
    number_of_red_wires = 0
    number_of_blue_wires = 0
    number_of_black_wires = 0
    number_of_white_wires = 0

    # Data gathering from input
    number_of_wires = len(wire_list)

    # Splits the list in to the number of each wire color
    for i in range(number_of_wires):
        temp = wire_list[i]
        if temp == 'yellow':
            number_of_yellow_wires += 1

        elif temp == 'red':
            number_of_red_wires += 1

        elif temp == 'blue':
            number_of_blue_wires += 1

        elif temp == 'black':
            number_of_black_wires += 1

        elif temp == 'white':
            number_of_white_wires += 1

    # Solver N.B. the if/elif/else statements are not combined when the results have the same outputs due to the fact
    # that multiple statements can be true and so it is necessary to run them in the same order of the manual.
    # todo tidy up this comment.
    answer = ""
    if number_of_wires == 3:
        if number_of_red_wires == 0:
            answer = 1  # "Cut The Second Wire"
        elif wire_list[-1] == 'white':
            answer = 2  # "Cut The Last Wire"
        elif number_of_blue_wires > 1:
            for i in range(number_of_wires):
                temp_num = -1 - i
                temp_wire_color = wire_list[temp_num]
                if temp_wire_color == "blue":
                    answer = 2 - i  # "Cut The Last Blue Wire"
                    break
        else:
            answer = 2  # "Cut Last Wire"

    elif number_of_wires == 4:
        if number_of_red_wires > 1 and (int(serial_num[-1]) % 2 == 0):
            for i in range(number_of_wires):
                temp_num = -1 - i
                temp_wire_color = wire_list[temp_num]
                if temp_wire_color == "red":
                    answer = number_of_wires - i  # "Cut The Last red Wire"
                    break
        elif wire_list[-1] == 'yellow' and number_of_red_wires == 0:
            answer = 0  # "Cut The First Wire"
        elif number_of_blue_wires == 1:
            answer = 0  # "Cut The First Wire"
        elif number_of_yellow_wires > 1:
            answer = 3  # "Cut The Last Wire"
        else:
            answer = 1  # "Cut The Second Wire"

    elif number_of_wires == 5:
        if wire_list[-1] == "black" and int(serial_num[-1]) % 2 != 0:
            answer = 3  # "Cut The Fourth Wire"
        elif number_of_red_wires == 1 and number_of_yellow_wires > 1:
            answer = 0  # "Cut The First Wire"
        elif number_of_black_wires == 0:
            answer = 1  # "Cut The Second Wire"
        else:
            answer = 0  # "Cut The First Wire"

    elif number_of_wires == 6:
        if number_of_yellow_wires == 0 and int(serial_num[-1]) % 2 != 0:
            answer = 2  # "Cut The Third Wire"
        elif number_of_yellow_wires == 1 and number_of_white_wires > 1:
            answer = 3  # "Cut The Fourth Wire"
        elif number_of_red_wires == 0:
            answer = 5  # "Cut The Last Wire"
        else:
            answer = 3  # "Cut The Forth Wire"

    return answer
    # End function


def button(number_of_batteries: int, car_indicator_light_is_lit: bool, frk_indicator_light_is_lit: bool,
           button_color: str, button_label: str):  # The Button
    """
    :param number_of_batteries: The number of batteries on the bomb
    :param car_indicator_light_is_lit: If the CAR indicator light is lit
    :param frk_indicator_light_is_lit: If the FRK indicator light is lit
    :param button_color: The color of the button
    :param button_label: The label on the button
    :return: bool that if True means that the button is a push and Immediately release
    """

    # var creation
    button_color = button_color.lower()
    button_label = button_label.lower()
    # colors
    blue = False
    red = False
    white = False
    yellow = False
    # labels
    abort = False
    detonate = False
    hold = False

    # data formatting
    # colors
    if button_color == "blue":
        blue = True
    elif button_color == "red":
        red = True
    elif button_color == "white":
        white = True
    elif button_color == "yellow":
        yellow = True

        # labels
    if button_label == "abort":
        abort = True
    elif button_label == "detonate":
        detonate = True
    elif button_label == "hold":
        hold = True

    # solving
    # main section
    # If the button is blue and the button says "Abort", hold the button and refer to "Releasing a Held Button".
    if blue is True and abort is True:
        press_and_immediately_release = False
    # If there is more than 1 battery on the bomb and the button says "Detonate", press and immediately release the
    # button.
    elif number_of_batteries > 1 and detonate is True:
        press_and_immediately_release = True
    # If the button is white and there is a lit indicator with label CAR, hold the button and refer to "Releasing a
    # Held Button".
    elif white is True and car_indicator_light_is_lit is True:
        press_and_immediately_release = False
    # If there are more than 2 batteries on the bomb and there is a lit indicator with label FRK, press and
    # immediately release the button.
    elif frk_indicator_light_is_lit is True and number_of_batteries > 2:
        press_and_immediately_release = True
    # If the button is yellow, hold the button and refer to "Releasing a Held Button".
    elif yellow is True:
        press_and_immediately_release = False
    # If the button is red and the button says "Hold", press and immediately release the button.
    elif red is True and hold is True:
        press_and_immediately_release = True
    # If none of the above apply, hold the button and refer to "Releasing a Held Button".
    else:
        press_and_immediately_release = False

    return press_and_immediately_release


def button_indicator_color(color: str):
    held_button_dict = {
        "blue": 4,
        "yellow": 5,
        "other": 1
    }
    return held_button_dict[color]


def maze(mazes: dict, green_1: list, green_2: list, start_position: list,
         end_position: list):  # a pathfinder that calculates moves to complete

    """
    N.B. top left of maze is [0,0] Bottom right is [5,5]
    :param mazes: dictionary of all the mazes ("mazes.json")
    :param green_1: list coordinate of the first green circle e.g. [0,1]
    :param green_2: list coordinate of the second green circle e.g. [5,2]
    :param start_position: list coordinate of the white square e.g. [0,0]
    :param end_position: list coordinate of the red triangle e.g. [5,2]
    :return: list of list coordinate of the coordinates from the start position to the end position
    e.g. [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5]]
    """
    # var creation
    maze_map = {}

    # maze selection
    test = False
    for i in range(9):
        if test is False:
            current_maze = mazes[str(i + 1)]

            temp_green_1 = current_maze["Green_circle_1"]
            temp_green_2 = current_maze["Green_circle_2"]

            if green_1 == temp_green_1 or green_1 == temp_green_2:
                if green_2 == temp_green_1 or green_2 == temp_green_2:
                    maze_map = current_maze
    # pathfinding
    route = pathfinder.solve_maze(start_position, start_position, end_position, [], maze_map)

    return route


# def simon_says_solver():

def simon_says(serial_number: list, strikes: int, colors_list: list):  # simon says module

    """
    :param serial_number: List form of the serial number ['A','L','5','0','F','2']
    :param strikes: Integer of the number of strikes
    :param colors_list: List of colors ["red","blue","green","yellow"]
    :return: List of colors to press in order
    """

    vowels = False
    for i in range(len(serial_number)):
        temp = str(serial_number[i])
        temp = temp.upper()
        if temp == "A" or temp == "E" or temp == "I" or temp == "O" or temp == "U":
            vowels = True
            continue

    if vowels:  # vowel simon says
        if strikes == 0:
            switch_dict = {
                "red": "blue",
                "blue": "red",
                "green": "yellow",
                "yellow": "green"
            }
        elif strikes == 1:
            switch_dict = {
                "red": "yellow",
                "blue": "green",
                "green": "blue",
                "yellow": "red"
            }
        else:
            switch_dict = {
                "red": "green",
                "blue": "red",
                "green": "yellow",
                "yellow": "blue"
            }
    else:  # no vowel simon says
        if strikes == 0:
            switch_dict = {
                "red": "blue",
                "blue": "yellow",
                "green": "green",
                "yellow": "red"
            }
        elif strikes == 1:
            switch_dict = {
                "red": "red",
                "blue": "blue",
                "green": "yellow",
                "yellow": "green"
            }
        else:
            switch_dict = {
                "red": "yellow",
                "blue": "green",
                "green": "blue",
                "yellow": "red"
            }
    answer = []
    for i in range(len(colors_list)):
        temp_color = switch_dict[colors_list[i]]
        answer.append(temp_color)

    return answer


def memory(display_number: int, position_list: list, label_list: list, stage: int, button_number_order: list):
    """
    :param display_number: Integer of the number displayed on the module
    :param position_list: List of previous positions of buttons
    :param label_list: List of previous labels
    :param stage: the current stage
    :param button_number_order: the combination of 4 buttons at the bottom of the module [4,2,3,1]
    :return: both the position and the label int
    """

    position = 0
    label = 0
    if stage == 1:  # Stage 1
        if display_number == 1 or display_number == 2:
            position = 2  # Second position
            label = button_number_order[position - 1]
        elif display_number == 3:
            position = 3  # Third position
            label = button_number_order[position - 1]
        elif display_number == 4:
            position = 4  # Forth position
            label = button_number_order[position - 1]

    elif stage == 2:  # Stage 2
        if display_number == 1:
            label = 4  # Labeled 4
            position = button_number_order.index(label) + 1
        elif display_number == 2 or display_number == 4:
            position = position_list[0]  # Same position as stage 1
            label = button_number_order[position - 1]
        elif display_number == 3:
            position = 1  # First position
            label = button_number_order[position - 1]

    elif stage == 3:  # Stage 3
        if display_number == 1:
            label = label_list[1]  # Same label as stage 2
            position = button_number_order.index(label) + 1
        elif display_number == 2:
            label = label_list[0]  # Same label as stage 1
            position = button_number_order.index(label) + 1
        elif display_number == 3:
            position = 3  # Third position
            label = button_number_order[position - 1]
        elif display_number == 4:
            label = 4  # Labeled 4
            position = button_number_order.index(label) + 1

    elif stage == 4:  # Stage 4
        if display_number == 1:
            position = position_list[0]  # Same position as stage 1
            label = button_number_order[position - 1]
        elif display_number == 2:
            position = 1  # First position
            label = button_number_order[position - 1]
        elif display_number == 3 or display_number == 4:
            position = position_list[1]  # Same position as stage 2
            label = button_number_order[position - 1]

    elif stage == 5:  # Stage 5
        if display_number == 1:
            label = label_list[0]  # Same label as stage 1
            position = button_number_order.index(label) + 1
        elif display_number == 2:
            label = label_list[1]  # Same label as stage 2
            position = button_number_order.index(label) + 1
        elif display_number == 3:
            label = label_list[3]  # Same label as stage 4
            position = button_number_order.index(label) + 1
        elif display_number == 4:
            label = label_list[2]  # Same label as stage 3
            position = button_number_order.index(label) + 1

    else:
        position = 0
        label = 0

    return position, label


def complex_wires(serial_number: list, parallel_port: bool, battery_num: int, red: bool, blue: bool, star: bool,
                  led: bool):
    """
    :param serial_number: List form of the serial number ['A','L','5','0','F','2']
    :param parallel_port: Boolean of whether the bomb has a parallel port
    :param battery_num: Number of battery modules the bomb has
    :param red: if the wire has the red trait
    :param blue: if the wire has the blue trait
    :param star: if the wire has the star trait
    :param led:  if the wire has the led trait
    :return: whether or not the wire should be cut
    """

    both_colors = False
    white = False
    red_only = False
    blue_only = False

    both_led_star = False
    neither_led_star = False
    star_only = False
    led_only = False

    if red is True and blue is True:
        both_colors = True
    elif red is False and blue is False:
        white = True
    elif red is True and blue is False:
        red_only = True
    elif red is False and blue is True:
        blue_only = True

    if star is True and led is True:
        both_led_star = True
    elif star is False and led is False:
        neither_led_star = True
    elif star is True and led is False:
        star_only = True
    elif star is False and led is True:
        led_only = True

    cut = False
    if (int(serial_number[-1]) % 2) != 0 and parallel_port is False and battery_num < 2:  # all false
        if (white is True and led is False) or \
                (red_only is True and star_only is True):
            cut = True

    elif (int(serial_number[-1]) % 2) != 0 and parallel_port is False and battery_num >= 2:  # battery
        if (white is True and led_only is False) or \
                (red_only is True and neither_led_star is False):
            cut = True

    elif (int(serial_number[-1]) % 2) != 0 and parallel_port is True and battery_num < 2:  # parallel
        if (white is True and led is False) or \
                (red_only is True and star_only is True) or \
                (blue_only is True and led is True) or \
                (both_colors is True and star_only is True):
            cut = True

    elif (int(serial_number[-1]) % 2) != 0 and parallel_port is True and battery_num >= 2:  # parallel and battery
        if (white is True and led_only is False) or \
                (red_only is True and neither_led_star is False) or \
                (blue_only is True and led is True) or \
                (both_colors is True and star_only is True):
            cut = True

    elif (int(serial_number[-1]) % 2) == 0 and parallel_port is False and battery_num < 2:  # even serial
        if (star_only is True and blue is False) or \
                (neither_led_star is True) or \
                (both_colors is True and star is False):
            cut = True

    elif (int(serial_number[-1]) % 2) == 0 and parallel_port is False and battery_num >= 2:  # even serial and battery
        if (white is True and led_only is False or both_led_star is True) or \
                (red_only is True) or \
                (blue_only is True and neither_led_star is True) or \
                (both_colors is True and star is False):
            cut = True

    elif (int(serial_number[-1]) % 2) == 0 and parallel_port is True and battery_num < 2:
        if (neither_led_star is True) or \
                (star_only is True and blue_only is False) or \
                (led_only is True and blue is True) or \
                (both_led_star is True and blue_only is True):
            cut = True

    else:  # all
        if (white is True and led_only is False) or \
                (red_only is True) or \
                (blue_only is True and star_only is False) or \
                (both_colors is True and both_led_star is False):
            cut = True

        # all false
        # answer=  "+------+-------+-------+-------+-------+\n" \
        #          "|      | White | Red   | Blue  | Both  |\n" \
        #          "+======+=======+=======+=======+=======+\n" \
        #          "| None | Cut   | Don't | Don't | Don't |\n" \
        #          "+------+-------+-------+-------+-------+\n" \
        #          "| Star | Cut   | Cut   | Don't | Don't |\n" \
        #          "+------+-------+-------+-------+-------+\n" \
        #          "| LED  | Don't | Don't | Don't | Don't |\n" \
        #          "+------+-------+-------+-------+-------+\n" \
        #          "| Both | Don't | Don't | Don't | Don't |\n" \
        #          "+------+-------+-------+-------+-------+"
        # battery
        # answer = "+------+-------+-------+-------+----------+\n" \
        #          "|      | White | Red   | Blue  | Both     |\n" \
        #          "+======+=======+=======+=======+==========+\n" \
        #          "| None | Cut   | Don't | Don't | Don't    |\n" \
        #          "+------+-------+-------+-------+----------+\n" \
        #          "| Star | Cut   | Cut   | Don't | Don't    |\n" \
        #          "+------+-------+-------+-------+----------+\n" \
        #          "| LED  | Don't | Cut   | Don't | Don't    |\n" \
        #          "+------+-------+-------+-------+----------+\n" \
        #          "| Both | Cut   | Cut   | Don't | Don't    |\n" \
        #          "+------+-------+-------+-------+----------+"
        # parallel
        # answer = "+------+-------+-------+-------+-------+\n" \
        #          "|      | White | Red   | Blue  | Both  |\n" \
        #          "+======+=======+=======+=======+=======+\n" \
        #          "| None | Cut   | Don't | Don't | Don't |\n" \
        #          "+------+-------+-------+-------+-------+\n" \
        #          "| Star | Cut   | Cut   | Don't | Cut   |\n" \
        #          "+------+-------+-------+-------+-------+\n" \
        #          "| LED  | Don't | Don't | Cut   | Don't |\n" \
        #          "+------+-------+-------+-------+-------+\n" \
        #          "| Both | Don't | Don't | Cut   | Don't |\n" \
        #          "+------+-------+-------+-------+-------+"
        # parallel and battery
        # answer = "+------+-------+-------+-------+-------+\n" \
        #          "|      | White | Red   | Blue  | Both  |\n" \
        #          "+======+=======+=======+=======+=======+\n" \
        #          "| None | Cut   | Don't | Don't | Don't |\n" \
        #          "+------+-------+-------+-------+-------+\n" \
        #          "| Star | Cut   | Cut   | Don't | Cut   |\n" \
        #          "+------+-------+-------+-------+-------+\n" \
        #          "| LED  | Don't | Cut   | Cut   | Don't |\n" \
        #          "+------+-------+-------+-------+-------+\n" \
        #          "| Both | Cut   | Cut   | Cut   | Don't |\n" \
        #          "+------+-------+-------+-------+-------+"
        # even serial
        # answer = "+------+-------+-------+-------+-------+\n" \
        #          "|      | White | Red   | Blue  | Both  |\n" \
        #          "+======+=======+=======+=======+=======+\n" \
        #          "| None | Cut   | Cut   | Cut   | Cut   |\n" \
        #          "+------+-------+-------+-------+-------+\n" \
        #          "| Star | Cut   | Cut   | Don't | Don't |\n" \
        #          "+------+-------+-------+-------+-------+\n" \
        #          "| LED  | Don't | Don't | Don't | Cut   |\n" \
        #          "+------+-------+-------+-------+-------+\n" \
        #          "| Both | Don't | Don't | Don't | Don't |\n" \
        #          "+------+-------+-------+-------+-------+"
        # even serial and battery
        # answer = "+------+-------+-----+-------+-------+\n" \
        #          "|      | White | Red | Blue  | Both  |\n" \
        #          "+======+=======+=====+=======+=======+\n" \
        #          "| None | Cut   | Cut | Cut   | Cut   |\n" \
        #          "+------+-------+-----+-------+-------+\n" \
        #          "| Star | Cut   | Cut | Don't | Don't |\n" \
        #          "+------+-------+-----+-------+-------+\n" \
        #          "| LED  | Don't | Cut | Don't | Cut   |\n" \
        #          "+------+-------+-----+-------+-------+\n" \
        #          "| Both | Cut   | Cut | Don't | Don't |\n" \
        #          "+------+-------+-----+-------+-------+"
        # even serial and parallel
        # answer = "+------+-------+-------+-------+-------+\n" \
        #          "|      | White | Red   | Blue  | Both  |\n" \
        #          "+======+=======+=======+=======+=======+\n" \
        #          "| None | Cut   | Cut   | Cut   | Cut   |\n" \
        #          "+------+-------+-------+-------+-------+\n" \
        #          "| Star | Cut   | Cut   | Don't | Cut   |\n" \
        #          "+------+-------+-------+-------+-------+\n" \
        #          "| LED  | Don't | Don't | Cut   | Cut   |\n" \
        #          "+------+-------+-------+-------+-------+\n" \
        #          "| Both | Don't | Don't | Cut   | Don't |\n" \
        #          "+------+-------+-------+-------+-------+"
        # all
        # answer = "+------+-------+-----+-------+-------+\n" \
        #          "|      | White | Red | Blue  | Both  |\n" \
        #          "+======+=======+=====+=======+=======+\n" \
        #          "| None | Cut   | Cut | Cut   | Cut   |\n" \
        #          "+------+-------+-----+-------+-------+\n" \
        #          "| Star | Cut   | Cut | Don't | Cut   |\n" \
        #          "+------+-------+-----+-------+-------+\n" \
        #          "| LED  | Don't | Cut | Cut   | Cut   |\n" \
        #          "+------+-------+-----+-------+-------+\n" \
        #          "| Both | Cut   | Cut | Cut   | Don't |\n" \
        #          "------+-------+-----+-------+-------+"
    return cut


def passwords(first_letter_list: list, second_letter_list: list, third_letter_list: list):
    """

    :param first_letter_list: List of all the letters in the first column ["a","e","l","z","x"]
    :param second_letter_list: List of all the letters in the second column ["a","e","l","z","x"]
    :param third_letter_list: List of all the letters in the third column ["a","e","l","z","x"]
    :return: list of possible words ["about","after"] only one will be compatible
    """

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

    return answers_list_3


def wire_sequences(color: str, color_history_dict: dict):  # todo test
    """

    :param color: The color of the wire currently be examined. "red" "blue" "black"
    :param color_history_dict: the number of the wires of that color previously seen. Given in the form
        color_history_dict={
        "red": 0,
        "blue": 3,
        "black": 2
    }
    :return: the terminals that if connect to the wire should be cut. An amended color history dict  todo improve
    """

    red = color_history_dict["red"]
    blue = color_history_dict["blue"]
    black = color_history_dict["black"]

    red_options = {
        1: ["C"],
        2: ["B"],
        3: ["A"],
        4: ["A", "C"],
        5: ["B"],
        6: ["A", "C"],
        7: ["A", "B", "C"],
        8: ["A", "B"],
        9: ["B"]
    }

    blue_options = {
        1: ["B"],
        2: ["A", "C"],
        3: ["B"],
        4: ["A"],
        5: ["B"],
        6: ["B", "C"],
        7: ["C"],
        8: ["A", "C"],
        9: ["A"]
    }

    black_options = {
        1: ["A", "B", "C"],
        2: ["A", "C"],
        3: ["B"],
        4: ["A", "C"],
        5: ["B"],
        6: ["B", "C"],
        7: ["A", "B"],
        8: ["C"],
        9: ["C"]
    }

    # solver
    answer = "Error"

    if color == "red":
        red += 1
        answer = red_options[red]
        color_history_dict["red"] = red
    elif color == "blue":
        blue += 1
        answer = blue_options[blue]
        color_history_dict["blue"] = blue
    elif color == "black":
        black += 1
        answer = black_options[black]
        color_history_dict["black"] = black

    return answer


def morse_sequence_to_word(sequence: str):
    sequence_to_word_dict = {
        ".../...././.-../.-..": "shell",
        "..../.-/.-../.-../...": "halls",
        ".../.-../../.-.-/-.-": "slick",
        "-/.-./../-.-./-.-": "trick",
        "-.../---/-..-/./...": "boxes",
        ".-.././.-/-.-/...": "leaks",
        ".../-/.-./---/-.../.": "strobe",
        "-.../../.../-/.-./---": "bistro",
        "..-./.-../../-.-./-.-": "flick",
        "-.../---/--/-.../...": "bombs",
        "-.../.-././.-/-.-": "break",
        "-.../.-./../-.-./-.-": "brick",
        ".../-/./.-/-.-": "steak",
        ".../-/../-./--.": "string",
        "...-/./-.-./-/---/.-.": "vector",
        "-..././.-/-/...": "beats"
    }
    return sequence_to_word_dict[sequence]


def morse_word_to_frequency(word: str):  # todo
    word_frequency_dict = {
        "shell": 3.505,
        "halls": 3.515,
        "slick": 3.522,
        "trick": 3.532,
        "boxes": 3.535,
        "leaks": 3.542,
        "strobe": 3.545,
        "bistro": 3.552,
        "flick": 3.555,
        "bombs": 3.565,
        "break": 3.572,
        "brick": 3.575,
        "steak": 3.582,
        "string": 3.592,
        "vector": 3.595,
        "beats": 3.600
    }
    return word_frequency_dict[word]


def whose_on_first(step_two=False, displayed_word="", button_word=""):  # todo test
    """
    :param step_two: True if entering the word on the button rather than the display
    :param displayed_word: The word on the display
    :param button_word:  The word on the button in the position indicated
    :return: the location to read from and a list of words to be tried in order
    """

    display_word_dictionary = {
        "blank": "middle right",
        "c": "top right",
        "cee": "bottom right",
        "display": "bottom right",
        "first": "top right",
        "hold on": "bottom right",
        "lead": "bottom right",
        "led": "middle left",
        "leed": "bottom left",
        "no": "bottom right",
        "nothing": "middle left",
        "okay": "top right",
        "read": "middle right",
        "red": "middle right",
        "reed": "bottom left",
        "says": "bottom right",
        "see": "bottom right",
        "their": "middle right",
        "there": "bottom right",
        "they are": "middle left",
        "they're": "bottom left",
        "ur": "top left",
        "yes": "middle left",
        "you": "middle right",
        "you are": "bottom right",
        "you're": "middle right",
        "your": "middle right",
        "": "bottom left"}

    word_corresponding_list = {
        "ready": ["yes", "okay", "what", "middle", "left", "press", "right", "blank", "ready", "no", "first", "uhhh",
                  "nothing", "wait"],
        "first": ["left", "okay", "yes", "middle", "no", "right", "nothing", "uhhh", "wait", "ready", "blank", "what",
                  "press", "first"],
        "no": ["blank", "uhhh", "wait", "first", "what", "ready", "right", "yes", "nothing", "left", "press", "okay",
               "no", "middle"],
        "blank": ["wait", "right", "okay", "middle", "blank", "press", "ready", "nothing", "no", "what", "left", "uhhh",
                  "yes", "first"],
        "nothing": ["uhhh", "right", "okay", "middle", "yes", "blank", "no", "press", "left", "what", "wait", "first",
                    "nothing", "ready"],
        "yes": ["okay", "right", "uhhh", "middle", "first", "what", "press", "ready", "nothing", "yes", "left", "blank",
                "no", "wait"],
        "what": ["uhhh", "what", "left", "nothing", "ready", "blank", "middle", "no", "okay", "first", "wait", "yes",
                 "press", "right"],
        "uhhh": ["ready", "nothing", "left", "what", "okay", "yes", "right", "no", "press", "blank", "uhhh", "middle",
                 "wait", "first"],
        "left": ["right", "left", "first", "no", "middle", "yes", "blank", "what", "uhhh", "wait", "press", "ready",
                 "okay", "nothing"],
        "right": ["yes", "nothing", "ready", "press", "no", "wait", "what", "right", "middle", "left", "uhhh", "blank",
                  "okay", "first"],
        "middle": ["blank", "ready", "okay", "what", "nothing", "press", "no", "wait", "left", "middle", "right",
                   "first", "uhhh", "yes"],
        "okay": ["middle", "no", "first", "yes", "uhhh", "nothing", "wait", "okay", "left", "ready", "blank", "press",
                 "what", "right"],
        "wait": ["uhhh", "no", "blank", "okay", "yes", "left", "first", "press", "what", "wait", "nothing", "ready",
                 "right", "middle"],
        "press": ["right", "middle", "yes", "ready", "press", "okay", "nothing", "uhhh", "blank", "left", "first",
                  "what", "no", "wait"],
        "you": ["sure", "you are", "your", "you're", "next", "uh huh", "ur", "hold", "what?", "you", "uh uh", "like",
                "done", "u"],
        "you are": ["your", "next", "like", "uh huh", "what?", "done", "uh uh", "hold", "you", "u", "you're", "sure",
                    "ur", "you are"],
        "your": ["uh uh", "you are", "uh huh", "your", "next", "ur", "sure", "u", "you're", "you", "what?", "hold",
                 "like", "done"],
        "you're": ["you", "you're", "ur", "next", "uh uh", "you are", "u", "your", "what?", "uh huh", "sure", "done",
                   "like", "hold"],
        "ur": ["done", "u", "ur", "uh huh", "what?", "sure", "your", "hold", "you're", "like", "next", "uh uh",
               "you are", "you"],
        "u": ["uh huh", "sure", "next", "what?", "you're", "ur", "uh uh", "done", "u", "you", "like", "hold", "you are",
              "your"],
        "uh huh": ["uh huh", "your", "you are", "you", "done", "hold", "uh uh", "next", "sure", "like", "you're", "ur",
                   "u", "what?"],
        "uh uh": ["ur", "u", "you are", "you're", "next", "uh uh", "done", "you", "uh huh", "like", "your", "sure",
                  "hold", "what?"],
        "what?": ["you", "hold", "you're", "your", "u", "done", "uh uh", "like", "you are", "uh huh", "ur", "next",
                  "what?", "sure"],
        "done": ["sure", "uh huh", "next", "what?", "your", "ur", "you're", "hold", "like", "you", "u", "you are",
                 "uh uh", "done"],
        "next": ["what?", "uh huh", "uh uh", "your", "hold", "sure", "next", "like", "done", "you are", "ur", "you're",
                 "u", "you"],
        "hold": ["you are", "u", "done", "uh uh", "you", "ur", "sure", "what?", "you're", "next", "hold", "uh huh",
                 "your", "like"],
        "sure": ["you are", "done", "like", "you're", "you", "hold", "uh huh", "ur", "sure", "u", "what?", "next",
                 "your", "uh uh"],
        "like": ["you're", "next", "u", "ur", "hold", "done", "uh uh", "what?", "uh huh", "you", "like", "sure",
                 "you are", "your"]
    }
    button_read_location = ""
    corresponding_word = ""
    if step_two is False:
        button_read_location = display_word_dictionary[displayed_word]
    else:
        corresponding_word = word_corresponding_list[button_word]

    return button_read_location, corresponding_word
