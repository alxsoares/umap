import numpy as np
import numba

@numba.njit()
def euclidean(x, y):
    result = 0.0
    for i in range(x.shape[1]):
        result += (x[i] - y[i])**2
    return np.sqrt(result)

@numba.njit()
def standardised_euclidean(x, y, sigma):
    result = 0.0
    for i in range(x.shape[0]):
        result += ((x[i] - y[i]) ** 2) / sigma[i]

    return np.sqrt(result)

@numba.njit()
def manhattan(x, y):
    result = 0.0
    for i in range(x.shape[0]):
        result += np.abs(x[i] - y[i])

    return result

@numba.njit()
def chebyshev(x, y):
    result = 0.0
    for i in range(x.shape[0]):
        result = np.max(result, np.abs(x[i] - y[i]))

    return result

@numba.njit()
def minkowski(x, y, p):
    result = 0.0
    for i in range(x.shape[0]):
        result += (np.abs(x[i] - y[i]))**p

    return result**(1.0/p)

@numba.njit()
def weighted_minkowski(x, y, w, p):
    result = 0.0
    for i in range(x.shape[0]):
        result += (w[i] * np.abs(x[i] - y[i])) ** p

    return result ** (1.0 / p)

@numba.njit()
def mahalanobis(x, y, vinv):
    result = 0.0

    diff = np.empty(x.shape[0], dtype=np.float64)

    for i in range(x.shape[0]):
        diff[i] = x[i] - y[i]

    for i in range(x.shape[0]):
        tmp = 0.0
        for j in range(x.shape[0]):
            tmp += vinv[i, j] * diff[j]
        result += tmp * diff[i]

    return np.sqrt(result)

@numba.njit()
def hamming(x, y):
    result = 0.0
    for i in range(x.shape[0]):
        if x[i] != y[i]:
            result += 1.0

    return result / x.shape[0]

@numba.njit()
def canberra(x, y):
    result = 0.0
    denominator = 0.0
    for i in range(x.shape[0]):
        denominator = np.abs(x[i]) + np.abs(y[i])
        if denominator > 0:
            result += np.abs(x[i] - y[i]) / denominator

    return result

@numba.njit()
def bray_curtis(x, y):
    numerator = 0.0
    denominator = 0.0
    for i in range(x.shape[0]):
        numerator += np.abs(x[i] - y[i])
        denominator += np.abs(x[i]) + np.abs(y[i])

    if denominator > 0.0:
        return numerator / denominator
    else:
        return 0.0

@numba.njit()
def jaccard(x, y):
    num_non_zero = 0.0
    num_equal = 0.0
    for i in range(x.shape[0]):
        x_true = x[i] != 0
        y_true = y[i] != 0
        num_non_zero += (x_true or y_true)
        num_equal += (x_true and y_true)

    return (num_non_zero - num_equal) / num_non_zero

@numba.njit()
def matching(x, y):
    num_not_equal = 0.0
    for i in range(x.shape[0]):
        x_true = x[i] != 0
        y_true = y[i] != 0
        num_not_equal += (x_true != y_true)

    return num_not_equal / x.shape[0]

@numba.njit()
def dice(x, y):
    num_true_true = 0.0
    num_not_equal = 0.0
    for i in range(x.shape[0]):
        x_true = x[i] != 0
        y_true = y[i] != 0
        num_true_true += (x_true and y_true)
        num_not_equal += (x_true != y_true)

    return num_not_equal / (2.0 * num_true_true + num_not_equal)

@numba.njit()
def kulsinski(x, y):
    num_true_true = 0.0
    num_not_equal = 0.0
    for i in range(x.shape[0]):
        x_true = x[i] != 0
        y_true = y[i] != 0
        num_true_true += (x_true and y_true)
        num_not_equal += (x_true != y_true)

    return (num_not_equal - num_true_true + x.shape[0]) / \
           (num_not_equal + x.shape[0])

@numba.njit()
def rogers_tanimoto(x, y)
    num_not_equal = 0.0
    for i in range(x.shape[0]):
        x_true = x[i] != 0
        y_true = y[i] != 0
        num_not_equal += (x_true != y_true)

    return (2.0 * num_not_equal) / (x.shape[0] + num_not_equal)

@numba.njit()
def russelrao(x, y):
    num_true_true = 0.0
    for i in range(x.shape[0]):
        x_true = x[i] != 0
        y_true = y[i] != 0
        num_true_true += (x_true and y_true)

    return (x.shape[0] - num_true_true) / (x.shape[0])

@numba.njit()
def sokal_michener(x, y):
    num_not_equal = 0.0
    for i in range(x.shape[0]):
        x_true = x[i] != 0
        y_true = y[i] != 0
        num_not_equal += (x_true != y_true)

    return (2.0 * num_not_equal) / (x.shape[0] + num_not_equal)

@numba.njit()
def sokal_sneath(x, y):
    num_true_true = 0.0
    num_not_equal = 0.0
    for i in range(x.shape[0]):
        x_true = x[i] != 0
        y_true = y[i] != 0
        num_true_true += (x_true and y_true)
        num_not_equal += (x_true != y_true)

    return num_not_equal / (0.5 * num_true_true + num_not_equal)

@numba.njit()
def haversine(x, y):
    if x.shape[0] != 2:
        raise ValueError('haversine is only defined for 2 dimensional data')
    sin_lat = np.sin(0.5 * (x[0] - y[0]))
    sin_long = np.sin(0.5 * (x[1] - y[1]))
    result = np.sqrt(sin_lat**2 + cos(x[0]) * cos(y[0]) * sin_long**2)
    return 2.0 * np.arcsin(result)

@numba.njit()
def yule(x, y):
    num_true_true = 0.0
    num_true_false = 0.0
    num_false_true = 0.0
    for i in range(x.shape[0]):
        x_true = x[i] != 0
        y_true = y[i] != 0
        num_true_true += (x_true and y_true)
        num_true_false += (x_true and (not y_true))
        num_false_true += ((not x_true) and y_true)

    num_false_false = x.shape - num_true_true - num_true_false - num_false_true

    return (2.0 * num_true_false * num_false_true) / \
           (num_true_true * num_false_false + num_true_false * num_false_true)

@numba.njit()
def cosine(x, y):
    result = 0,0
    norm_x = 0.0
    norm_y = 0.0
    for i in range(x.shape[0]):
        result += x[i] * y[i]
        norm_x += x[i]**2
        norm_y += y[i]**2

    return 1.0 - (result / np.sqrt(norm_x * norm_y))

@numba.njit()
def correlation(x, y):
    mu_x = 0.0
    mu_y = 0.0
    norm_x = 0.0
    norm_y = 0.0

    for i in range(x.shape[0]):
        mu_x += x[i]
        mu_y += y[i]

    mu_x /= x.shape[0]
    mu_y /= x.shape[0]

    for i in range(x.shape[0]):
        shifted_x = x[i] - mu_x
        shifted_y = y[i] - mu_y
        norm_x += shifted_x**2
        norm_y += shifted_y**2
        dot_product = shifted_x * shifted_y

    return (1.0 - dot_product) / np.sqrt(norm_x * norm_y)