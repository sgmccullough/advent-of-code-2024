input = "input.txt"

def q1():
  rules = []
  updates = []
  isRule = True
  for line in open(input, "r"):
    if line.strip() == "":
      isRule = False
    elif isRule:
      rules.append(list(line.strip().split('|')))
    else:
      updates.append(list(line.strip().split(',')))
  total = 0
  for updateList in updates:
    isValid = True
    for rule in rules:
      if rule[0] in updateList and rule[1] in updateList:
        if not updateList.index(rule[0]) < updateList.index(rule[1]):
          isValid = False
          break
    if isValid:
      total += int(updateList[int((len(updateList) - 1) / 2)])
  
  return(total)

def q2():
  rules = []
  updates = []
  isRule = True
  for line in open(input, "r"):
    if line.strip() == "":
      isRule = False
    elif isRule:
      rules.append(list(line.strip().split('|')))
    else:
      updates.append(list(line.strip().split(',')))
  invalidUpdates = []
  for updateList in updates:
    for rule in rules:
      if rule[0] in updateList and rule[1] in updateList:
        if not updateList.index(rule[0]) < updateList.index(rule[1]):
          invalidUpdates.append(updateList)
          break
  for updateList in invalidUpdates:
    i = 0
    while i < len(rules):
      rule = rules[i]
      if rule[0] in updateList and rule[1] in updateList:
        first = updateList.index(rule[0])
        second = updateList.index(rule[1])
        if not first < second:
          firstVal = updateList[first]
          secondVal = updateList[second]
          updateList[first] = secondVal
          updateList[second] = firstVal
          i = 0
        else:
          i+=1
      else:
        i+=1
  total = 0
  for update in invalidUpdates:
    total+=int(update[int((len(update) - 1) / 2)])
  return(total)

if __name__=="__main__":
  print(f"Part 1:", q1())
  print(f"Part 2:", q2())