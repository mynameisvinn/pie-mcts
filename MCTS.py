from tqdm import trange
import numpy as np

class MCTS(object):
    def __init__(self):
        pass
    
    def fit(self, root_node, n_rollouts):
        self.root_node = root_node
        self.n_rollouts = n_rollouts
    
    def predict(self):
        for rollout in trange(self.n_rollouts):
            trace = [self.root_node]  # a trace for each rollout
            curr_node = trace[0]

            # select an unvisited child
            curr_child = curr_node.select_unvisited_children

            # once a rollout has been played from child, it is visited
            curr_child.is_visited = True

            # add node for qa tracing
            trace.append(curr_child)

            # start rollout from unvisited child
            while True:
                next_child = np.random.choice(curr_child.ls_children_)
                trace.append(next_child)

                # option 1: child is terminal, so get its utility value
                if next_child.is_terminal:
                    outcome = next_child.reward
                    break

                # option 2: child has children
                else:
                    curr_child = next_child


            # propagate - for each node, update its (a) win and (b) games played counts
            for node in trace:
                node.q += outcome
                node.n += 1
                
        return self._select_child().name
    
    
    def _select_child(self):
        """return root node's child with the most plays (not
        biggest ucb).
        
        
        mcts will naturally favor children with high ucb 
        scores by selecting them more often. 
        """
        
        max_plays = 0
        selected_child = None
        
        for child in self.root_node.ls_children_:
            if child.n > max_plays:
                selected_child = child
                max_plays = child.n

        return selected_child