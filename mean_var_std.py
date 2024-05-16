import numpy as np

def calculate(list):

    # check if the list has 9 numbers
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    #create numpy array and reshape the list
    array = np.array(list)
    array = array.reshape(3,3)

    #keys needed
    keys = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']

    #calculation dictionary
    calculations = {key: [] for key in keys}

    #necessary calculations
    calculations['mean'] = [np.mean(array, axis=0).tolist(), np.mean(array, axis=1).tolist(), np.mean(array).tolist()]

    calculations['variance'] = [np.var(array, axis=0).tolist(), np.var(array, axis=1).tolist(), np.var(array).tolist()]

    calculations['standard deviation'] = [np.std(array, axis=0).tolist(), np.std(array, axis=1).tolist(), np.std(array).tolist()]

    calculations['max'] = [np.max(array, axis=0).tolist(), np.max(array, axis=1).tolist(), np.max(array).tolist()]

    calculations['min'] = [np.min(array, axis=0).tolist(), np.min(array, axis=1).tolist(), np.min(array).tolist()]

    calculations['sum'] = [np.sum(array, axis=0).tolist(), np.sum(array, axis=1).tolist(), np.sum(array).tolist()]

    return calculations
