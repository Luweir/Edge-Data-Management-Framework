#!/usr/bin/python

import math
import utils
import matplotlib.pyplot as plt

######################################################
#This is really only effective as a one-sided cusum.
#The other side (the low side) seems to be... odd.
def cusum(vals, k, h):
   """
   """
   shvals = []
   slvals = []
   hlist = []
   nhlist = []
   npos = 0
   nneg = 0
   sh = 0
   sl = 0
   for val in vals: 
      hlist.append(h)
      nhlist.append(-h)
      sh += max(0, val - k + sh)
      sl += min(0, val - k + sl)
      shvals.append(sh)
      slvals.append(sl)
      if sh >= h or sl <= -h:
         #print "Alarm"
         sh = 0 
         sl = 0
      #print "Curr. val: %.2f -- Curr. Sum High: %.2f -- Curr. Sum Low: %.2f" % (val, sh, sl)

   return (shvals, slvals, hlist, nhlist)



def esth(vals):
   """
   A reasonable estimate for h is approx. 5 * sigma.
   (i.e. 5 * std. deviation of samples.)
   """
   return 5.0 * utils.stddev(vals)
   

def buildk(vals, ma, s=1.5):
   """
   According to Kemp (1962), the expression for determing a target value
   k for cusum should be done via:

         k = mean_a + .5 delta
         (Where: delta is the mean shift we want to detect.
                 mean_a is an "acceptable process mean value."
                 mean_a is the mean of the original dataset.) 

   Lucas et al. (1982) suggested it be close to .5 delta as well,
   and it should be chosen close to:

                    mean_d - mean_a
         k = ---------------------------
               ln (mean_d) - ln (mean_a)

   Mean_d is the "barely tolerable mean value".  This is the mean that
   CUSUM should quickly detect.  Mean_d is based on the declared needs
   of an experimental designer, the mean, and the std dev.

      mean_d = s * p + mean_a 
      (Where: s is a value chosen by the experimental designers,
              p is the standard deviation, and mean_a is the mean
              of the dataset.)
   """
   md = s * utils.stddev(vals) + ma
   return (md - ma) / (math.log(md, math.e) - math.log(ma, math.e))
   
   

if __name__ == "__main__":

   #Diabetic disease insurance
   ddd = [26.486,26.521,26.521,26.502,26.628,26.613,26.624,26.533,26.486,26.482,26.377,26.411,26.427,26.388,26.565,26.756,26.678,26.714,26.848,26.872,26.903,26.828,26.924,26.949,26.872,26.892,27.01,26.938,26.937,26.903,26.71,26.698,26.492,26.414,26.491,26.458,26.513,26.349,26.427,26.485,26.365,26.392,26.458,26.383,26.539,26.38,26.388,26.185,26.184,26.255,26.208,26.243,26.411,26.427,26.388,26.423,26.345,26.438,26.392,26.547]
   # ddd = [19.321,19.436,19.418,19.312,19.258,19.194,19.243,19.215,19.061,19.068,19.111,18.927,19.02,19.061,18.991,19.03,18.977,19.073,18.908,18.981,19.119,19.119,19.159,19.135,19.105,19,19.023,19.059,19.078,19.101,19.054,19.174,18.939,19.322,19.048,19.045,19.03,18.93,18.939,18.937,18.959,18.937,19.049,19.106,19.07,19.101,19.059,19.242,19.116,19.082,19.118,19.248,19.328,19.278,19.179,19.214,19.054,19.059,19.191,19.207]
   # ddd = [47.202,47.273,47.25,47.332,47.213,47.372,47.273,47.438,46.691,46.599,46.623,46.653,46.136,46.127,45.948,45.935,45.726,45.139,44.978,44.937,44.269,44.079,43.741,43.375,42.847,42.322,42.322,41.797,41.406,40.924,40.427,39.857,39.517,38.999,38.493,37.954,37.552,37.084,36.615,36.098,35.58,35.141,34.184,34.177,33.739,33.226,32.913,32.4,31.833,31.862,31.554,30.953,30.639,30.561,30.368,30.224,29.79,29.261,29.287,28.866]

   k = buildk(ddd, utils.mean(ddd))
   shvals, slvals, hlist, nhlist = cusum(ddd, k, 20)
   print(max(shvals), shvals.index(max(shvals)))

   plt.plot([0,1,3,0,2,4,8,6,4,0], "-go")
   plt.plot(shvals, "-go")
   plt.plot(slvals, "-bo")
   plt.plot(hlist, "-rx")
   plt.plot(nhlist, "-rx")

   plt.show()
















