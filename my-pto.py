#!/usr/bin/env python3
from core.PTO import PTO

if __name__ == "__main__":
  mypto = PTO ()
  for y in mypto.years:
    print ("{} of {} hours available in {}".format (y.totalRemaining (), y.totalHours (), y.year))
  