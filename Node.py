import numpy as np
import copy

class Node(object):
    """
    
    a Node represents a state in the *game tree*. 
    
    evaluating a sequence of nodes, all the way to
    the terminal node, is a *playout*.
    
    once fully instantiated, each Node will know
    its parent and children. terminal Nodes will
    contain payouts/utility values.
    
    only nodes that spawn a playout can be marked
    as visited.
    """
    
    def __init__(self, name, reward=None):
        self.name = name
        self.q = 0  # number of wins
        self.n = 0  # num rollouts ie how many playouts
        self.is_visited = False  # nodes used to launch rollouts are marked visited
        self.ls_children_ = []  # list of children nodes
        self.reward = reward  # if terminal, node will have utility
 
    @property
    def is_terminal(self):
        """check if the node is a terminal node."""
        return len(self.ls_children_) == 0
        
    def add_children(self, ls_children):
        """add a list consisting of children nodes."""
        self.ls_children_ = copy.copy(ls_children)  # copy since lists are mutable
        self.ls_unvisited_children_ = ls_children  # we will sample from list of unvisited children
        _ = self._update_childs_parent()  # each child is updated with its parent
        
    def _update_childs_parent(self):
        """update a node's children with information about its parent.
        
        every node must know its parent in order to calculate its ucb 
        statistic, which requires its parent's N (ie num rollouts)
        """
        for child in self.ls_children_:
            child.parent_node = self
        
    @property
    def select_unvisited_children(self):
        """for a given node, select an unvisited child.
        
        a node is considered "expanded" once all of its children
        has been visited.        
        """
        # option 1: root node still has unvisited children (aka not expanded)
        if not self.is_expanded:
            
            # select child for rollout
            selected_child = np.random.choice(self.ls_unvisited_children_)
            
            # housekeeping
            self.ls_unvisited_children_.remove(selected_child)
            return selected_child
        
        # option 2: all children have been evaluated, so select child with the highest ucb score
        else:
            selected_child = None
            max_ucb = 0
            
            # select child with the highest ucb score 
            for child in self.ls_children_:
                if child._calculate_ucb > max_ucb:
                    selected_child = child
                    max_ucb = child._calculate_ucb
            return selected_child
        
    @property
    def is_expanded(self):
        """a root node is considered expanded once its 
        children have had playouts.
        """
        return len(self.ls_unvisited_children_) == 0
    
    @property
    def _calculate_ucb(self):
        """
        ni is the number of the times the node has been 
        visited and N is the total number of times that 
        its parent has been visited. 
        
        http://mcts.ai/about/
        """
        c_param = .14  # hyperparam, usually sqrt of 2
        parent_N = self.parent_node.n
        term_1 = (self.q / self.n)  # can be interpreted as the value estimate
        term_2 = c_param * np.sqrt((2 * np.log(parent_N) / self.n))
        return  term_1 + term_2