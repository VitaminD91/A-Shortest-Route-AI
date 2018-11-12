# A* search
def a_star(graph, start, dest):

    # path is a list of tuples of the form ('node', 'cost')
    frontier.insert([(start, 0)], 0)
    explored = set()

    while not frontier.is_empty():

        # show progress of algorithm
        if visualization:
            visualize(frontier)

        # shortest available path
        path = frontier.remove()

        # frontier contains paths with final node unexplored
        node = path[-1][0]
        g_cost = path[-1][1]
        explored.add(node)

        # goal test:
        if node == dest:
            # return only path without cost
            return [x for x, y in path]

        for neighbor, distance in graph[node]:
            cumulative_cost = g_cost + distance
            f_cost = cumulative_cost + heuristic(neighbor, h)
            new_path = path + [(neighbor, cumulative_cost)]

            # add new_path to frontier
            if neighbor not in explored:
                frontier.insert(new_path, f_cost)

            # update cost of path in frontier
            elif neighbor in frontier._queue:
                frontier.insert(new_path, f_cost)
                print(path)
    return False