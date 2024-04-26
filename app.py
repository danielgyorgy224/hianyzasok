hianyzasok = []
with open("hianyzasok.txt", "r", encoding="utf-8") as fi:
    for sor in fi:
        hianyzasok.append(list(map(int, sor.strip().split(", "))))
        
def osszes_hianyzas(l):
    o = 0
    for h in l:
        for n in h:
            o+=n
    return o

def het_nohianyzas(l):
    i = 0
    while i < len(l) and sum(l[i]) != 0:
        i+=1
    if i<len(l):
        return True
    else:
        return False

def het_5nelkevesebb(l):
    i = 0
    while i < len(l) and sum(l[i]) < 5:
        i+=1
    if i<len(l):
        return True
    else:
        return False

print(f"1. feladat: {osszes_hianyzas(hianyzasok)} óra hiányzás volt összesen.")

if het_nohianyzas(hianyzasok):
    print("2. feladat: Volt olyan hét, amikor nem volt hiányzó.")
else:
    print("2. feladat: Nem volt olyan hét, amikor nem volt hiányzó.")

if het_5nelkevesebb(hianyzasok):
    print("3. feladat: Volt olyan hét, amikor ötnél kevesebb hiányzó volt.")
else:
    print("3. feladat: Nem volt olyan hét, amikor ötnél kevesebb hiányzó volt.")