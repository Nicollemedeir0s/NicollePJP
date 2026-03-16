frutas = ["maçã", "banana", "uva"]
numeros = [1, 2, 3, 4]

print("Primeira fruta:", frutas [0])
print("Última fruta:", frutas [-1])

frutas[1] = "banana-nanica"
print("Após alterar:", frutas)

frutas.append("morango")
frutas.insert(1, "pera")
print("Após adicionar:", frutas)

frutas.remove("uva")
ultima = frutas.pop()
print("Após remover 'uva' e pop():", frutas, "Última removida:", ultima)

print("Listas original 'numeros':", numeros)
print("Somas dos números:", sum(numeros))")
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
numeros.reverse()
print("Reversa:", numeros)
numeros.sort()
print("Ordenada crescente:", numeros)
numeros.sort(reverse=True)
print("Ordenada decrescente:", numeros)

for fruta in frutas:
    print("Fruta:", fruta)

quadrados = [n * n for n in [1, 2, 3, 4, 5]]
print("Quadrados", quadrados)