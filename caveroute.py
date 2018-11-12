import sys

class Cavern():

    def __init__(self, parent=None, x=None, y=None):
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0
        self.x = x
        self.y = y
        self.connections = []

    def __eq__(self, other):
        return self.x == other.x & self.y == other.y


def astar(maze, start, end):

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

        open_list.pop(current_index)
        closed_list.append(current_node)


        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range 
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(current_node, node_position)

            children.append(new_node)

        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def get_cave_string():
    filename = sys.argv[1] + ".cav"
    f = open(filename, 'r')
    cave_string = f.read()
    f.close()
    return cave_string

def main():
    # 7,2,8,3,2,14,5,7,6,11,2,11,6,14,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0
    cave_string = get_cave_string()
    cave_string_split = cave_string.split(',') 
    cavern_count = cave_string_split[0]
    cavern_coords = cave_string_split[1:2 * int(cavern_count)+1]
    cavern_connections = cave_string_split[len(cavern_coords) + 1:len(cave_string_split)]

    caverns = []
    for i in range(0, len(cavern_coords), 2):
        cavern = Cavern(None, cavern_coords[i], cavern_coords[i + 1])
        caverns.append(cavern)

    for cavern in caverns:
        print("cavern at coords " + cavern.x + "," + cavern.y)
    

    




if __name__ == '__main__':
    main()