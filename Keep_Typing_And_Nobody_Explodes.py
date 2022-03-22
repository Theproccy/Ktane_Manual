import cutie
import rich

import ktane_modules_solvers as solvers


def get_bomb_details():
    prompt_text_start = "Is there a "
    prompt_text_end = " on the bomb"
    parallel = cutie.prompt_yes_or_no(prompt_text_start + "parallel port" + prompt_text_end)
    frk_light = cutie.prompt_yes_or_no(prompt_text_start + "lit FRK indicator" + prompt_text_end)
    car_light = cutie.prompt_yes_or_no(prompt_text_start + "lit CAR indicator" + prompt_text_end)
    serial_number_input_str = input("Please enter the Serial Number")
    batteries = input("Please enter the number of batteries on the bomb")

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
    wires = []
    while selection != 0:
        selection = cutie.select(color_options, selected_index=3)
        wires.append(color_options[selection])
    return wires


def main():
    rich.print("[bold]https://www.bombmanual.com/print/KeepTalkingAndNobodyExplodes-BombDefusalManual-v1.pdf"
               "\n Open the pages on symbols\n"
               "Also run the program called [reverse]'Knobs.exe'[/reverse] from the same file this needs to run "
               "separately from the main code.[/bold]\n"
               "Use the arrow keys to navigate the menus.")

    info_dict = get_bomb_details()
    options_list = ["New Bomb", "Wires", "Buttons", "Maze", "Simon says", "Memory", "Complex wires", "Passwords",
                    "Wire Sequences", "Morse", "On The Subject Of Whose First", "Symbols"]
    while True:
        print("\n \nPlease Select the module you want to solve")
        selection = cutie.select(options_list, selected_index=1)
        if selection == 1:  # wires
            label_dict = {
                1: "First",
                2: "Second",
                3: "Third",
                4: "Fourth",
                5: "Fifth",
                6: "Sixth"
            }
            wire_to_cut = solvers.wires(info_dict, wires_input())
            print("Cut the " + label_dict[wire_to_cut] + " wire.")

        elif selection == 2:
            button_color_list = ["BLUE", "RED", "WHITE", "YELLOW", "BLACK"]  # all color options for the button
            button_label_list = ["Abort", "Detonate", "Hold", "Press"]  # all the label Options for the button

            color_select = cutie.select(button_color_list)
            label_select = cutie.select(button_label_list)

            color = button_color_list[color_select]
            label = button_label_list[label_select]

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
            break
        else:
            pass
