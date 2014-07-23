import csv
import math

# Adapted from Heer & Stone C3 and Wikipedia
# http://en.wikipedia.org/wiki/Color_difference#CIEDE2000
# Heer & Stone based off of http://www.ece.rochester.edu/~gsharma/ciede2000/
def ciede2000(lab1, lab2):
  kl = 1
  kc = 1
  kh = 1

  pi = math.pi
  L1 = lab1[0]
  a1 = lab1[1]
  b1 = lab1[2]
  L2 = lab2[0]
  a2 = lab2[1]
  b2 = lab2[2]

  Cab1 = math.sqrt(a1*a1 + b1*b1)
  Cab2 = math.sqrt(a2*a2 + b2*b2)
  Cab = (Cab1+Cab2)/2

  # create a'_1 and a'_2 (per wikipedia)
  G = 0.5*(1 - math.sqrt(math.pow(Cab,7)/(math.pow(Cab,7)+math.pow(25,7))))
  ap1 = (1+G) * a1
  ap2 = (1+G) * a2

  Cp1 = math.sqrt(ap1*ap1 + b1*b1)
  Cp2 = math.sqrt(ap2*ap2 + b2*b2)
  Cpp = Cp1 * Cp2

  # Constrain hue between 0 and 2pi
  hp1 = math.atan2(b1, ap1)
  hp2 = math.atan2(b2, ap2)
  if hp1 < 0:
    hp1 = hp1 + 2*pi
  if hp2 < 0:
    hp2 = hp2 + 2*pi

  dL = L1 - L2
  dC = Cp2 - Cp1

  dhp = hp2 - hp1
  if dhp > pi:
    dhp = dhp - 2*pi
  if dhp < -pi:
    dhp = dhp + 2*pi
  if Cpp == 0:
    dhp = 0

  # Note that the defining equations actually need signed hue and chroma
  #   differences, which is different from prior color difference formulae
  dH = 2 * math.sqrt(Cpp) * math.sin(dhp/2)

  # Weighting functions
  Lp = 0.5 * (L1 + L2)
  Cp = 0.5 * (Cp1 + Cp2)

  # Average hue computation
  # Average hue is computed in radians and converted to degrees where needed
  hp = 0.5 * (hp1 + hp2)
  # Identify positions for which abs hue diff exceeds 180 degrees
  if abs(hp1-hp2) > pi:
    hp = hp - pi
  if hp < 0:
    hp = hp + 2*pi

  # If one of chroma values is 0, set mean hue to sum, which is equivalent to
  #   other value
  if Cpp == 0:
    hp = hp1 + hp2

  Lpm502 = (Lp-50) * (Lp-50)
  Sl = 1 + 0.015*Lpm502 / math.sqrt(20+Lpm502)
  Sc = 1 + 0.045*Cp
  T = 1 - 0.17*math.cos(hp - pi/6) + 0.24*math.cos(2*hp) + 0.32*math.cos(3*hp+pi/30) - 0.20*math.cos(4*hp - 63*pi/180)
  Sh = 1 + 0.015 * Cp * T
  ex = (180/pi*hp-275) / 25
  delthetarad = (30*pi/180) * math.exp(-1 * (ex*ex))
  Rc = 2 * math.sqrt(math.pow(Cp,7) / (math.pow(Cp,7) + math.pow(25,7)))
  RT = -1 * math.sin(2*delthetarad) * Rc

  dL = dL / (kl*Sl)
  dC = dC / (kc*Sc)
  dH = dH / (kh*Sh)

  # The CIE 2000 color difference
  return math.sqrt(dL*dL + dC*dC + dH*dH + RT*dC*dH)

