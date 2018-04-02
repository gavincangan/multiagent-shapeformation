from macros import *
import numpy as np
import grid_agent as ga
from world import world
from visualize import Visualize

if __name__ == "__main__":
    not_my_home = world(6,6)
    not_my_home.new_agent(3,4)
    my_agent = not_my_home.new_agent(4,2)
    not_my_home.new_agent(2,1)
    not_my_home.new_agent(3,2)
    all_agents = not_my_home.list_all_agents()
    agents_in_range = not_my_home.agents_in_range(0, 3, 3, 0)
    for agent in agents_in_range:
        print agent
    my_agent.broadcast_msg(0x7)

    for agent in all_agents:
        print str(agent)

    # root = Tk()
    # canvas = Canvas(root, width=400, height=400)
    # canvas.grid()
    # root.mainloop()

    vis = Visualize(not_my_home)
    vis.draw_world()
    vis.draw_agents()
    # vis.do_loop()
    vis.canvas.pack()
    vis.canvas.update()
    vis.canvas.after(2000)

    print '\n\n'
    for agent in all_agents:
        print str(agent)

    my_agent.move(MoveActions.UP)
    vis.canvas.update()

    print '\n\n'
    for agent in all_agents:
        print str(agent)

    vis.canvas.after(2000)
    my_agent.move(MoveActions.UP)
    vis.canvas.update()
    vis.canvas.after(2000)

    my_agent.move(MoveActions.LEFT)
    vis.canvas.update()
    vis.canvas.after(2000)

    my_agent.move(MoveActions.LEFT)
    vis.canvas.update()
    vis.canvas.after(2000)

    my_agent.move(MoveActions.LEFT)
    vis.canvas.update()
    vis.canvas.after(2000)

    my_agent.move(MoveActions.DOWN)
    vis.canvas.update()
    vis.canvas.after(2000)

    my_agent.move(MoveActions.RIGHT)
    vis.canvas.update()
    vis.canvas.after(2000)

    my_agent.move(MoveActions.RIGHT)
    vis.canvas.update()
    vis.canvas.after(2000)

    my_agent.move(MoveActions.RIGHT)
    vis.canvas.update()
    vis.canvas.after(2000)

    for agent in all_agents:
        print str(agent)
    print("Hello")
