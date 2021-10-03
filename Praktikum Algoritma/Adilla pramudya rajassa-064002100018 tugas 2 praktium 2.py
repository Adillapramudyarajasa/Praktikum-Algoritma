@author: ASUS


Nama : Adilla Pramudya Rajasa
NIM  : 064002100018
"""



from math import*
print("------------------------------------------------------------------------ ")
print("Membuat kalkulator jarak lingkaran besar antara dua titik di bumi")
print("Calculate the great circle distance between two points on the earth \n")
print("------------------------------------------------------------------------ ")

lat1 = int(input("Latitude 1 : "))
lat2 = int(input("Latitude 2 : "))
lon1 = int(input("Longitude 1 : "))
lon2 = int(input("Longitude 2 : "))
print("\n")
print("#####################################################")

lat1, lat2, lon1, lon2 = map(radians, [lat1, lat2, lon1, lon2])
dlon = lon2 - lon1
dlat = lat2 - lat1
a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
c = 2 * atan2(sqrt(a), sqrt(1-a))
r = 6371
d = c*r

print(f"Jarak antara dua titik adalah {ceil(d)} km")
print("hHasil Pada Jarak Sudah dibulatkan")
print("#################################################### ")
