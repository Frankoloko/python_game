# import math

# degree = 180.0 # (-1, 0) # links # WRONG (-1, -1)
# degree_vector = ( round( math.sin(degree) ), round( math.sin(degree) ) )

# # degree = 270.0 / 2 # (0, -1) # af # WRONG (1, 0)
# # degree_vector = ( round( math.sin(degree) ), round( math.cos(degree) ) )

# # degree = 0.0 # (1, 0) # regs # REG
# # degree = 90.0 # (0, 1) # boontoe # REG
# # degree_vector = ( round( math.cos(degree) ), round( math.sin(degree) ) )

# # print(degree_vector)

# # while degree >= 360.0:
# #     degree -= 360.0

# # degree = 0.0
# # vector = ( round(math.sin(degree)), round(math.cos(degree)))
# # print(f'Op {degree}, {vector}')

# # degree = 90.0
# # vector = ( round(math.sin(degree)), round(math.cos(degree)))
# # print(f'Regs {degree}, {vector}')

# # degree = 180.0
# # vector = ( round(math.sin(degree)), round(math.cos(degree)))
# # print(f'Af {degree}, {vector}')

# # degree = 270.0
# # vector = ( round(math.sin(degree)), round(math.cos(degree)))
# # print(f'Links {degree}, {vector}')


# # print(round(math.sin(90.0)), round(math.cos(90.0)), round(math.tan(90.0)))
# # print(round(math.sin(180.0)), round(math.cos(180.0)), round(math.tan(180.0)))
# # print(round(math.sin(270.0)), round(math.cos(270.0)), round(math.tan(270.0)))

# # print(round(math.sin(0)), round(math.cos(0)), round(math.tan(0)))
# # print(round(math.sin(360.0)), round(math.cos(360.0)), round(math.tan(360.0)))

import math

degree = 100.0
radians = degree * (math.pi / 180)
vector = (math.cos(radians), math.sin(radians))