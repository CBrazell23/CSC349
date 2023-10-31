import sys


def IJM1Func(i, j):
    if(str1[j - 1] == 'A'):
        return output[i - 1][j] + A0
    elif(str1[j - 1] == 'C'):
        return output[i - 1][j] + C0
    elif (str1[j - 1] == 'G'):
        return output[i - 1][j] + G0
    elif (str1[j - 1] == 'T'):
        return output[i - 1][j] + T0


def IM1JFunc(i, j):
    if(str2[i - 1] == 'A'):
        return output[i][j - 1] + A0
    elif(str2[i - 1] == 'C'):
        return output[i][j - 1] + C0
    elif (str2[i - 1] == 'G'):
        return output[i][j - 1] + G0
    elif (str2[i - 1] == 'T'):
        return output[i][j - 1] + T0


def IM1JM1Func(i, j):
    if(str1[i - 1] == 'A' and str2[j - 1] == 'A'):
        return output[j - 1][i - 1] + AA
    elif(str1[i - 1] == 'A' and str2[j - 1] == 'C'):
        return output[j - 1][i - 1] + AC
    elif (str1[i - 1] == 'A' and str2[j - 1] == 'G'):
        return output[j - 1][i - 1] + AG
    elif (str1[i - 1] == 'A' and str2[j - 1] == 'T'):
        return output[j - 1][i - 1] + AT
    elif(str1[i - 1] == 'C' and str2[j - 1] == 'A'):
        return output[j - 1][i - 1] + AC
    elif(str1[i - 1] == 'C' and str2[j - 1] == 'C'):
        return output[j - 1][i - 1] + CC
    elif (str1[i - 1] == 'C' and str2[j - 1] == 'G'):
        return output[j - 1][i - 1] + CG
    elif (str1[i - 1] == 'C' and str2[j - 1] == 'T'):
        return output[j - 1][i - 1] + CT
    elif (str1[i - 1] == 'G' and str2[j - 1] == 'A'):
        return output[j - 1][i - 1] + AG
    elif (str1[i - 1] == 'G' and str2[j - 1] == 'C'):
        return output[j - 1][i - 1] + CG
    elif (str1[i - 1] == 'G' and str2[j - 1] == 'G'):
        return output[j - 1][i - 1] + GG
    elif (str1[i - 1] == 'G' and str2[j - 1] == 'T'):
        return output[j - 1][i - 1] + GT
    elif (str1[i - 1] == 'T' and str2[j - 1] == 'A'):
        return output[j - 1][i - 1] + AT
    elif (str1[i - 1] == 'T' and str2[j - 1] == 'C'):
        return output[j - 1][i - 1] + CT
    elif (str1[i - 1] == 'T' and str2[j - 1] == 'G'):
        return output[j - 1][i - 1] + GT
    elif (str1[i - 1] == 'T' and str2[j - 1] == 'T'):
        return output[j - 1][i - 1] + TT


fileToRead = sys.argv[1]
f = open(fileToRead, "r")
data = []
for line in f:
    data.append(line)

str1 = data[0]
str2 = data[1]

Vals = data[3]
ValsSplit = Vals.split()
AA = int(ValsSplit[1])
AC = int(ValsSplit[2])
AG = int(ValsSplit[3])
AT = int(ValsSplit[4])
A0 = int(ValsSplit[5])
Vals = data[4]
ValsSplit = Vals.split()
CC = int(ValsSplit[2])
CG = int(ValsSplit[3])
CT = int(ValsSplit[4])
C0 = int(ValsSplit[5])
Vals = data[5]
ValsSplit = Vals.split()
GG = int(ValsSplit[3])
GT = int(ValsSplit[4])
G0 = int(ValsSplit[5])
Vals = data[6]
ValsSplit = Vals.split()
TT = int(ValsSplit[4])
T0 = int(ValsSplit[5])
Vals = data[7]
ValsSplit = Vals.split()
O0 = int(ValsSplit[5])

sequences = [0] * 2

output = [[0 for j in range(len(str1))] for i in range(len(str2))]


for i in range(1, len(str1)):
    if(str1[0] == 'A'):
        output[0][i] = output[0][i - 1] + A0
    elif(str1[0] == 'C'):
        output[0][i] = output[0][i - 1] + C0
    elif (str1[0] == 'G'):
        output[0][i] = output[0][i - 1] + G0
    elif (str1[0] == 'T'):
        output[0][i] = output[0][i - 1] + T0

for j in range(1, len(str2)):
    if(str2[0] == 'A'):
        output[j][0] = output[j - 1][0] + A0
    elif(str2[0] == 'C'):
        output[j][0] = output[j - 1][0] + C0
    elif (str2[0] == 'G'):
        output[j][0] = output[j - 1][0] + G0
    elif (str2[0] == 'T'):
        output[j][0] = output[j - 1][0] + T0

for i in range(1, len(str2)):
    for j in range(1, len(str1)):
        IJM1 = IJM1Func(i, j)
        IM1J = IM1JFunc(i, j)
        IM1JM1 = IM1JM1Func(j, i)
        output[i][j] = max(IJM1, IM1J, IM1JM1)

sequence = ""

i = len(str1) - 1
j = len(str2) - 1
myBool = 1
while(not(i == 0 and j == 0)):
    if str2[j - 1] == 'A' and output[j - 1][i] + A0 == output[j][i]:
        sequence += "U"
        j -= 1
    elif str2[j - 1] == 'C' and output[j - 1][i] + C0 == output[j][i]:
        sequence += "U"
        j -= 1
    elif str2[j - 1] == 'G' and output[j - 1][i] + G0 == output[j][i]:
        sequence += "U"
        j -= 1
    elif str2[j - 1] == 'T' and output[j - 1][i] + T0 == output[j][i]:
        sequence += "U"
        j -= 1
    elif str1[i - 1] == 'A' and output[j][i - 1] + A0 == output[j][i]:
        sequence += "L"
        i -= 1
    elif str1[i - 1] == 'C' and output[j][i - 1] + C0 == output[j][i]:
        sequence += "L"
        i -= 1
    elif str1[i - 1] == 'G' and output[j][i - 1] + G0 == output[j][i]:
        sequence += "L"
        i -= 1
    elif str1[i - 1] == 'T' and output[j][i - 1] + T0 == output[j][i]:
        sequence += "L"
        i -= 1
    else:
        sequence += "D"
        i -= 1
        j -= 1

newSequence = sequence[::-1]
newStr1 = ""
newStr2 = ""
i = 0
j = 0
for x in newSequence:
    if x == 'L':
        newStr2 += '- '
        newStr1 += str1[i] + " "
        i += 1
    elif x == 'U':
        newStr1 += '- '
        newStr2 += str2[j] + " "
        j += 1
    elif x == 'D':
        newStr1 += str1[i] + " "
        newStr2 += str2[j] + " "
        i += 1
        j += 1

newStr1 = newStr1.strip()
newStr2 = newStr2.strip()
print("x: " + newStr1)
print("y: " + newStr2)
print("Score: " + str(output[len(str2) - 1][len(str1) - 1]))