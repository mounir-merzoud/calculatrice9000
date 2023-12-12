# Liste pour stocker les résultats
historique_calculs = []

num1 = float(input("Enter the 1st number: "))
operator = input("Enter an operator (+ - * / % ** or a custom symbol): ")
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print("A + B =", result)
elif operator == "-":
    result = num1 - num2
    print("A - B =", result)
elif operator == "*":
    result = num1 * num2
    print("A * B =", result)
elif operator == "/" and num2 != 0:
    result = num1 / num2
    print("A / B =", result)
elif operator == "%" and num2 != 0:
    result = num1 % num2
    print("A % B =", result)
elif operator == "**" and num2 != 0:
    result = num1 ** num2
    print("A ** B =", result)
elif operator == "//" and num2 != 0:
    result = num1 // num2
    print("A // B =", result)
    # Ajouter le résultat à l'historique
    historique_calculs.append(f"{num1} // {num2} = {result}")
else:
    print("L'opération n'est pas valide")

# Ajouter une vérification pour le cas où num2 est égal à zéro
if (operator == "/" or operator == "%" or operator == "//") and num2 == 0:
    print("Erreur: Division par zéro.")
else:
    # Ajouter le résultat à l'historique pour les autres opérations réussies
    historique_calculs.append(f"{num1} {operator} {num2} = {result}")

# Afficher l'historique des calculs
print("\nHistorique des calculs:")
for calcul in historique_calculs:
    print(calcul)
