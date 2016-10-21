__author__ = 'Pranay'
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('fivethirtyeight')

# xs = np.array(range(1,7), dtype=np.float64)
# ys = np.array([5,4,6,5,6,7], dtype=np.float64)

def create_dataset(hm, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation=='pos':
            val+=step
        elif correlation and correlation=='neg':
            val-=step
    xs = [i for i in range(len(ys))]
    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)

def best_fit_slope_and_intercept(xs, ys):
    m = ( ((mean(xs)*mean(ys)) - mean(xs*ys)) /
          (pow(mean(xs),2) - mean(xs*xs)) )
    b = mean(ys) - m*mean(xs)
    return m, b

def sqrEr(ys_orig, ys_line):
    return sum((ys_line-ys_orig)**2)

def coefDitermination(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squarred_error_regr = sqrEr(ys_orig, ys_line)
    squarred_error_mean = sqrEr(ys_orig, y_mean_line)
    return 1 - squarred_error_regr/squarred_error_mean

xs, ys = create_dataset(40, 40, 2, correlation='pos')

m,b = best_fit_slope_and_intercept(xs, ys)

regression_line = [(m*x) + b for x in xs]

preict_x = 8
predicted_y = m*preict_x + b

print (m, b, coefDitermination(ys, regression_line))
plt.scatter(xs, ys)
plt.plot(xs, regression_line)
plt.scatter(preict_x, predicted_y, s=100)
plt.show()