# fibonacci sorozat első 20 tagja

# a1 = 1
# a2 = 1

# print('1 1', end=' ')
# for i in range(18):
#     uj = a1 + a2
#     print(f'{uj}', end=' ')
#     a1 = a2
#     a2 = uj
#           0       1         2          3
# lista = ['cica', 'kutya', 'pingvin', 'tigris']

# len(Összetett_adatszerkezet_neve) -> visszaadja a lista hosszát

# print(lista[2])

# lista = [1, 2, 3, 4, 5, 12, 32, 44, 50]

# lista[3] = 26

# for x in lista:
#     print(x, end=' ')

# for i in range(len(lista)):
#     lista[i] = 26
# print('\n')
# for x in lista:
#     print(x, end=' ')

# t = [25, 36, 44, 34, 31, 69, 11, 10, 99, 42, 23]
# # t = [2, 3, 4]
# # összegzés tétele
# sum = 0
# for x in t:
#     sum += x

# print(f'az elemek összege: {sum}')
# print(f'az elemek átlaga: {sum / len(t)}')

# szoveg = 'megszentségteleníthetetlenségeitekért'

# print(len(szoveg))
# print(szoveg[0])


# karakter_lista = ['f', 'u', 'c', 'k']

# szo = ""
# for c in karakter_lista:
#     szo += c
# print(szo + ' you!')

# szorzat = 1
# for i in range(10):
#     szorzat *= 2
#     print(szorzat)


# első 100 prímszám:
# szam = 2
# primekSzama = 0
# while primekSzama < 100:
#     osztokSzama = 0
#     for oszto in range(2, szam//2 + 1):
#         if szam % oszto == 0: 
#             osztokSzama += 1
#     if osztokSzama == 0:
#         primekSzama += 1
#         print(f'{primekSzama}: {szam}')
#     szam += 1

szam = int(input("írj be egy számot: "))

print(f'{szam} osztói:', end= ' ')

print(1, end=' ')

if szam != 1:
    for oszto in range(2, szam//2 + 1):
        if szam % oszto == 0:
            print(oszto, end=' ')
    print(szam, end=' ')