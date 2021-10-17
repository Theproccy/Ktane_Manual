def solve_maze(start_coordinates: list[int],
               current_coordinates: list[int],
               end_coordinates: list[int],
               explored_coordinates: list,
               maze: dict) -> list:

    """This will find a path to solve the maze.
    Args:
        start_coordinates (list[list[int]]): the starting position of the player
        current_coordinates (list[list[int]]): the current position which is used for recursion
        end_coordinates (list[list[int]]): the destination position
        explored_coordinates (list): a list of cords which has been travelled by the code
        maze (dict): a dictionary with all the info about the maze that
    Returns:
        list: contains a list of coordinates which is the path from the start to end
    """

    if current_coordinates == end_coordinates:  # check if we have reached the destination
        return [current_coordinates]
    elif current_coordinates in explored_coordinates:  # check if we have explored the cord
        pass
    else:
        explored_coordinates.append(current_coordinates)

        # check if we can move to top of the current box
        if current_coordinates[1] >= 1:
            if not (maze["horizontal_wall"][current_coordinates[1] - 1][current_coordinates[0]]):
                answer_list = solve_maze(start_coordinates,
                                         [current_coordinates[0], current_coordinates[1] - 1],
                                         end_coordinates,
                                         explored_coordinates,
                                         maze)

                if answer_list and start_coordinates == current_coordinates:
                    answer_list.append(current_coordinates)
                    return answer_list[::-1]

                elif answer_list:
                    answer_list.append(current_coordinates)
                    return answer_list

        # check if we can move to bottom of the current box
        if current_coordinates[1] < 5:
            if not (maze["horizontal_wall"][current_coordinates[1]][current_coordinates[0]]):
                answer_list = solve_maze(start_coordinates,
                                         [current_coordinates[0], current_coordinates[1] + 1],
                                         end_coordinates,
                                         explored_coordinates,
                                         maze)

                if answer_list and start_coordinates == current_coordinates:
                    answer_list.append(current_coordinates)
                    return answer_list[::-1]

                elif answer_list:
                    answer_list.append(current_coordinates)
                    return answer_list

        # check if we can move to left of the current box
        if current_coordinates[0] >= 1:
            if not (maze["vertical_wall"][current_coordinates[1]][current_coordinates[0] - 1]):
                answer_list = solve_maze(start_coordinates,
                                         [current_coordinates[0] - 1, current_coordinates[1]],
                                         end_coordinates,
                                         explored_coordinates,
                                         maze)

                if answer_list and start_coordinates == current_coordinates:
                    answer_list.append(current_coordinates)
                    return answer_list[::-1]

                elif answer_list:
                    answer_list.append(current_coordinates)
                    return answer_list

        # check if we can move to right of the current box
        if current_coordinates[0] < 5:
            if not (maze["vertical_wall"][current_coordinates[1]][current_coordinates[0]]):
                answer_list = solve_maze(start_coordinates,
                                         [current_coordinates[0] + 1, current_coordinates[1]],
                                         end_coordinates,
                                         explored_coordinates,
                                         maze)

                if answer_list and start_coordinates == current_coordinates:
                    answer_list.append(current_coordinates)
                    return answer_list[::-1]

                elif answer_list:
                    answer_list.append(current_coordinates)
                    return answer_list
