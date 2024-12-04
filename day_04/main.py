input = "input.txt"

def q1():
  wordSearch = []
  for line in open(input, "r"):
    wordSearch.append(list(line.strip()))
  XMAScount = 0
  l = 0
  while l < len(wordSearch):
    c = 0
    while c < len(wordSearch[l]):
      if wordSearch[l][c] == 'X':
        if c + 3 < len(wordSearch[l]):
          if "".join(wordSearch[l][c:c+4]) == "XMAS":
            # Horizontal Forwards -> +3 right, -0 left, -0 up, +0 down
            # print("Horizontal Forwards")
            XMAScount+=1
          if l + 3 < len(wordSearch):
            if wordSearch[l][c] + wordSearch[l+1][c+1] + wordSearch[l+2][c+2] + wordSearch[l+3][c+3] == "XMAS":
              # Diagonal down right -> +3 right, -0 left, -0 up, +3 down
              # print("Diagonal down Right")
              XMAScount+=1
          if l - 3 >= 0:
            if wordSearch[l][c] + wordSearch[l-1][c+1] + wordSearch[l-2][c+2] + wordSearch[l-3][c+3] == "XMAS":
              # Diagonal up right -> +3 right, -0 left, -3 up, +0 down
              # print("Diagonal up Right")
              XMAScount+=1
        if c - 3 >= 0:
          if "".join(wordSearch[l][c-3:c+1])[::-1] == "XMAS":
            # Horizontal Backwards -> +0 right, -3 left, -0 up, +0 down
            # print("Horizontal Backwards")
            XMAScount+=1
          if l + 3 < len(wordSearch):
            if wordSearch[l][c] + wordSearch[l+1][c-1] + wordSearch[l+2][c-2] + wordSearch[l+3][c-3] == "XMAS":
              # Diagonal down left -> +0 right, -3 left, -0 up, +3 down
              # print("Diagonal down Left")
              XMAScount+=1
          if l - 3 >= 0:
            if wordSearch[l][c] + wordSearch[l-1][c-1] + wordSearch[l-2][c-2] + wordSearch[l-3][c-3] == "XMAS":
              # Diagonal up left -> +0 right, -3 left, -3 up, +0 down
              # print("Diagonal up Left")
              XMAScount+=1
        if l + 3 < len(wordSearch):
          if wordSearch[l][c] + wordSearch[l+1][c] + wordSearch[l+2][c] + wordSearch[l+3][c] == "XMAS":
            # Vertical Forwards -> +0 right, -0 left, -0 up, +3 down
            # print("Vertical Forwards")
            XMAScount+=1
        if l - 3 >= 0:
          if wordSearch[l][c] + wordSearch[l-1][c] + wordSearch[l-2][c] + wordSearch[l-3][c] == "XMAS":
            # Vertical Backwards -> +0 right, -0 left, -3 up, +0 down
            # print("Vertical Backwards")
            XMAScount+=1
      c+=1
    l+=1
  return(XMAScount)

def q2():
  wordSearch = []
  for line in open(input, "r"):
    wordSearch.append(list(line.strip()))
  XMAScount = 0
  l = 0
  while l < len(wordSearch):
    c = 0
    while c < len(wordSearch[l]):
      if wordSearch[l][c] == 'A':
        if l + 1 < len(wordSearch) and l - 1 >= 0 and c + 1 < len(wordSearch[l]) and c - 1 >= 0:
          x_1 = wordSearch[l-1][c-1] + wordSearch[l][c] + wordSearch[l+1][c+1]
          x_2 = wordSearch[l+1][c-1] + wordSearch[l][c] + wordSearch[l-1][c+1]
          # print(x_1, x_2)
          if (x_1 == "MAS" or x_1[::-1] == "MAS") and (x_2 == "MAS" or x_2[::-1] == "MAS"):
            XMAScount+=1
      c+=1
    l+=1
  return(XMAScount)

if __name__=="__main__":
  print(f"Part 1:", q1())
  print(f"Part 2:", q2())