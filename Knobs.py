import rich


def knobs():
    up = ["001011111101", "101010011011"]
    down = ["011001111101", "101010010001"]
    left = ["000010100111", "000010000110"]
    right = ["101111111010", "101100111010"]
    answer = ""
    sequence_input = input(
        "Please enter the sequence of LEDs(E.G. 001011111101)(1 meaning light is on): "
    )
    exit_knobs = False
    if sequence_input == up[0] or sequence_input == up[1]:
        answer = "Up"
    elif sequence_input == down[0] or sequence_input == down[1]:
        answer = "Down"
    elif sequence_input == left[0] or sequence_input == left[1]:
        answer = "Left"
    elif sequence_input == right[0] or sequence_input == right[1]:
        answer = "Right"
    elif sequence_input == "":
        exit_knobs = True
    else:
        answer = "Data was entered wrong try again."
    rich.print("[bold green]" + answer + "[/bold green]")
    return exit_knobs


print(
    "Data entry for the led sequences is done like so:\n"
    "+---+---+---+---+---+---+\n"
    "|   |   | X |   | X | X |\n"
    "+===+===+===+===+===+===+\n"
    "| X | X | X | X |   | X |\n"
    "+---+---+---+---+---+---+\n"
    "Will be entered as : 001011111101\n"
    "Leave blank to exit\n"
)

while True is True:
    knobs()
