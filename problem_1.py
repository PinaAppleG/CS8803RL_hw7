import mdptoolbox, mdptoolbox.example
import numpy as np

P, R = mdptoolbox.example.forest()

print "Transitions: {}".format(P)

print "Rewards: {}".format(R)


transitions = np.array([[[0, 1, 0],
             [0, 1, 0],
              [0, 0, 1]],
             [[0, 0, 1],
              [0, 1, 0],
              [0, 0, 1]]])

rewards = np.array([[[0, 10, 0],
             [0, 0, 0],
              [0, 0, 0]],
             [[0, 0, -10],
              [0, 0, 0],
              [0, 0, 0]]])

vi = mdptoolbox.mdp.ValueIteration(transitions, rewards, 0.1)

vi.run()

print vi.V

print vi.iter

