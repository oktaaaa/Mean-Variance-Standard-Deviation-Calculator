import numpy as np

def calculate(list):
  
  
  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')
  else:
    array = np.array(list)
    matrix = (np.reshape(array, (3,3)))
    

    mean = [(np.mean(matrix, axis = 0).tolist()), (np.mean(matrix, axis = 1).tolist()), (np.mean(matrix))]
    var = [(np.var(matrix, axis = 0).tolist()), (np.var(matrix, axis = 1).tolist()), (np.var(matrix))]
    std =[(np.std(matrix, axis = 0).tolist()), (np.std(matrix, axis = 1).tolist()), (np.std(matrix))]
    maxi =[(np.max(matrix, axis = 0).tolist()), (np.max(matrix, axis = 1).tolist()), (np.max(matrix))]
    mini = [(np.min(matrix, axis = 0).tolist()), (np.min(matrix, axis = 1).tolist()), (np.min(matrix))]
    sums =  [(np.sum(matrix, axis = 0).tolist()),(np.sum(matrix, axis = 1).tolist()), (np.sum(matrix))]

    calculation = {
      'mean' : mean,
      'variance' : var,
      'standard deviation' : std,
      'max' : maxi,
      'min' : mini,
      'sum' : sums
    }

    return calculation


print(calculate([0,1,2,3,5,6,7,8,9]))
