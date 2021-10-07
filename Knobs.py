def knobs():
    up = ["001011111101", "101010011011"]
    down = ["011001111101", "101010010001"]
    left = ["000010100111", "000010000110"]
    right = ["101111111010", "101100111010"]

    sequence_input = input("Please enter the sequence of LEDs(E.G. 001011111101)(1 meaning light is on): ")
    exit_knobs = True
    if sequence_input == up[0] or sequence_input == up[1]:
        print("Up")
    elif sequence_input == down[0] or sequence_input == down[1]:
        print("Down")
    elif sequence_input == left[0] or sequence_input == left[1]:
        print("Left")
    elif sequence_input == right[0] or sequence_input == right[1]:
        print("Right")
    elif sequence_input == "":
        exit_knobs = True
    else:
        print("Data was entered wrong try again.")
    return exit_knobs


print("Data entry for the led sequences is done like so:\n"
      "+---+---+---+---+---+---+\n"
      "|   |   | X |   | X | X |\n"
      "+===+===+===+===+===+===+\n"
      "| X | X | X | X |   | X |\n"
      "+---+---+---+---+---+---+\n"
      "Will be entered as : 001011111101\n"
      "Leave blank to exit\n")

exit_ = False
while exit_ is False:
    exit_ = knobs()
