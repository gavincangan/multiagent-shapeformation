from macros import *
import numpy as np
import grid_agent as ga

class world:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.occ_map = np.zeros((h, w)) #occupancy map
        self.ptr_map = [[[] for row in range(w)] for row in range(h)]
        self.agents = []
        self.visualize = None

    def add_agent(self, agent_obj, pos_y, pos_x):
        pos_x, pos_y = self.xy_saturate(pos_x, pos_y)
        agent_obj.update_position(pos_y, pos_x)
        print 'Adding: ', str(agent_obj)
        self.agents.append(agent_obj)

    def add_rocks(self, rocks):
        if rocks:
            for rock in rocks:
                rockx, rocky = self.xy_saturate(rock[1], rock[0])
                if( not self.is_blocked(rocky, rockx) ):
                    self.occ_map[rocky][rockx] = IS_ROCK
                    self.ptr_map[rocky][rockx] = tuple()
                else:
                    raise NotImplementedError

    def new_agent(self, pos_row, pos_col):
        agent_obj = ga.DistributedAgent(self, pos_row, pos_col)
        #agent_obj.update_position(self, pos_row, pos_col)
        return agent_obj

    def move_agent(self, agent_obj, move_cmd):
        agent_obj.move(move_cmd)
        raise NotImplementedError

    def rm_agent(self, agent_obj):
        self.agents.remove(agent_obj)

    def get_size(self):
        return (self.h, self.w)

    def is_validpos(self, y, x):
        if x < 0 or x > self.w - 1 or y < 0 or y > self.h - 1:
            return False
        else:
            return True

    def is_blocked(self, y, x):
        # print 'Cell :', y, x
        if not self.is_validpos(y, x): return True
        if(self.occ_map[y][x] == IS_ROCK): return True
        return False

    def xy_saturate(self, x,y):
        if(x<0): x=0
        if(x>self.w-1): x=self.w-1
        if(y<0): y=0
        if(y>self.h-1): y=self.h-1
        return(x, y)

    def occ_map_view(self, y, x, dy, dx):
        # print '$$', x, dx, y, dy
        if(dx < 0):
            x = x + dx
            dx = dx * (-1)
        if(dy < 0):
            y = y + dy
            dy = dy * (-1)
        x1 = x + dx
        y1 = y + dy
        x, y = self.xy_saturate(x, y)
        x1, y1 = self.xy_saturate(x1, y1)
        # print '##', x,x1,y,y1,'\n',self.occ_map, '\n', self.occ_map[y: y1, x :x1], '\n\t#$#'
        return (y, x, y1, x1, self.occ_map[y: y1, x :x1])

    def agents_in_range(self, y1, x1, y2, x2):
        # print(y1, x1, y2, x2)
        x1,y1 = self.xy_saturate(x1, y1)
        x2,y2 = self.xy_saturate(x2, y2)
        if(x2 > x1):
            sx = x1
            bx = x2
        else:
            sx = x2
            bx = x1
        if(y2 > y1):
            sy = y1
            by = y2
        else:
            sy = y2
            by = y1
        # print(sy, sx, by, bx)
        # print(sy, sx, by-sy+1, bx-sx+1)
        ptr_map_range = self.ptr_map[sy: by-sy+1]
        ptr_map_range = [ cells_row[sx:bx-sx+1] for cells_row in ptr_map_range ]
        list_agents = []
        for row in ptr_map_range:
            for cell in row:
                if cell: #is not empty
                    for agent in cell:
                        list_agents.append(agent)
        return list_agents

    def list_all_agents(self):
        return self.agents

    def get_nbors_occ(self, y, x):
        '''
        Return contents of neighbors of given cell
        return: array [ RIGHT, UP, LEFT, DOWN, WAIT ]
        '''
        nbors = np.ones(5, dtype = int ) * INVALID
        # x, y = self.xy_saturate(x, y)
        if(x > 0):
            nbors[MoveActions.LEFT] = self.occ_map[y][x-1]
        if(x < self.w - 1):
            nbors[MoveActions.RIGHT] = self.occ_map[y][x+1]
        if(y > 0):
            nbors[MoveActions.UP] = self.occ_map[y-1][x]
        if(y < self.h - 1):
            nbors[MoveActions.DOWN] = self.occ_map[y+1][x]
        nbors[MoveActions.WAIT] = self.occ_map[y][x]
        return nbors

    def get_nbors_ptr(self, tagent):
        y = tagent.y
        x = tagent.x
        nbors = ( [],[],[],[],[] )
        if(x > 0):
            for agent in self.ptr_map[y][x-1]:
                nbors[MoveActions.LEFT].append(agent)
        if(x < self.w - 1):
            for agent in  self.ptr_map[y][x+1]:
                nbors[MoveActions.RIGHT].append(agent)
        if(y > 0):
            for agent in self.ptr_map[y-1][x]:
                nbors[MoveActions.UP].append(agent)
        if(y < self.h - 1):
            for agent in self.ptr_map[y+1][x]:
                nbors[MoveActions.DOWN].append(agent)
        for agent in self.ptr_map[y][x]:
            nbors[MoveActions.WAIT].append(agent)
        nbors[MoveActions.WAIT].remove(tagent)
        return nbors

    def print_all_agents(self):
        for agent in self.agents:
            print(str(agent))

    def passable(self, y, x):
        if(self.is_blocked(y, x)): return False
        if(self.occ_map[y][x] == UNOCCUPIED):
            return True
        elif(MAX_AGENTS_IN_CELL > 1):
            if( len(self.ptr_map[y][x]) < MAX_AGENTS_IN_CELL ):
                return True
            else:
                return False
        else:
            return False
