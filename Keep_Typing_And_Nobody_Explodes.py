import json

import cutie
import rich

import ktane_modules_solvers as solvers

# global declare
info_dict = {}
ALL_MAZES = {}


def get_bomb_details():
    prompt_text_start = "Is there a "
    prompt_text_end = " on the bomb: "

    parallel = cutie.prompt_yes_or_no(prompt_text_start + "parallel port" + prompt_text_end)
    frk_light = cutie.prompt_yes_or_no(prompt_text_start + "lit FRK indicator" + prompt_text_end)
    car_light = cutie.prompt_yes_or_no(prompt_text_start + "lit CAR indicator" + prompt_text_end)
    serial_number_input_str = input("Please enter the Serial Number: ")
    batteries = input("Please enter the number of batteries on the bomb: ")

    if batteries.isnumeric() is True:
        batteries = int(batteries)
    else:
        batteries = 0

    serial_number_list = list(serial_number_input_str.upper())

    bomb_details_dict = {
        "parallel": parallel,
        "frk_light": frk_light,
        "car_light": car_light,
        "serial_number_list": serial_number_list,
        "batteries": batteries,
    }
    return bomb_details_dict


def wires_input():
    color_options = ['No more wires', 'red', 'blue', 'black', 'white', ]
    selection = 3
    wires_list = []
    while selection != 0:
        selection = cutie.select(color_options, selected_index=3)
        wires_list.append(color_options[selection])
    return wires_list


def wires():
    label_dict = {
        1: "First",
        2: "Second",
        3: "Third",
        4: "Fourth",
        5: "Fifth",
        6: "Sixth"
    }
    wire_to_cut = solvers.wires(info_dict["serial_number_list"], wires_input())
    print("Cut the " + label_dict[wire_to_cut] + " wire.")


def buttons():
    button_color_list = ["BLUE", "RED", "WHITE", "YELLOW", "BLACK"]  # all color options for the button
    button_label_list = ["Abort", "Detonate", "Hold", "Press"]  # all the label Options for the button
    # Data entry
    color_select = cutie.select(button_color_list)
    label_select = cutie.select(button_label_list)
    # int str conversion
    color = button_color_list[color_select]
    label = button_label_list[label_select]
    # Solving
    push_and_release = solvers.button(info_dict["batteries"],
                                      info_dict["car_light"],
                                      info_dict["frk_light"],
                                      color,
                                      label)

    if push_and_release is False:
        button_indicator_list = ["blue", "yellow", "other"]
        indicator_color_selection = cutie.select(button_indicator_list)
        held_button_number = solvers.button_indicator_color(button_color_list[indicator_color_selection])
        print("Release the button with a " + held_button_number + " in any position")
    else:
        print("Push then immediately release the button")


def maze():
    # data input
    print("All Coordinates are to be entered like so : x,y  (e.g. (3,5) would be 3,5 )"
          "\n Top Left (1,1)")
    green_1_input = input("Please enter the coordinate of the green circle : ")
    green_2_input = input("Please enter the coordinate of the other green circle : ")
    start_position_input = input("Please enter the coordinate of the white dot : ")
    end_position_input = input("Please enter the coordinate of the red triangle : ")
    print("\n")  # quality of life new line

    # Formatting
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
        green_1_temp = green_1.pop(i)
        green_2_temp = green_2.pop(i)

        start_position.insert(i, start_temp - 1)
        end_position.insert(i, end_temp - 1)
        green_1.insert(i, green_1_temp - 1)
        green_2.insert(i, green_2_temp - 1)

    route = solvers.maze(ALL_MAZES, green_1, green_2, start_position, end_position)  # Generates route

    # converts route to instructions
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
    num = 0
    word_num = 1
    temp_list = []
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


def simon_says():
    strikes = int(input("How Many Strikes are there: "))
    color_options = ["red", "blue", "green", "yellow", "Module Completed"]
    module_completed = False
    color_input_list = []
    while module_completed is False:
        print(color_input_list)
        selected_color = cutie.select(color_options, selected_index=1)
        if selected_color == 4:
            break
        else:
            color_string = color_options[selected_color]
            color_input_list.append(color_string)
            color_output_list = solvers.simon_says(info_dict["serial_number_list"], strikes, color_input_list)
            rich.print("[bold green]" + color_output_list + "[/bold green]")


def memory():
    position_list = []
    label_list = []

    for stage in range(5):
        displayed_number = int(input("Please enter the number displayed on the screen of the module: "))
        button_numbers = input(
            "Please enter the numbers on the keys from left to right with a comma separating each value. i.e. '4,2,1,3")
        number_list = list(map(int, button_numbers.split(",")))
        position, label = solvers.memory(displayed_number, position_list, label_list, stage, number_list)
        position_list.append(position)
        label_list.append(label)
        rich.print("[bold green]" + "Press the key labeled '" + str(label) + "'[/bold green]\n")


def complex_wires():
    color_options = ["White", "Red", "Blue", "Both", "Exit"]
    led_star_options = ["None", "Led", "Star", "Both"]
    module_completed = False

    result_dict = {
        0: [False, False],  # White / None
        1: [True, False],  # Red   / Led
        2: [False, True],  # Blue  / Star
        3: [True, True]  # Both  / Both
    }

    while module_completed is False:
        print("\n")  # todo add words (complex wires)
        color_choice = cutie.select(color_options, selected_index=2)

        if color_choice == 4:  # if exit is selected terminate the module
            break

        print("\n")
        led_star_choice = cutie.select(led_star_options, selected_index=2)

        colors = result_dict[color_choice]
        led_star = result_dict[led_star_choice]

        red = colors[0]
        blue = colors[1]
        led = led_star[0]
        star = led_star[1]

        cut_wire = solvers.complex_wires(info_dict["serial_number_list"], info_dict["parallel"], info_dict["batteries"],
                                         red, blue, star, led)

        if cut_wire is True:
            answer = "Cut the wire."
        else:
            answer = "Continue to the next wire."

        rich.print("[bold green]" + answer + "[/bold green]\n")


def passwords():
    first_letter_input = str(
        input("Enter all of the letters in the first column (E.G. aelzx) : "))
    second_letter_input = str(
        input("Enter all of the letters in the Second column (E.G. aelzx) : "))
    third_letter_input = str(
        input("Enter all of the letters in the third column (E.G. aelzx) : "))

    # data formatting
    first_letter_list = list(first_letter_input.strip())
    second_letter_list = list(second_letter_input.strip())
    third_letter_list = list(third_letter_input.strip())
    answers = solvers.passwords(first_letter_list, second_letter_list, third_letter_list)

    rich.print("[bold green] The word is: " + str(answers) + "[/bold green]\n")  # todo fix formatting on answer output


def wire_sequence():
    print("Please select the color of the wire or exit to exit")
    wire_color_list = ["Exit", "Red", "Blue", "Black"]
    color_history_dict = {
        "Red": 0,
        "Blue": 0,
        "Black": 0
    }

    while 1 == 1:
        wire_color = cutie.select(wire_color_list, selected_index=1)
        print("\n")

        if wire_color == 0:  # if exit selected
            break

        answer = solvers.wire_sequences(wire_color_list[wire_color], color_history_dict)

        if answer != "Error":
            color_history_dict[wire_color_list[wire_color]] += 1
        else:
            print("error")  # todo error msg

        rich.print("[bold green] The word is: " + str(answer) + "[/bold green]\n")


def whose_on_first():  # todo add error handling
    i = 0
    while i < 3:
        i += 1
        try:
            button_position = solvers.whose_on_first_step_one(
                input("Please enter the word displayed : ").lower())  # position of button to read
        except LookupError:
            rich.print("[blink]DISPLAYED WORD NOT FOUND!")
            i -= 1
            continue
        try:
            corresponding_word = solvers.whose_on_first_step_two(
                input(
                    "Please enter the word in the box that is located in the " + button_position + " : ").lower())
        except LookupError:
            rich.print("[blink]BUTTON WORD NOT FOUND!")
            i -= 1
            continue

            # word on button to press

        rich.print("[bold green]" + str(corresponding_word) + "[/bold green]")  # output


def morse():
    solved = False
    words = solvers.morse_word_list()
    while solved is False:
        text = input("Please enter as many letters as you have decoded: ")  # input
        text_list = list(text.lower())
        for i in range(len(text_list)):
            words = solvers.morse_smart_sort(text_list[i], words)
            print("Options Remaining :{}".format(words))
        if len(words) == 1:
            solved = True
    rich.print("[bold green] {} [/bold green]".format(solvers.morse_word_to_frequency(words[0].lower())))


def data_load():
    # Data Load
    global ALL_MAZES
    ALL_MAZES = json.load(open("mazes.json"))


def new_bomb():
    global info_dict
    info_dict = get_bomb_details()


def main():
    data_load()
    new_bomb()

    rich.print("[bold]https://www.bombmanual.com/print/KeepTalkingAndNobodyExplodes-BombDefusalManual-v1.pdf"
               "\n Open the pages on symbols\n"
               "Also run the program called [reverse]'Knobs.exe'[/reverse] from the same file this needs to run "
               "separately from the main code.[/bold]\n"
               "Use the arrow keys to navigate the menus.")

    options_list = ["New Bomb", "Wires", "Buttons", "Maze", "Simon says", "Memory", "Complex wires", "Passwords",
                    "Wire Sequences", "Morse", "On The Subject Of Whose First"]  # ,"Symbols"
    while True:
        print("\n \nPlease Select the module you want to solve")
        selection = cutie.select(options_list, selected_index=1)
        print("\n")
        if selection == 1:
            wires()

        elif selection == 2:
            buttons()

        elif selection == 3:
            maze()

        elif selection == 4:
            simon_says()

        elif selection == 5:
            memory()

        elif selection == 6:
            complex_wires()

        elif selection == 7:
            passwords()

        elif selection == 8:
            wire_sequence()

        elif selection == 9:
            morse()

        elif selection == 10:
            whose_on_first()

        elif selection == 11:
            pass  # symbols() TODO

        elif selection == 0:
            new_bomb()


if __name__ == '__main__':
    main()
