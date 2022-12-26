"""
This file was written to test matplotlib's autolegend placement
algorithm, but shows lots of different ways to create legends so is
useful as a general examples

Thanks to John Gill and Phil ?? for help at the matplotlib sprint at
pycon 2005 where the auto-legend support was written.
"""
from pylab import *
import sys
import matplotlib.mlab as mlab
rcParams['legend.loc'] = 'best'

def loglikelihood(N, mug, mub, mu= 0.5, niter=1000):
    arr = []
    for j in range(niter):
        l = [0.0]
        ran = randn(N) + array([mu] * N)
#        print ran
        for i in range(1,N):
            l.append(max(0, l[-1] + (mub-mug) *(ran[i] - 0.5* (mug+mub))))
        arr.append(max(l))
    from scipy.stats.mstats import mquantiles as mq
    print([i/abs(mug-mub) for i in mq(arr, [0.25,0.5,0.75,0.95, 0.975, 0.99])])
    return array(arr)

def fig_1():
    figure(5)
#    n, bins, patches = hist(randn(1000), 40, normed=1)
    sample = loglikelihood(25, 0.5, 0.0, - 0.5)
    n, bins, patches = hist(sample, 80, normed=1)
    l, = plot(bins, mlab.normpdf(bins, mean(sample), 1.0), 'r--', label='fit', linewidth=3)
    legend([l, patches[0]], ['fit', 'hist'])

def main():
    nfigs = 1
    figures = []
    for f in sys.argv[1:]:
        try:
            figures.append(int(f))
        except ValueError:
            pass
    if len(figures) == 0:
        figures = range(1, nfigs+1)

    for fig in figures:
        fn_name = "fig_%d" % fig
        fn = globals()[fn_name]
        fn()
    show()

def main2():
    for ir in [-0.5, 0, 0.5]:
#        for t in [24,36,48,60,72,84]:
        for t in [11,15,18,21,23,25]:
            print(ir, t)
            loglikelihood(t, 0.5, 0.0, ir)

if __name__ == '__main__':
#    main()
    main2()
