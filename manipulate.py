import numpy as np

transitions = np.array([[[0,1,0], [0, 0, 1]], [[0, 1, 0], [0, 1, 0]], [[0, 0, 1], [0, 0, 1]]])
#
# morphed = np.array([], dtype=np.int64).reshape(0, transitions.shape[0])
#
# for i in xrange(transitions.shape[0]):
#     print transitions[i][0,:]
#     morphed = np.vstack((morphed, transitions[i][0]))
#
# print morphed

#a = np.array([[[1, 2],[3, 4]], [[5, 6], [7, 8]]])
print np.swapaxes(transitions, 0, 1)