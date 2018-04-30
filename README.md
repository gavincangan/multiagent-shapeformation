#Implementation of Multi-Agent Shape Formation in a gridworld simulation.
-Agents are initialized at random positions in the gridworld.
-Run a reverse search to get the cost from any cell to the nearest goal cell
-Uses a modified version of A* search in reverse from all goal positions until
all start positions are covered.
-Each agent greedily moves towards its nearest goal position
-When an agent reaches a goal position, the any other agent that was trying to
reach this point has to find another goal position now.
-So the search process is repeated, and the cost table is updated
-Because the order of planning can have an impact on the time taken by the
solution, the planning sequence is randomized at each step.
-The reverse search can be thought of as a virtual exploration, with the added
benefit of being guided by a heuristic, that is the manhattan distance heuristic that
A* uses.
-However, because there is no actual motion during this search process, it is not
equivalent to learning to cooperate in a task.
-To execute: run solver_model.py
-Link to YouTube video: https://youtu.be/DCipbUKtsTM
