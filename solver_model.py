import numpy as np

import gworld as world
import cost_heur_astar as ch_astar
from visualize import *

def get_boundwalls(world):
    h, w = world.get_size()
    bwalls = set()
    for x in range(w):
        bwalls.add( (0,x) )
        bwalls.add( (h-1,x) )
    for y in range(h):
        bwalls.add( (y,0) )
        bwalls.add( (y,w-1) )
    return tuple(bwalls)

class SolverModel:
    def __init__(self, world, visualize = None):
        self.world = world
        self.goal_pos = world.goal_pos
        self.cost_heur = dict()
        self.update_cost_heur()
        self.needs_update = False
        self.vis = visualize

    def update_cost_heur(self):
        agents, goals = self.update_goal_pos()
        start = []
        for agent in agents:
            start.append(self.world.aindx_cpos[agent])
        self.cost_heur = ch_astar.get_costmat(self.world.get_nbor_cells,
                                        goals,
                                        start,
                                        lambda cell: 1,
                                        lambda cell: cell not in self.world.goal_blocked and not self.world.is_blocked(cell[0], cell[1]),
                                        self.cost_heur )
        return self.cost_heur

    def update_goal_pos(self):
        agents = []
        goal_pos = self.goal_pos
        for agent in self.world.get_agents():
            if(self.world.aindx_goalreached[agent]):
                if( self.world.aindx_cpos[agent] in goal_pos ):
                    goal_pos.remove( self.world.aindx_cpos[agent] )
            else:
                agents.append( agent )
        self.goal_pos = goal_pos
        return agents, goal_pos

    def agent_greedy_step(self, agent):
        cpos = self.world.aindx_cpos[agent]
        nbors = self.world.get_nbor_cells(cpos)

        nbor0 = nbors[-1]
        best_nbor = nbor0
        # print self.cost_heur
        min_cost = self.cost_heur[nbor0][0]

        for nbor in nbors:
            if(self.world.passable(nbor) and nbor in self.cost_heur):
                tcost = self.cost_heur[nbor][0]
                if(tcost < min_cost):
                    min_cost = tcost
                    best_nbor = nbor

        nxt_action = self.world.pos_to_action(cpos, best_nbor)
        return best_nbor, nxt_action

    def solve_step(self):
        act_agents, goal_pos = self.update_goal_pos()
        random.shuffle(act_agents)

        for agent in act_agents:

            self.update_goal_pos()

            if (self.needs_update):
                self.update_cost_heur()
                self.needs_update = False

            best_nbor, nxt_action = self.agent_greedy_step(agent)

            self.vis.canvas.update()
            self.vis.canvas.after(100)

            self.world.agent_action(agent, nxt_action)

            if(best_nbor in self.goal_pos):
                self.world.aindx_goalreached[agent] = True
                self.world.goal_blocked.append( best_nbor )

                self.needs_update = True

if __name__ == "__main__":

    a = world.GridWorld(15, 15)

    bwalls = get_boundwalls(a)
    a.add_rocks( bwalls )

    # a.add_rocks( ( (1,1),(3,3),(1,3),(3,1),(2,4) ) )
    # # a.add_agents( ((3,2),(1,6),(7,8),(2,6),(2,8),(5,6),(4,7)) )
    # a.add_agents_rand(7)
    # a.add_goal_pos( ( (2,3),(6,1),(8,7),(6,2),(8,2),(6,5),(7,4) ) )

    a.add_agents_rand(24)
    a.add_goal_pos( ( (3,2),(4,2),(5,2),(2,3),(6,3),(2,4),(6,4), \
                      (3,6),(4,6),(5,6),(6,6),(2,7),(5,7),(3,8),(4,8),(5,8),(6,8), \
                      (3,10),(6,10),(2,11),(4,11),(6,11),(2,12),(5,12) \
                      ) )

    # a.add_agents_rand(27)
    # a.add_goal_pos( ( (2,2),(3,2),(4,2),(3,3),(2,4),(3,4),(4,4), \
    #                   (3,6),(2,7),(3,7),(4,7),(3,8), \
    #                   (2,10),(3,10),(4,10),(3,11),(2,12),(3,12),(4,12),
    #                   (6,2),(6,3),(6,4), (6,6),(6,7),(6,8), (6,10),(6,11),(6,12) \
    #                   ) )

    vis = Visualize(a)

    vis.draw_world()
    vis.draw_agents()

    vis.canvas.pack()
    vis.canvas.update()
    vis.canvas.after(200)

    solver = SolverModel(a, vis)

    break_loop = False
    iter_val = 0

    while (True):
        print 'iter: ', iter_val
        solver.solve_step()

        break_loop = True
        for agent in a.get_agents():
            if (not a.aindx_goalreached[agent]):
                break_loop = False

        vis.canvas.update()
        vis.canvas.after(250)

        if(break_loop):
            break

        iter_val += 1

    vis.canvas.update()
    vis.canvas.after(2500)