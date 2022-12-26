import math

def mean(vals):
   return sum(vals)/float(len(vals))

def var(vals):
   """
   Unbiased sample variance.
   """
   m = mean(vals)
   try: return sum([(x - m)**2 for x in vals]) / (float(len(vals)) - 1)
   except ZeroDivisionError: return 0

def stddev(vals):
   return math.sqrt(var(vals))


def norm_by_max(vals):
   mx = float(max(vals))
   return [val/mx for val in vals]

