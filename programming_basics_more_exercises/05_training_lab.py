import math

aula_h = float(input())
aula_w = float(input())

aula_w_spaces = (aula_w - 1) // 0.7
aula_h_spaces = (aula_h) // 1.2

workspaces = math.floor((aula_w_spaces * aula_h_spaces) - 3)

print (workspaces)