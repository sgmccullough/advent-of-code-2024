input = "input.txt"

def q1():
  left = []
  right = []
  for line in open(input, "r"):
    x = line.strip().split()
    left.append(int(x[0]))
    right.append(int(x[1]))
  left.sort()
  right.sort()
  i = 0
  diff = 0
  while i < len(left):
    diff += abs(left[i] - right[i])
    i+=1
  return(diff)

def q2():
  left = []
  right = dict()
  for line in open(input, "r"):
    x = line.strip().split()
    left.append(int(x[0]))
    if int(x[1]) in right:
      right[int(x[1])] += 1
    else:
      right[int(x[1])] = 1
  similarity = 0
  for val in left:
    if val in right:
      similarity += val * right[val]
  return(similarity)

if __name__=="__main__":
  print(f"Part 1:", q1())
  print(f"Part 2:", q2())