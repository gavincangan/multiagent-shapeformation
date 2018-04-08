import pqueue

INSANE_HIGH = 1000

def manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def least_dist_to_b(a, b):
    min_dist = manhattan_dist(a, b[0])
    for _b in b:
        temp_dist = manhattan_dist(a, _b)
        if(temp_dist < min_dist):
            min_dist = temp_dist
    return min_dist

def all_b_in_a(a, b):
    returnVal = True
    for _b in b:
        if(_b not in a):
            returnVal = False
    return returnVal

def get_costmat(neighbour_fn,
              start,
              end,
              cost = lambda pos: 1,
              passable = lambda pos: True,
              costs = 0,
              heuristic = least_dist_to_b,
              stopCondOr = lambda x=0: False,
              stopCondAnd = lambda x=0: True
              ):

    # tiles to check (tuples of (x, y), cost)
    todo = pqueue.PQueue()

    for start_pos in start:
        todo.update(start_pos, 0)

    # for end_pos in end:
    #     todo.update(end_pos, 1000)

    # tiles we've been to
    visited = set()

    # associated G and H costs for each tile (tuples of G, H)
    if(not costs):
        costs = dict()
    for start_pos in start:
        costs[start_pos] = (0, least_dist_to_b(start_pos, end))

    # parents for each tile
    parents = {}

    # while ( ( (todo and ( all_b_in_a(visited, end) ) ) and stopCondAnd()) or stopCondOr()):
    while ((todo and stopCondAnd()) or stopCondOr()):
        cur, c = todo.pop_smallest()

        visited.add(cur)
        # check neighbours
        nbors = neighbour_fn(cur)
        for n in nbors:
            # skip it if we've already checked it, or if it isn't passable
            if ((n in visited) or
                (not passable(n))):
                continue

            if not (n in todo):
                # we haven't looked at this tile yet, so calculate its costs
                g = costs[cur][0] + cost(cur)
                h = heuristic(n, end)
                costs[n] = (g, h)
                parents[n] = cur
                todo.update(n, g + h)
            else:
                # if we've found a better path, update it
                g, h = costs[n]
                new_g = costs[cur][0] + cost(cur)
                if new_g < g:
                    g = new_g
                    todo.update(n, g + h)
                    costs[n] = (g, h)
                    parents[n] = cur

    return costs
