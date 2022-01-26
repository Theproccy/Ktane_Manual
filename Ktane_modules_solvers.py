""" A Library of solvers for the included modules in the game Keep talking nobody explodes"""


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
    :return:
    """

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
    answer = ""
    releasing_held_button = False

    if blue is True and abort is True:
        releasing_held_button = True
    elif number_of_batteries > 1 and detonate is True:
        answer = "Press and Immediately Release"
    elif white is True and car_indicator_light_is_lit is True:
        releasing_held_button = True
    elif frk_indicator_light_is_lit is True and number_of_batteries > 2:
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
