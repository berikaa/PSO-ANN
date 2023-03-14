from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import functools
import numpy as np
import sklearn.metrics
import sklearn.datasets
import sklearn.model_selection
import sklearn.metrics as sk


from pyswarm import pso

def dim_weights(shape):
    dim = 0
    for i in range(len(shape)-1):
        dim = dim + (shape[i] + 1) * shape[i+1]
    return dim

def weights_to_vector(weights):
    w = np.asarray([])
    for i in range(len(weights)):
        v = weights[i].flatten()
        w = np.append(w, v)
    return w

def vector_to_weights(vector, shape):
    weights = []
    idx = 0
    for i in range(len(shape)-1):
        r = shape[i+1]
        c = shape[i] + 1
        idx_min = idx
        idx_max = idx + r*c
        W = vector[idx_min:idx_max].reshape(r,c)
        weights.append(W)
    return weights

def eval_neural_network(weights, shape, X, y):
    mse = np.asarray([])
    for w in weights:
        weights = vector_to_weights(w, shape)
        nn = MultiLayerPerceptron(shape, weights=weights)
        #X=np.array(X)

        y_pred = nn.run(X)
        #y_pred=np.isnan(y_pred)
        mse = np.append(mse, sklearn.metrics.mean_squared_error(np.atleast_2d(y), y_pred))
    return mse

def print_best_particle(best_particle):
    ("New best particle found at iteration #{i} with mean squared error: {score}".format(i=best_particle[0], score=best_particle[1]))

def build_model(X,y):

  num_classes = 4

 # X, X_test, y, y_test = sklearn.model_selection.train_test_split(x_all, y_all)
  X=np.array(X)
  #X_test=np.array(X_test)
  y=np.array(y)
  y=y.astype(np.int)
  """
  y_test=np.array(y_test)
  y_test=y_test.astype(np.int)
  """

  num_inputs = X.shape[1]

  y_true = np.zeros((len(y), num_classes))

  for i in range(len(y)):
      y_true[i, y[i]-1] = 1


  # Set up
  shape = (num_inputs, 8,8, num_classes)

  cost_func = functools.partial(eval_neural_network, shape=shape, X=X, y=y_true.T)

  swarm = ParticleSwarm(cost_func, num_dimensions=dim_weights(shape), num_particles=50)

  # Train...
  i = 1
  best_scores = [(i, swarm.best_score)]
  print_best_particle(best_scores[-1])
  while swarm.best_score>1e-6 and i<800:
      swarm._update()
      i = i+1
      if swarm.best_score < best_scores[-1][1]:
          best_scores.append((i, swarm.best_score))
          print_best_particle(best_scores[-1])

  # Test...
  #X_test=np.array(X_test)
  best_weights = vector_to_weights(swarm.g, shape)
  best_nn = MultiLayerPerceptron(shape, weights=best_weights)
  return best_nn
