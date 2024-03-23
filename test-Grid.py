class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def print_maze(maze, maze_width):
    """Prints the maze in 2D format"""
    for i in range(len(maze)):
        if i % maze_width == 0 and i != 0:
            print()
        print(maze[i], end=' ')
    print()


def astar(maze, start, end, maze_width):
    """Returns a list of positions as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:#, (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Adjacent squares

            # Get node position
            node_position = (current_node.position % maze_width + new_position[1], current_node.position // maze_width + new_position[0])

            # Make sure within range
            if node_position[0] >= maze_width or node_position[0] < 0 or node_position[1] >= len(maze) // maze_width or node_position[1] < 0:
                continue

            # Calculate the index in the flattened maze list
            node_index = node_position[1] * maze_width + node_position[0]

            # Make sure walkable terrain
            if maze[node_index] != ".":
                continue

            # Create new node
            new_node = Node(current_node, node_index)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position % maze_width - end_node.position % maze_width) ** 2) + ((child.position // maze_width - end_node.position // maze_width) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def main():
    maze = [
        ".", ".", ".", ".", "X", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", "X", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", "X", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", "X", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", "X", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", "X", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", "X", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", "X", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
    ]

    maze_width = 10
    start = 0
    end = 76  # (7, 6) in a 10x10 grid

    print("Original Maze:")
    print_maze(maze, maze_width)

    path = astar(maze, start, end, maze_width)
    print(path)
    if path:
        print("\nPath Found:")
        for position in path:
            maze[position] = "*"
        print_maze(maze, maze_width)
    else:
        print("\nNo path found!")


if __name__ == '__main__':
    main()
