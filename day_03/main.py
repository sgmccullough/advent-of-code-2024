import re

input = "input.txt"

def recur(curr):
  if curr[0] == 'u':
    recur(curr[1:])

def q1():
  total = 0
  for line in open(input, "r"):
    vals = re.findall(r'mul\(\d+,\d+\)', line.strip())
    for val in vals:
      splitVals = re.split('\\(|,|\\)', val)
      total += int(splitVals[1])*int(splitVals[2])

  return(total)

def q2():
  total = 0
  multiply = True
  for line in open(input, "r"):
    vals = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', line.strip())
    for val in vals:
      if "do()" in val:
        multiply = True
      elif "don't()" in val:
        multiply = False
      elif multiply:
        splitVals = re.split('\\(|,|\\)', val)
        total += int(splitVals[1])*int(splitVals[2])

  return(total)

if __name__=="__main__":
  print(f"Part 1:", q1())
  print(f"Part 2:", q2())