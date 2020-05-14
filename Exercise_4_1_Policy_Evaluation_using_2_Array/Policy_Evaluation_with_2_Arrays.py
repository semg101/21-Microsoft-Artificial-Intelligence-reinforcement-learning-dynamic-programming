#Policy Evaluation calculates the value function for a policy, given the policy and the full definition of the associated Markov Decision Process. 
#The full definition of an MDP is the set of states, the set of available actions for each state, the set of rewards, the discount factor, 
#and the state/reward transition function.

import test_dp               # required for testing and grading your code
import gridworld_mdp as gw   # defines the MDP for a 4x4 gridworld


#The gridworld MDP defines the probability of state transitions for our 4x4 gridworld using a "get_transitions()" function.
#Let's try it out now, with state=2 and all defined actions.

# try out the gw.get_transitions(state, action) function
state = 2
actions = gw.get_available_actions(state)

for action in actions:
    transitions = gw.get_transitions(state=state, action=action)

    # examine each return transition (only 1 per call for this MDP)
    for (trans) in transitions:
        next_state, reward, probability = trans    # unpack tuple
        print("transition("+ str(state) + ", " + action + "):", "next_state=", next_state, ", reward=", reward, ", probability=", probability)


#Implement the algorithm for Iterative Policy Evaluation using the 2 array approach. 
#In the 2 array approach, one array holds the value estimates for each state computed on the previous iteration, 
#and one array holds the value estimates for the states computing in the current iteration.

#A empty function policy_eval_two_arrays is provided below; implement the body of the function to correctly calculate 
#the value of the policy using the 2 array approach. The function defines 5 parameters - a definition of each parameter 
#is given in the comment block for the function. For sample parameter values, see the calling code in the cell following the function.
def policy_eval_two_arrays(state_count, gamma, theta, get_policy, get_transitions):
    """
    This function uses the two-array approach to evaluate the specified policy for the specified MDP:
    
    'state_count' is the total number of states in the MDP. States are represented as 0-relative numbers.
    
    'gamma' is the MDP discount factor for rewards.
    
    'theta' is the small number threshold to signal convergence of the value function (see Iterative Policy Evaluation algorithm).
    
    'get_policy' is the stochastic policy function - it takes a state parameter and returns list of tuples, 
        where each tuple is of the form: (action, probability).  It represents the policy being evaluated.
        
    'get_transitions' is the state/reward transiton function.  It accepts two parameters, state and action, and returns
        a list of tuples, where each tuple is of the form: (next_state, reward, probabiliity).  
        
    """
    V = state_count*[0]
    #
    # INSERT CODE HERE to evaluate the policy using the 2 array approach 
    #
    return V


#First, test our function using the MDP defined by gw.* functions.
def get_equal_policy(state):
    # build a simple policy where all 4 actions have the same probability, ignoring the specified state
    policy = ( ("up", .25), ("right", .25), ("down", .25), ("left", .25))
    return policy

n_states = gw.get_state_count()

# test our function
values = policy_eval_two_arrays(state_count=n_states, gamma=.9, theta=.001, get_policy=get_equal_policy, get_transitions=gw.get_transitions)

print("Values=", values)


import numpy as np
a = np.append(values, 0)
print(np.reshape(a, (4,4)))


#Now, test our function using the test_dp helper. The helper also uses the gw MDP, but with a different gamma value. 
#If our function passes all tests, a passcode will be printed.

# test our function using the test_db helper
test_dp.policy_eval_two_arrays_test( policy_eval_two_arrays )