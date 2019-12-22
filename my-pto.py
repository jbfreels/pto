from core.PTO import PTO

if __name__ == "__main__":
  mypto = PTO ()
  for y in mypto.years:
    print ("{} hours total in {}".format (y.get_total_hours (), y.year))
  