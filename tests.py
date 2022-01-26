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
    if Modules.wires(['A', 'L', '5', '0', 'F', '2'], ["white", "white", "white""yellow"]) == 0:
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


print(test_wires())
