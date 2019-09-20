import math

co = 2
ca = 8
hip = math.sqrt(co ** 2 + ca ** 2)
print('hipotenusa calculada = {:.2f}'.format(hip))
hip_m=math.hypot(co,ca)
print('hipotenusa pela funçao hypot = {:.2f}'.format(hip_m))