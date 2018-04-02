from macros import *
import numpy as np
import random
import grid_agent as ga
from world import world
from visualize import Visualize

class Experiment:
    def __init__(self, world_dim, nagents, agent_xy):
        self.world = world(world_dim[1], world_dim[0])
        self.vis = Visualize(self.world)
        self.list_agents = []
        for index in range(nagents):
            self.list_agents.append(self.world.new_agent(agent_xy[index][1], agent_xy[index][0]))

    def init_vis(self):
        self.vis.draw_world()
        self.vis.draw_agents()
        self.vis.canvas.pack()
        self.vis.canvas.update()

    def run_random(self, ts, T):
        nsteps = int(T/ts)
        nagents = len(self.list_agents)
        for step in range(nsteps):
            random.shuffle(self.list_agents)
            for agent in self.list_agents:
                agent.move(random.choice(agent.get_move_actions()))
                agent.observe_quadrant(random.choice(agent.get_obs_actions()))
                agent.broadcast_msg(random.choice(agent.comm_actions))
                self.vis.canvas.update()
                self.vis.canvas.after(int((ts * 900) /nagents))
            print '\n'
            for agent in self.list_agents:
                print agent
            print '\n\n'
            self.vis.canvas.after(int(ts * 100))

if __name__ == "__main__":

    my_exp = Experiment( (10,10), 7, ((3,2),(1,6),(7,8),(2,6),(0,9),(5,6),(4,7)) )
    my_exp.world.add_rocks( ( (1,1),(3,3),(1,3),(3,1),(2,0),(2,4) ) )

    # my_exp = Experiment( (5,5), 6, ((3,2),(1,2),(2,4),(0,4),(3,0),(4,4)) )
    # my_exp.world.add_rocks( ( (1,1),(3,3),(1,3),(3,1),(2,0),(2,4) ) )

    my_exp.init_vis()
    my_exp.run_random(2, 100)
