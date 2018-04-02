from gworld import *
from visualize import *

def get_m_astar_path(world, start, goal, constraints = None):
    ret_path = m_astar.find_path(world.get_nbor_cells,
              start,
              goal,
              lambda cell: 1,
              lambda cell, constraints : world.passable( cell, constraints ),
              world.yxt_dist_heuristic,
              constraints)
    return ret_path

a = GridWorld(9,9)
a.add_rocks(    [
                (0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),    \
                (9,0),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9),    \
                (1,0),(2,0),(3,0),(4,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                (1,9),(2,9),(3,9),(4,9),(4,9),(5,9),(6,9),(7,9),(8,9)
                ] )
a.add_agents( [ (1,1,3,2), (2,1,2,2) ] )

vis = Visualize(a)

vis.draw_world()
vis.draw_agents()

vis.canvas.pack()
vis.canvas.update()
vis.canvas.after(500)

agents = a.get_agents()

conflict = False

path_maxlen = 0

constraints = []

# cpos = a.aindx_cpos[agent]
# goal = a.aindx_goal[agent]
# start_cell = (cpos[0], cpos[1], 0)
# goal_cell = (goal[0], goal[1], ANY_TIME)

vis.canvas.after(500)

vis.canvas.update()
vis.canvas.after(5000)
