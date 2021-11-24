tam = int(input())
while tam != 0:
  poligonoI = []
  posMG = 0
  MG = 0
  suma = 0
  poligonoI = list(map(int, input().split()))
  for i in range(tam):
    num = poligonoI[i]
    suma += num
    if num > MG:
      MG = num
      posMG = i
  posID  = posII = posMG
  while True:
    sumaP = 0
    for i in range(posII,posID+1):
      sumaP += poligonoI[i]
    cumple = True
    sumaLocal = 0
    j = 1
    while cumple:
      if (posID+j) == len(poligonoI):
        j=-posID
      sumaLocal += poligonoI[posID+j]
      if sumaLocal == sumaP:
        sumaLocal = 0
      elif sumaLocal > sumaP:
        cumple = False
      j+=1
      if j == len(poligonoI):
        j=0
      if (posID+j)==posII:
        if sumaLocal!=0:
          cumple=False
        break

    if cumple:
      res = tam - (suma / sumaP)
      if (tam-res)<3:
        print(-1)
      else:
        print(int(res))
      break
    else:
      sigD = posID+1
      if sigD>len(poligonoI):
        sigD = 0
      sigI = posII-1
      if sigI == -1:
        sigI = len(poligonoI)-1
      valD = sumaP + poligonoI[sigD]
      valI = sumaP + poligonoI[sigI]
      if valI < valD:
        posII = sigI
        sumaP = valI
      else:
        posID = sigD
        sumaP = valD
  tam = int(input())

# 12
# 10 30 20 10 20 40 10 30 20 10 20 20