#
#
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Group 16
#               Aidan Murphy
#               Bobby Hao
#               Jay Ahhlschwede
#               Israel Prado
# Section:      ENGR-102-525
# Assignment:   Lab Topic 8 team
# Date:         12/10/2022

#take input, format into list of digits
tin = str(input('Enter the time: \n'))
diglist = list(tin)

if len(diglist) == 5:
  time1 = str(diglist[0])
  time2 = str(diglist[1])
  time3 = str(diglist[3])
  time4 = str(diglist[4])
elif len(diglist) == 4:
  time1 = str(diglist[0])
  time2 = str(diglist[2])
  time3 = str(diglist[3])
  time4 = str(diglist[1])

# time 1

if time1 == '0':
  a11 = "\b"
  a21 = "\b"
  a31 = "\b"
  b11 = "\b"
  b21 = "\b"
  b31 = "\b"
  c11 = "\b"
  c21 = "\b"
  c31 = "\b"
  d11 = "\b"
  d21 = "\b"
  d31 = "\b"
  e11 = "\b"
  e21 = "\b"
  e31 = "\b"
if time1 == '1':
  a11 = ' '
  a21 = time1
  a31 = ' '
  b11 = time1
  b21 = time1
  b31 = ' '
  c11 = ' '
  c21 = time1
  c31 = ' '
  d11 = ' '
  d21 = time1
  d31 = ' '
  e11 = time1
  e21 = time1
  e31 = time1
if time1 == '2':
  a11 = time1
  a21 = time1
  a31 = time1
  b11 = ' '
  b21 = ' '
  b31 = time1
  c11 = time1
  c21 = time1
  c31 = time1
  d11 = time1
  d21 = ' '
  d31 = ' '
  e11 = time1
  e21 = time1
  e31 = time1
if time1 == '3':
  a11 = time1
  a21 = time1
  a31 = time1
  b11 = ' '
  b21 = ' '
  b31 = time1
  c11 = time1
  c21 = time1
  c31 = time1
  d11 = ' '
  d21 = ' '
  d31 = time1
  e11 = time1
  e21 = time1
  e31 = time1
if time1 == '4':
  a11 = time1
  a21 = ' '
  a31 = time1
  b11 = time1
  b21 = ' '
  b31 = time1
  c11 = time1
  c21 = time1
  c31 = time1
  d11 = ' '
  d21 = ' '
  d31 = time1
  e11 = ' '
  e21 = ' '
  e31 = time1
if time1 == '5':
  a11 = time1
  a21 = time1
  a31 = time1
  b11 = time1
  b21 = ' '
  b31 = ' '
  c11 = time1
  c21 = time1
  c31 = time1
  d11 = ' '
  d21 = ' '
  d31 = time1
  e11 = time1
  e21 = time1
  e31 = time1
if time1 == '6':
  a11 = time1
  a21 = time1
  a31 = time1
  b11 = time1
  b21 = ' '
  b31 = ' '
  c11 = time1
  c21 = time1
  c31 = time1
  d11 = time1
  d21 = ' '
  d31 = time1
  e11 = time1
  e21 = time1
  e31 = time1
if time1 == '7':
  a11 = time1
  a21 = time1
  a31 = time1
  b11 = ' '
  b21 = ' '
  b31 = time1
  c11 = ' '
  c21 = ' '
  c31 = time1
  d11 = ' '
  d21 = ' '
  d31 = time1
  e11 = ' '
  e21 = ' '
  e31 = time1
if time1 == '8':
  a11 = time1
  a21 = time1
  a31 = time1
  b11 = time1
  b21 = ' '
  b31 = time1
  c11 = time1
  c21 = time1
  c31 = time1
  d11 = time1
  d21 = ' '
  d31 = time1
  e11 = time1
  e21 = time1
  e31 = time1
if time1 == '9':
  a11 = time1
  a21 = time1
  a31 = time1
  b11 = time1
  b21 = ' '
  b31 = time1
  c11 = time1
  c21 = time1
  c31 = time1
  d11 = ' '
  d21 = ' '
  d31 = time1
  e11 = time1
  e21 = time1
  e31 = time1

# time 2

if time2 == '1':
  a12 = ' '
  a22 = time2
  a32 = ' '
  b12 = time2
  b22 = time2
  b32 = ' '
  c12 = ' '
  c22 = time2
  c32 = ' '
  d12 = ' '
  d22 = time2
  d32 = ' '
  e12 = time2
  e22 = time2
  e32 = time2
if time2 == '2':
  a12 = time2
  a22 = time2
  a32 = time2
  b12 = ' '
  b22 = ' '
  b32 = time2
  c12 = time2
  c22 = time2
  c32 = time2
  d12 = time2
  d22 = ' '
  d32 = ' '
  e12 = time2
  e22 = time2
  e32 = time2
if time2 == '3':
  a12 = time2
  a22 = time2
  a32 = time2
  b12 = ' '
  b22 = ' '
  b32 = time2
  c12 = time2
  c22 = time2
  c32 = time2
  d12 = ' '
  d22 = ' '
  d32 = time2
  e12 = time2
  e22 = time2
  e32 = time2
if time2 == '4':
  a12 = time2
  a22 = ' '
  a32 = time2
  b12 = time2
  b22 = ' '
  b32 = time2
  c12 = time2
  c22 = time2
  c32 = time2
  d12 = ' '
  d22 = ' '
  d32 = time2
  e12 = ' '
  e22 = ' '
  e32 = time2
if time2 == '5':
  a12 = time2
  a22 = time2
  a32 = time2
  b12 = time2
  b22 = ' '
  b32 = ' '
  c12 = time2
  c22 = time2
  c32 = time2
  d12 = ' '
  d22 = ' '
  d32 = time2
  e12 = time2
  e22 = time2
  e32 = time2
if time2 == '6':
  a12 = time2
  a22 = time2
  a32 = time2
  b12 = time2
  b22 = ' '
  b32 = ' '
  c12 = time2
  c22 = time2
  c32 = time2
  d12 = time2
  d22 = ' '
  d32 = time2
  e12 = time2
  e22 = time2
  e32 = time2
if time2 == '7':
  a12 = time2
  a22 = time2
  a32 = time2
  b12 = ' '
  b22 = ' '
  b32 = time2
  c12 = ' '
  c22 = ' '
  c32 = time2
  d12 = ' '
  d22 = ' '
  d32 = time2
  e12 = ' '
  e22 = ' '
  e32 = time2
if time2 == '8':
  a12 = time2
  a22 = time2
  a32 = time2
  b12 = time2
  b22 = ' '
  b32 = time2
  c12 = time2
  c22 = time2
  c32 = time2
  d12 = time2
  d22 = ' '
  d32 = time2
  e12 = time2
  e22 = time2
  e32 = time2
if time2 == '9':
  a12 = time2
  a22 = time2
  a32 = time2
  b12 = time2
  b22 = ' '
  b32 = time2
  c12 = time2
  c22 = time2
  c32 = time2
  d12 = ' '
  d22 = ' '
  d32 = time2
  e12 = time2
  e22 = time2
  e32 = time2
if time2 == '0':
  a12 = time2
  a22 = time2
  a32 = time2
  b12 = time2
  b22 = ' '
  b32 = time2
  c12 = time2
  c22 = ' '
  c32 = time2
  d12 = time2
  d22 = ' '
  d32 = time2
  e12 = time2
  e22 = time2
  e32 = time2

# time 3

if time3 == '1':
  a13 = ' '
  a23 = time3
  a33 = ' '
  b13 = time3
  b23 = time3
  b33 = ' '
  c13 = ' '
  c23 = time3
  c33 = ' '
  d13 = ' '
  d23 = time3
  d33 = ' '
  e13 = time3
  e23 = time3
  e33 = time3
if time3 == '2':
  a13 = time3
  a23 = time3
  a33 = time3
  b13 = ' '
  b23 = ' '
  b33 = time3
  c13 = time3
  c23 = time3
  c33 = time3
  d13 = time3
  d23 = ' '
  d33 = ' '
  e13 = time3
  e23 = time3
  e33 = time3
if time3 == '3':
  a13 = time3
  a23 = time3
  a33 = time3
  b13 = ' '
  b23 = ' '
  b33 = time3
  c13 = time3
  c23 = time3
  c33 = time3
  d13 = ' '
  d23 = ' '
  d33 = time3
  e13 = time3
  e23 = time3
  e33 = time3
if time3 == '4':
  a13 = time3
  a23 = ' '
  a33 = time3
  b13 = time3
  b23 = ' '
  b33 = time3
  c13 = time3
  c23 = time3
  c33 = time3
  d13 = ' '
  d23 = ' '
  d33 = time3
  e13 = ' '
  e23 = ' '
  e33 = time3
if time3 == '5':
  a13 = time3
  a23 = time3
  a33 = time3
  b13 = time3
  b23 = ' '
  b33 = ' '
  c13 = time3
  c23 = time3
  c33 = time3
  d13 = ' '
  d23 = ' '
  d33 = time3
  e13 = time3
  e23 = time3
  e33 = time3
if time3 == '6':
  a13 = time3
  a23 = time3
  a33 = time3
  b13 = time3
  b23 = ' '
  b33 = ' '
  c13 = time3
  c23 = time3
  c33 = time3
  d13 = time3
  d23 = ' '
  d33 = time3
  e13 = time3
  e23 = time3
  e33 = time3
if time3 == '7':
  a13 = time3
  a23 = time3
  a33 = time3
  b13 = ' '
  b23 = ' '
  b33 = time3
  c13 = ' '
  c23 = ' '
  c33 = time3
  d13 = ' '
  d23 = ' '
  d33 = time3
  e13 = ' '
  e23 = ' '
  e33 = time3
if time3 == '8':
  a13 = time3
  a23 = time3
  a33 = time3
  b13 = time3
  b23 = ' '
  b33 = time3
  c13 = time3
  c23 = time3
  c33 = time3
  d13 = time3
  d23 = ' '
  d33 = time3
  e13 = time3
  e23 = time3
  e33 = time3
if time3 == '9':
  a13 = time3
  a23 = time3
  a33 = time3
  b13 = time3
  b23 = ' '
  b33 = time3
  c13 = time3
  c23 = time3
  c33 = time3
  d13 = ' '
  d23 = ' '
  d33 = time3
  e13 = time3
  e23 = time3
  e33 = time3
if time3 == '0':
  a13 = time3
  a23 = time3
  a33 = time3
  b13 = time3
  b23 = ' '
  b33 = time3
  c13 = time3
  c23 = ' '
  c33 = time3
  d13 = time3
  d23 = ' '
  d33 = time3
  e13 = time3
  e23 = time3
  e33 = time3

# time 4

if time4 == '1':
  a14 = ' '
  a24 = time4
  a34 = ' '
  b14 = time4
  b24 = time4
  b34 = ' '
  c14 = ' '
  c24 = time4
  c34 = ' '
  d14 = ' '
  d24 = time4
  d34 = ' '
  e14 = time4
  e24 = time4
  e34 = time4
if time4 == '2':
  a14 = time4
  a24 = time4
  a34 = time4
  b14 = ' '
  b24 = ' '
  b34 = time4
  c14 = time4
  c24 = time4
  c34 = time4
  d14 = time4
  d24 = ' '
  d34 = ' '
  e14 = time4
  e24 = time4
  e34 = time4
if time4 == '3':
  a14 = time4
  a24 = time4
  a34 = time4
  b14 = ' '
  b24 = ' '
  b34 = time4
  c14 = time4
  c24 = time4
  c34 = time4
  d14 = ' '
  d24 = ' '
  d34 = time4
  e14 = time4
  e24 = time4
  e34 = time4
if time4 == '4':
  a14 = time4
  a24 = ' '
  a34 = time4
  b14 = time4
  b24 = ' '
  b34 = time4
  c14 = time4
  c24 = time4
  c34 = time4
  d14 = ' '
  d24 = ' '
  d34 = time4
  e14 = ' '
  e24 = ' '
  e34 = time4
if time4 == '5':
  a14 = time4
  a24 = time4
  a34 = time4
  b14 = time4
  b24 = ' '
  b34 = ' '
  c14 = time4
  c24 = time4
  c34 = time4
  d14 = ' '
  d24 = ' '
  d34 = time4
  e14 = time4
  e24 = time4
  e34 = time4
if time4 == '6':
  a14 = time4
  a24 = time4
  a34 = time4
  b14 = time4
  b24 = ' '
  b34 = ' '
  c14 = time4
  c24 = time4
  c34 = time4
  d14 = time4
  d24 = ' '
  d34 = time4
  e14 = time4
  e24 = time4
  e34 = time4
if time4 == '7':
  a14 = time4
  a24 = time4
  a34 = time4
  b14 = ' '
  b24 = ' '
  b34 = time4
  c14 = ' '
  c24 = ' '
  c34 = time4
  d14 = ' '
  d24 = ' '
  d34 = time4
  e14 = ' '
  e24 = ' '
  e34 = time4
if time4 == '8':
  a14 = time4
  a24 = time4
  a34 = time4
  b14 = time4
  b24 = ' '
  b34 = time4
  c14 = time4
  c24 = time4
  c34 = time4
  d14 = time4
  d24 = ' '
  d34 = time4
  e14 = time4
  e24 = time4
  e34 = time4
if time4 == '9':
  a14 = time4
  a24 = time4
  a34 = time4
  b14 = time4
  b24 = ' '
  b34 = time4
  c14 = time4
  c24 = time4
  c34 = time4
  d14 = ' '
  d24 = ' '
  d34 = time4
  e14 = time4
  e24 = time4
  e34 = time4
if time4 == '0':
  a14 = time4
  a24 = time4
  a34 = time4
  b14 = time4
  b24 = ' '
  b34 = time4
  c14 = time4
  c24 = ' '
  c34 = time4
  d14 = time4
  d24 = ' '
  d34 = time4
  e14 = time4
  e24 = time4
  e34 = time4

# output

if len(diglist) == 5:
  print(a11 + a21 + a31+ ' ' + a12 + a22 + a32 + '   ' + a13 + a23 + a33 + ' ' + a14 + a24 + a34+" ")
  print(b11 + b21 + b31+ ' ' + b12 + b22 + b32 + ' : ' + b13 + b23 + b33 + ' ' + b14 + b24 + b34+" ")
  print(c11 + c21 + c31+ ' ' + c12 + c22 + c32 + '   ' + c13 + c23 + c33 + ' ' + c14 + c24 + c34+" ")
  print(d11 + d21 + d31+ ' ' + d12 + d22 + d32 + ' : ' + d13 + d23 + d33 + ' ' + d14 + d24 + d34+" ")
  print(e11 + e21 + e31+ ' ' + e12 + e22 + e32 + '   ' + e13 + e23 + e33 + ' ' + e14 + e24 + e34+" ")
elif len(diglist) == 4:
  print(a11 + a21 + a31+ '   ' + a12 + a22 + a32 + ' ' + a13 + a23 + a33+" ")
  print(b11 + b21 + b31+ ' : ' + b12 + b22 + b32 + ' ' + b13 + b23 + b33+" ")
  print(c11 + c21 + c31+ '   ' + c12 + c22 + c32 + ' ' + c13 + c23 + c33+" ")
  print(d11 + d21 + d31+ ' : ' + d12 + d22 + d32 + ' ' + d13 + d23 + d33+" ")
  print(e11 + e21 + e31+ '   ' + e12 + e22 + e32 + ' ' + e13 + e23 + e33+" ")
elif len(diglist) == 5:
  if diglist[0] != ('1' or '2'):
    print('Invalid time')
  elif int(diglist[1]) > 2:
    print('Invalid time')
  elif int(diglist[3]) >= 6:
    print('Invalid time')
elif len(diglist) == 4:
  if int(diglist[2]) >= 6:
    print('Invalid time')
# Character key & Print horizontal list

#take input, format into list of digits
