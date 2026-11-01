from list_ import List

l = List()

canciones = [
    ["Do I Wanna Know?", "Arctic Monkeys", 272, 950000],
    ["505", "Arctic Monkeys", 253, 870000],
    ["R U Mine?", "Arctic Monkeys", 201, 810000],
    ["Yellow", "Coldplay", 269, 780000],
    ["Viva La Vida", "Coldplay", 242, 920000],
    ["Believer", "Imagine Dragons", 204, 1100000],
    ["Demons", "Imagine Dragons", 177, 760000],
    ["Shape of You", "Ed Sheeran", 233, 1500000],
    ["Perfect", "Ed Sheeran", 263, 980000],
    ["Blinding Lights", "The Weeknd", 200, 1700000],
    ["Starboy", "The Weeknd", 230, 1300000],
    ["Bad Guy", "Billie Eilish", 194, 1150000],
    ["Lovely", "Billie Eilish", 201, 990000],
    ["Thunder", "Imagine Dragons", 187, 850000],
    ["Numb", "Linkin Park", 185, 1200000],
    ["In The End", "Linkin Park", 216, 1450000],
    ["Faint", "Linkin Park", 162, 700000],
    ["Smells Like Teen Spirit", "Nirvana", 301, 890000],
    ["Come As You Are", "Nirvana", 219, 730000],
    ["Bohemian Rhapsody", "Queen", 354, 1600000],
    ["Don't Stop Me Now", "Queen", 210, 940000],
    ["Yesterday", "Beatles", 125, 680000],
    ["Hey Jude", "Beatles", 431, 1350000],
    ["One", "Metallica", 447, 910000],
    ["Nothing Else Matters", "Metallica", 388, 1020000],
    ["Zombie", "Cranberries", 306, 890000],
    ["Radioactive", "Imagine Dragons", 186, 1120000],
    ["Photograph", "Ed Sheeran", 258, 840000],
    ["Fix You", "Coldplay", 295, 970000],
    ["Adventure of a Lifetime", "Coldplay", 251, 690000],
    ["Happier Than Ever", "Billie Eilish", 298, 780000],
    ["Lose Yourself", "Eminem", 326, 1400000],
    ["Without Me", "Eminem", 290, 1190000],
    ["Mockingbird", "Eminem", 251, 1010000],
    ["Halo", "Beyonce", 261, 870000],
    ["Rolling in the Deep", "Adele", 228, 1240000],
    ["Someone Like You", "Adele", 285, 980000],
    ["Take On Me", "A-ha", 225, 760000],
    ["Counting Stars", "OneRepublic", 257, 1180000],
    ["Apologize", "OneRepublic", 208, 720000]
]
for cancion in canciones:
    l.append(cancion)

cancionMasLarga = l[0]

for cancion in l:
    if cancion[2] > cancionMasLarga[2]:
        cancionMasLarga = cancion

print("Canción más larga:")
print(cancionMasLarga)

for cancion in l:
    if cancion[2]>cancionMasLarga[2]:
        cancionMasLarga=cancion



def by_reproducciones(cancion):
    return cancion[3]

l.add_criterion("reproducciones", by_reproducciones)

l.sort_by_criterion("reproducciones")

print("TOP 5")

for i in range(1, 6):
    print(l[-i])

print("TOP 10")

for i in range(1, 11):
    print(l[-i])
    
print("TOP 40")

for i in range(1,41):
    print(l[-i])

print("Canciones de Arctic Monkeys:")
for cancion in l:
    if cancion[1]=="Arctic Monkeys":
        print(cancion)

print("Artistas de una sola palabra:")

mostrados = []

for cancion in l:
    if len(cancion[1].split()) == 1 and cancion[1] not in mostrados:
        print(cancion[1])
        mostrados.append(cancion[1])



       



