#Policy Evaluation calculates the value function for a policy, given the policy and the full definition of the associated Markov Decision Process. 
#The full definition of an MDP is the set of states, the set of available actions for each state, the set of rewards, the discount factor, and 
#the state/reward transition function.

import test_dp               # required for testing and grading your code
import gridworld_mdp as gw   # defines the MDP for a 4x4 gridworld

#Implement the algorithm for Iterative Policy Evaluation using the in-place approach. 
#In the in-place approach, one array holds the values being estimated for each state and the same array is used for estimates of states needed by the algorithm.

#A empty function policy_eval_in_place is provided below; implement the body of the function to correctly calculate the value of the policy 
#using the 2 array approach. The function defines 5 parameters - a definition of each parameter is given in the comment block for the function. 
#For sample parameter values, see the calling code in the cell following the function.

def policy_eval_in_place(state_count, gamma, theta, get_policy, get_transitions):
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
    # insert code here to evaluate the policy using the in-place approach 
    #
    return V


#First, test our function using the MDP defined by gw.* functions.
def get_equal_policy(state):
    # build a simple policy where all 4 actions have the same probability, ignoring the specified state
    policy = ( ("up", .25), ("right", .25), ("down", .25), ("left", .25))
    return policy

n_states = gw.get_state_count()

# test our function
values = policy_eval_in_place(state_count=n_states, gamma=.9, theta=.001, get_policy=get_equal_policy, \
    get_transitions=gw.get_transitions)

print("Values=", values)

# test our function using the test_db helper
test_dp.policy_eval_in_place_test(policy_eval_in_place)