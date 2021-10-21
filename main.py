fisier = open("C:/Facultate/anul III sem 1/LFTC/Lab 2/venv/text.txt")

operatori = ['=', '+', '-', '*', '%', '/', '++', '==', '!=', '<', '>', '>=', '<=', '+=', '-=']

separatori = [';', '{', '}', '(', ')', '<<', '>>', ',']

cuvinte_cheie = ['int', 'float', 'bool', 'cin', 'cout', 'main()', '#include', '<iostream>', 'using', 'namespace', 'std',
                 'while', 'for', 'if', 'else', 'return']

lista = []

program = fisier.read().split("\n")

lista_afisare_constante = []  # pentru afisare
lista_afisare_identificatori = []  # pentru afisare

for linie in program:
    atomi = linie.split(' ')
    for atom in atomi:
        if atom in operatori:
            lista.append(atom.strip())
        elif atom in separatori:
            lista.append(atom.strip())
        elif atom in cuvinte_cheie:
            lista.append(atom.strip())
        elif atom.isnumeric():
            lista.append(atom.strip())
            lista_afisare_constante.append(atom.strip())
        else:  # pentru float
            aux = atom.split('.')
            if aux[0].isnumeric() is True and aux[1].isnumeric() is True:
                lista.append(atom.strip())
                lista_afisare_constante.append(atom.strip())  # pentru afisare
            elif atom.strip() != "":
                lista.append(atom.strip())
                lista_afisare_identificatori.append(atom.strip())  # pentru afisare

# afisare raw
# for element in lista:
#   print(element)

# afisare sortata, fara duplicate
lista = set(lista)

print("Operatori:")
lista_afisare = []
for atom in lista:
    if atom in operatori:
        lista_afisare.append(atom)
print(lista_afisare)

print("\nSeparatori:")
for atom in lista:
    if atom in separatori:
        lista_afisare.append(atom)
print(lista_afisare)

print("\nCuvinte cheie:")
for atom in lista:
    if atom in cuvinte_cheie:
        lista_afisare.append(atom)
print(lista_afisare)

print("\nConstante:")
lista_afisare_constante = set(lista_afisare_constante)
print(lista_afisare_constante)

print("\nIdentificatori:")
lista_afisare_identificatori = set(lista_afisare_identificatori)
print(lista_afisare_identificatori)
