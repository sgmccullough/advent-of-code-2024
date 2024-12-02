input = "input.txt"

def q1():
  safeNum = 0
  for line in open(input, "r"):
    levels = line.strip().split()
    dir = 0
    safe = True
    i = 1
    while i < len(levels):
      curr = int(levels[i])
      prev = int(levels[i-1])
      if dir == 0:
        if curr > prev:
          dir = 1
        elif curr < prev:
          dir = -1
        else:
          safe = False
          break
      if dir == 1:
        if not (curr > prev and curr - prev >= 1 and curr - prev <= 3):
          safe = False
          break
      elif dir == -1:
        if not (curr < prev and curr - prev <= -1 and curr - prev >= -3):
          safe = False
          break
      i+=1
    if safe:
      safeNum += 1
  return(safeNum)

def q2_recur(levels):
  dir = 0
  safe = True
  i = 1
  while i < len(levels):
    curr = int(levels[i])
    prev = int(levels[i-1])
    if dir == 0:
      if curr > prev:
        dir = 1
      elif curr < prev:
        dir = -1
      else:
        safe = False
        break
    if dir == 1:
      if not (curr > prev and curr - prev >= 1 and curr - prev <= 3):
        safe = False
        break
    elif dir == -1:
      if not (curr < prev and curr - prev <= -1 and curr - prev >= -3):
        safe = False
        break
    i+=1
  return(safe)

def q2():
  safeNum = 0
  for line in open(input, "r"):
    levels = line.strip().split()
    dir = 0
    safe = True
    i = 1
    while i < len(levels):
      curr = int(levels[i])
      prev = int(levels[i-1])
      if dir == 0:
        if curr > prev:
          dir = 1
        elif curr < prev:
          dir = -1
        else:
          safe = False
          break
      if dir == 1:
        if not (curr > prev and curr - prev >= 1 and curr - prev <= 3):
          safe = False
          break
      elif dir == -1:
        if not (curr < prev and curr - prev <= -1 and curr - prev >= -3):
          safe = False
          break
      i+=1
    if safe:
      safeNum += 1
    else:
      j = 0
      while j < len(levels):
        if q2_recur(levels[:j] + levels[j+1:]):
          safeNum+=1
          break
        j+=1
  return(safeNum)

if __name__=="__main__":
  print(f"Part 1:", q1())
  print(f"Part 2:", q2())