import json

import Ktane_modules_solvers as Modules


# todo clean up
def test_wires():
    three_wire_tests_passed = []
    four_wire_tests_passed = []
    five_wire_tests_passed = []
    six_wire_tests_passed = []

    # three wire tests
    if Modules.wires(['A', 'L', '5', '0', 'F', '2'], ["white", "white", "white"]) == 1:
        # If there are no red wires, cut the second wire.
        three_wire_tests_passed.append(True)
    else:
        three_wire_tests_passed.append(False)
    if Modules.wires(['A', 'L', '5', '0', 'F', '2'], ["red", "white", "white"]) == 2:
        # Otherwise, if the last wire is white, cut the last wire.
        three_wire_tests_passed.append(True)
    else:
        three_wire_tests_passed.append(False)
    if Modules.wires(['A', 'L', '5', '0', 'F', '2'], ["blue", "blue", "red"]) == 1:
        # Otherwise, if there is more than one blue
        # wire, cut the last blue wire.
        three_wire_tests_passed.append(True)
    else:
        three_wire_tests_passed.append(False)
    if Modules.wires(['A', 'L', '5', '0', 'F', '2'], ["red", "white", "blue"]) == 2:
        # Otherwise, cut the last wire.
        three_wire_tests_passed.append(True)
    else:
        three_wire_tests_passed.append(False)

    # four wire
    if Modules.wires(['A', 'L', '5', '0', 'F', '1'], ["red", "red", "white", "white"]) == 1:
        # If there is more than one red wire and the last digit of the serial number is odd, cut the last red wire.
        four_wire_tests_passed.append(True)
    else:
        four_wire_tests_passed.append(False)

    if Modules.wires(['A', 'L', '5', '0', 'F', '2'], ["white", "white", "white", "yellow"]) == 0:
        # Otherwise, if the last wire is yellow and
        # there are no red wires, cut the first wire.
        four_wire_tests_passed.append(True)
    else:
        four_wire_tests_passed.append(False)
    if Modules.wires(['A', 'L', '5', '0', 'F', '2'], ["white", "white", "blue", "white"]) == 0:
        # Otherwise, if there is exactly one blue wire, cut the first wire.
        four_wire_tests_passed.append(True)
    else:
        four_wire_tests_passed.append(False)
    if Modules.wires(['A', 'L', '5', '0', 'F', '2'], ["white", "yellow", "yellow", "white"]) == 3:
        # Otherwise, if there is more than one yellow
        # wire, cut the last wire.
        four_wire_tests_passed.append(True)
    else:
        four_wire_tests_passed.append(False)
    if Modules.wires(['A', 'L', '5', '0', 'F', '2'], ["white", "white", "white", "white"]) == 1:
        # Otherwise, cut the second wire.
        four_wire_tests_passed.append(True)
    else:
        four_wire_tests_passed.append(False)

    # five wire
    if Modules.wires(['A', 'L', '5', '0', 'F', '1'], ["white", "white", "white", "white", "black"]) == 3:
        # If the last wire is black and the last digit of the serial number is odd, cut the fourth wire.
        five_wire_tests_passed.append(True)
    else:
        five_wire_tests_passed.append(False)
    if Modules.wires(['A', 'L', '5', '0', 'F', '2'], ["yellow", "yellow", "red", "white", "white"]) == 0:
        # Otherwise, if there is exactly one red wire and there is more than one yellow wire, cut the first wire.
        five_wire_tests_passed.append(True)
    else:
        five_wire_tests_passed.append(False)
    if Modules.wires(['A', 'L', '5', '0', 'F', '2'], ["white", "white", "white", "white", "white"]) == 1:
        # Otherwise, if there are no black wires, cut the second wire.
        five_wire_tests_passed.append(True)
    else:
        five_wire_tests_passed.append(False)
    if Modules.wires(['A', 'L', '5', '0', 'F', '2'], ["white", "white", "black", "white", "white"]) == 0:
        # Otherwise, cut the first wire.
        five_wire_tests_passed.append(True)
    else:
        five_wire_tests_passed.append(False)

    # 6 wires
    if Modules.wires(['A', 'L', '5', '0', 'F', '1'], ["white", "white", "white", "white", "white", "white"]) == 2:
        # If there are no yellow wires and the last digit of the serial number is odd, cut the third wire.
        six_wire_tests_passed.append(True)
    else:
        six_wire_tests_passed.append(False)
    if Modules.wires(['A', 'L', '5', '0', 'F', '2'], ["white", "yellow", "white", "white", "white", "white"]) == 3:
        # Otherwise, if there is exactly one yellow wire and there is more than one white wire, cut the fourth wire.
        six_wire_tests_passed.append(True)
    else:
        six_wire_tests_passed.append(False)
    if Modules.wires(['A', 'L', '5', '0', 'F', '2'], ["white", "white", "white", "white", "white", "white"]) == 5:
        # Otherwise, if there are no red wires, cut the last wire.
        six_wire_tests_passed.append(True)
    else:
        six_wire_tests_passed.append(False)
    if Modules.wires(['A', 'L', '5', '0', 'F', '2'], ["white", "white", "white", "red", "white", "white"]) == 3:
        # Otherwise, cut the fourth wire.
        six_wire_tests_passed.append(True)
    else:
        six_wire_tests_passed.append(False)

    return three_wire_tests_passed, four_wire_tests_passed, five_wire_tests_passed, six_wire_tests_passed


def test_button():
    button_tests_passed = []
    if not Modules.button(number_of_batteries=0, car_indicator_light_is_lit=False, frk_indicator_light_is_lit=False,
                          button_color="blue", button_label="abort"):
        # If the button is blue and the button says "Abort", hold the button and refer to "Releasing a Held Button".
        button_tests_passed.append(True)
    else:
        button_tests_passed.append(False)
    if Modules.button(number_of_batteries=2, car_indicator_light_is_lit=False, frk_indicator_light_is_lit=False,
                      button_color="red", button_label="detonate"):
        # If there is more than 1 battery on the bomb and the button says "Detonate", press and immediately release
        # the button.
        button_tests_passed.append(True)
    else:
        button_tests_passed.append(False)
    if not Modules.button(number_of_batteries=0, car_indicator_light_is_lit=True, frk_indicator_light_is_lit=False,
                          button_color="white", button_label="detonate"):
        # If the button is white and there is a lit indicator with label CAR, hold the button and refer to "Releasing
        # a Held Button".
        button_tests_passed.append(True)
    else:
        button_tests_passed.append(False)
    if Modules.button(number_of_batteries=3, car_indicator_light_is_lit=False, frk_indicator_light_is_lit=True,
                      button_color="white", button_label="detonate"):
        # If there are more than 2 batteries on the bomb and there is a lit indicator with label FRK, press and
        # immediately release the button.
        button_tests_passed.append(True)
    else:
        button_tests_passed.append(False)
    if not Modules.button(number_of_batteries=0, car_indicator_light_is_lit=False, frk_indicator_light_is_lit=False,
                          button_color="yellow", button_label="detonate"):
        # If the button is yellow, hold the button and refer to "Releasing a Held Button".
        button_tests_passed.append(True)
    else:
        button_tests_passed.append(False)
    if Modules.button(number_of_batteries=0, car_indicator_light_is_lit=False, frk_indicator_light_is_lit=False,
                      button_color="red", button_label="hold"):
        # If the button is red and the button says "Hold", press and immediately release the button.
        button_tests_passed.append(True)
    else:
        button_tests_passed.append(False)
    if not Modules.button(number_of_batteries=0, car_indicator_light_is_lit=False, frk_indicator_light_is_lit=False,
                          button_color="white", button_label="detonate"):
        # If none of the above apply, hold the button and refer to "Releasing a Held Button".
        button_tests_passed.append(True)
    else:
        button_tests_passed.append(False)
    return button_tests_passed


def test_maze():
    maze_test_passed = {}
    maze_results = {
        '1': [[0, 0], [1, 0], [2, 0], [2, 1], [1, 1], [1, 2], [2, 2], [2, 3], [3, 3], [3, 2], [4, 2], [5, 2], [5, 3],
              [5, 4], [5, 5]],

        '2': [[0, 0], [1, 0], [1, 1], [0, 1], [0, 2], [0, 3], [1, 3], [1, 2], [2, 2], [2, 1], [3, 1], [3, 0], [4, 0],
              [4, 1], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]],

        '3': [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [1, 4], [1, 3], [1, 2], [0, 2], [0, 3], [0, 4],
              [0, 5], [1, 5], [2, 5], [3, 5], [3, 4], [3, 3], [3, 2], [4, 2], [4, 3], [4, 4], [4, 5], [5, 5]],

        '4': [[0, 0], [1, 0], [1, 1], [1, 2], [2, 2], [2, 1], [3, 1], [4, 1], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]],

        '5': [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1], [0, 2], [1, 2], [1, 3],
              [2, 3], [3, 3], [3, 4], [2, 4], [1, 4], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5]],

        '6': [[0, 0], [0, 1], [0, 2], [0, 3], [1, 3], [1, 4], [0, 4], [0, 5], [1, 5], [2, 5], [3, 5], [3, 4], [3, 3],
              [3, 2], [3, 1], [4, 1], [4, 0], [5, 0], [5, 1], [5, 2], [4, 2], [4, 3], [4, 4], [5, 4], [5, 5]],

        '7': [[0, 0], [1, 0], [2, 0], [3, 0], [3, 1], [4, 1], [4, 0], [5, 0], [5, 1], [5, 2], [4, 2], [4, 3], [3, 3],
              [2, 3], [2, 4], [3, 4], [4, 4], [4, 5], [5, 5]],

        '8': [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5]],

        '9': [[0, 0], [0, 1], [0, 2], [1, 2], [1, 1], [1, 0], [2, 0], [3, 0], [4, 0], [4, 1], [4, 2], [3, 2], [3, 3],
              [2, 3], [2, 4], [2, 5], [3, 5], [3, 4], [4, 4], [4, 5], [5, 5]]
    }

    green_coordinates_1 = {
        "1": [0, 1],
        "2": [4, 1],
        "3": [3, 3],
        "4": [0, 0],
        "5": [4, 2],
        "6": [4, 0],
        "7": [1, 0],
        "8": [3, 0],
        "9": [2, 1]

    }
    green_coordinates_2 = {
        "1": [5, 2],
        "2": [1, 3],
        "3": [5, 3],
        "4": [0, 3],
        "5": [4, 2],
        "6": [2, 4],
        "7": [1, 5],
        "8": [2, 3],
        "9": [0, 4]
    }
    ALL_MAZES = json.load(open("mazes.json"))
    for num in range(9):
        current_number = str(num + 1)
        if Modules.maze(mazes=ALL_MAZES, green_1=green_coordinates_1[current_number],
                        green_2=green_coordinates_2[current_number], start_position=[0, 0],
                        end_position=[5, 5]) == maze_results[current_number]:
            maze_test_passed["Maze " + current_number] = True
        else:
            maze_test_passed["Maze " + current_number] = False
    return maze_test_passed


def test_simon_says():  # todo fill out
    temp = Modules.simon_says(serial_number=['A', '0', '0', '0', '0', '0'], strikes=0,
                              colors_list=["red", "blue", "green", "yellow"])
    return temp


# print(test_wires())
# print(test_button())
# print(test_maze())
print(test_simon_says())
