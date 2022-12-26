#!/usr/bin/python

import math
import mlpy
import numpy as np

import utils

def euc_day_sim(d1, d2):
   """
   Euclidian daily similarity for two sequences of identical lengths.
   """
   if len(d1) != len(d2): return None

   d = 0.0
   n = len(d1)
   for i in range(0, len(d1)):
      for j in range(i+1, len(d2)):
         d += abs(d1[i] - d2[j]) / ((n-1.0) * ((n-2.0)) / 2.0)
         
   return d


 

if __name__ == "__main__":
   
   d1 = [20, 23, 16, 19, 23, 16, 22, 12, 9, 17, 20, 18, #1974
      2, 8, 8, 23, 14, 25, 16, 25, 7, 2, 3, 13, #1975
      20, 18, 30, 17, 23, 21, 14, 22, 18, 18, 13, 27, #1976
      25, 20, 31, 22, 15, 26, 21, 23, 14, 13, 58, 15, #1977
      29, 27, 25, 10, 17, 17, 30, 22, 14, 15, 14, 14,
      24, 14, 19, 9, 11, 7, 19, 8, 19, 22, 11, 22]
   
   d2 = [10, 6, 7, 14, 14, 5, 5, 1, 2, 3, 4, 10, 
      14, 18, 19, 20, 13, 14, 10, 10, 5, 4, 6, 16,
      20, 23, 16, 19, 23, 16, 22, 12, 9, 17, 20, 18, #1974
      2, 8, 8, 23, 14, 25, 16, 25, 7, 2, 3, 13, #1975
      20, 18, 30, 17, 23, 21, 14, 22, 18, 18, 13, 27, #1976
      25, 20, 31, 22, 15, 26, 21, 23, 14, 13, 58, 15] #1977
         

   #print euc_day_sim(ddd)
   d1 = utils.norm_by_max(d1)
   d2 = utils.norm_by_max(d2)
   print "\"Smoothed\" Euclidian Distance: ", euc_day_sim(d1, d2)

   mydtw = mlpy.Dtw(onlydist=True)
   print "Dynamic Time Warp Distance: ", mydtw.compute(d1, d2)

