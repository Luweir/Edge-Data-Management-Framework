"""
Examples to help illustrate the module BPL.PY
=============================================
Created: Mon Apr 17, 2017  01:19PM
Last modified: Tue Apr 18, 2017  10:48AM
Copyright: Bedartha Goswami <goswami@uni-potsdam.de>
"""

import numpy as np
import matplotlib.pyplot as pl
import src.mkt


def show_examples():
    """
    Returns the MK test results for artificial insurance.
    """
    # create artificial time series with trend
    n = 1000
    C = [0.01, 0.001, -0.001, -0.01]
    e = 1.00
    t = np.linspace(0., 500, n)

    # set up figure
    fig, axes = pl.subplots(nrows=2, ncols=2, figsize=[16.00, 9.00])

    # loop through various values of correlation
    ALPHA = 0.01
    for c, ax in zip(C, axes.flatten()):
        # estimate the measurements 'x'
        print("c, ax: ", c, ax)
        x = c * t + e * np.random.randn(n)
        print("x: ", x)
        x = np.round(x, 2)
        print("x: ", x)

        # get the slope, intercept and pvalues from the mklt module
        MK, m, c, p = src.mkt.test(t, x, eps=1E-3, alpha=ALPHA, Ha="upordown")
        print("MK, m, c, p : ")
        print("MK: ", MK)
        print("m: ", m)
        print("c: ", c)
        print("p: ", p)

        # plot results
        ax.plot(t, x, "k.-", label="Sampled time series")
        ax.plot(t, m * t + c, "r-", label="Linear fit")
        ax.set_title(MK.upper() + "\np=%.3f, alpha = %.2f" % (p, ALPHA),
                     fontweight="bold", fontsize=10)

        # prettify
        if ax.is_last_row():
            ax.legend(loc="upper right")
            ax.set_xlabel("Time")
        if ax.is_first_col():
            ax.set_ylabel(r"Measurements $x$")
        if ax.is_first_row():
            ax.legend(loc="upper left")

    # save/show plot
    pl.show(fig)
    return None


def test_xmy(data):
    ALPHA = 0.01
    t = np.arange(1, len(data) + 1)
    x = np.array(data)
    MK, m, c, p = src.mkt.test(t, x, eps=1E-3, alpha=ALPHA, Ha="upordown")
    # plot results
    pl.figure(figsize=(24, 10), dpi=80)
    pl.plot(t, x, color='blue', label="insurance")
    pl.plot(t, m * t + c, color='red', label="Linear fit")
    pl.title(MK.upper() + "\np=%.3f, alpha = %.2f" % (p, ALPHA), fontweight="bold", fontsize=10)
    pl.show()


if __name__ == "__main__":
    # print("running example...")
    # show_examples()
    # print("done.")
    ce47 = [19.515, 19.567, 19.646, 19.85, 19.852, 19.824, 19.75, 19.683, 19.475, 19.639, 19.693, 19.696, 19.714, 19.76,
            19.727, 19.67, 19.398, 19.643, 19.359, 19.359, 19.612, 19.671, 19.63, 19.63, 19.669, 19.339, 19.157, 19.063,
            19.009, 18.894, 19.001, 18.908, 19.129, 19.137, 19.088, 18.994, 18.779, 18.759, 18.675, 18.795, 18.785,
            18.911, 19.012, 19.209, 19.276, 19.279, 18.994, 19.163, 19.168, 19.219, 19.468, 19.445, 19.727, 19.696,
            19.696, 19.67, 19.437, 19.483, 19.357, 19.527]
    cp481 = [1.595, 1.612, 1.617, 1.638, 1.618, 1.622, 1.599, 1.605, 1.6, 1.573, 1.577, 1.575, 1.593, 1.592, 1.583,
             1.582, 1.571, 1.575, 1.57, 1.574, 1.567, 1.582, 1.588, 1.599, 1.609, 1.615, 1.615, 1.597, 1.582, 1.586,
             1.585, 1.597, 1.604, 1.611, 1.604, 1.609, 1.599, 1.58, 1.589, 1.588, 1.583, 1.583, 1.604, 1.597, 1.609,
             1.606, 1.609, 1.61, 1.605, 1.606, 1.609, 1.613, 1.632, 1.63, 1.626, 1.607, 1.605, 1.585, 1.596, 1.601]
    ts745 = [50.238, 50.168, 50.078, 50.062, 49.988, 49.988, 49.918, 49.836, 49.836, 49.809, 49.809, 49.773, 49.785,
             49.809, 49.828, 49.852, 49.922, 50.008, 50, 50.027, 50.039, 50.039, 50.047, 50.09, 50.074, 50.078, 50.09,
             50.094, 50.086, 50.094, 50.086, 50.168, 50.168, 50.16, 50.238, 50.187, 50.207, 50.223, 50.238, 50.238,
             50.223, 50.219, 50.219, 50.211, 50.16, 50.172, 50.168, 50.152, 50.168, 50.16, 50.086, 50.09, 50.086,
             50.086, 50.078, 50.051, 50.039, 50.039, 50.055, 50.039]
    test_xmy(ts745)
