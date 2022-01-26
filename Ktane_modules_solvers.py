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
    :return: bool that if True means that the button is a push and immoderately release
    """

    # var creation

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
            temp = mazes[str(i + 1)]

            temp_green_1 = temp["Green_circle_1"]
            temp_green_2 = temp["Green_circle_2"]

            if green_1 == temp_green_1 or green_1 == temp_green_2:
                if green_2 == temp_green_1 or green_2 == temp_green_2:
                    maze_map = temp
    # pathfinding
    route = pathfinder.solve_maze(start_position, start_position, end_position, [], maze_map)

    return route
