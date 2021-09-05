def solve_maze(start_coordinates: list[int], current_coordinates: list[int],
               end_coordinates: list[int],
               explored_coordinates: list, maze: dict) -> list:
    """this will find a path to solve the maze.
    Args:
        start_coordinates (list[list[int]]): the starting pos of the player
        current_coordinates (list[list[int]]): the current pos which is used for recursion
        end_coordinates (list[list[int]]): the destination pos
        explored_coordinates (list): a list of cords which has been travelled by the code
        maze (dict): a dict with all the info about the maze that
    Returns:
        list: contains a list of cords which is the path from the start to end
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
                ans = solve_maze(start_coordinates, [current_coordinates[0], current_coordinates[1] - 1],
                                 end_coordinates, explored_coordinates, maze)
                if ans and start_coordinates == current_coordinates:
                    ans.append(current_coordinates)
                    return ans[::-1]
                elif ans:
                    ans.append(current_coordinates)
                    return ans

        # check if we can move to bottom of the current box
        if current_coordinates[1] < 5:
            if not (maze["horizontal_wall"][current_coordinates[1]][current_coordinates[0]]):
                ans = solve_maze(start_coordinates, [current_coordinates[0], current_coordinates[1] + 1],
                                 end_coordinates, explored_coordinates, maze)
                if ans and start_coordinates == current_coordinates:
                    ans.append(current_coordinates)
                    return ans[::-1]
                elif ans:
                    ans.append(current_coordinates)
                    return ans

        # check if we can move to left of the current box
        if current_coordinates[0] >= 1:
            if not (maze["vertical_wall"][current_coordinates[1]][current_coordinates[0] - 1]):
                ans = solve_maze(start_coordinates, [current_coordinates[0] - 1, current_coordinates[1]],
                                 end_coordinates, explored_coordinates, maze)
                if ans and start_coordinates == current_coordinates:
                    ans.append(current_coordinates)
                    return ans[::-1]
                elif ans:
                    ans.append(current_coordinates)
                    return ans

        # check if we can move to right of the current box
        if current_coordinates[0] < 5:
            if not (maze["vertical_wall"][current_coordinates[1]][current_coordinates[0]]):
                ans = solve_maze(start_coordinates, [current_coordinates[0] + 1, current_coordinates[1]],
                                 end_coordinates, explored_coordinates, maze)
                if ans and start_coordinates == current_coordinates:
                    ans.append(current_coordinates)
                    return ans[::-1]
                elif ans:
                    ans.append(current_coordinates)
                    return ans
