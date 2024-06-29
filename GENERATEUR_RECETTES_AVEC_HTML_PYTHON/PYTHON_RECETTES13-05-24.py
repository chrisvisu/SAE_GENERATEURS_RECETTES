#Faye_Sonko Galsen thia kaw thia kaname
import csv

def lire_fichier_csv(base_donnees):
    liste_contenu = []  # Créer une liste vide pr stocker le contenu du fichier CSV
    # Ouvrir le fichier CSV
    with open(base_donnees, 'r') as fichier_csv:
        # Lire chaque ligne du fichier CSV
        for ligne in fichier_csv:
            # Diviser la ligne en une liste d'éléments en utilisant la virgule comme séparateur
            elements = ligne.strip().split(';')
            # Ajouter la liste d'éléments à la liste principale
            liste_contenu.append(elements)
            

    return liste_contenu
#______________________________________________________________________________________________________


# Appeler la fonction pour lire le fichier CSV
base_donnees = r"C:\iut\ccbc_.csv"
recipes:list = lire_fichier_csv(base_donnees)
#print(recipes)

def trouver_recettes(donnees, mots):
    # Convertir les mots en minuscules pour une comparaison insensible à la casse
    mots = [mot.lower() for mot in mots]
    # Liste pour stocker les recettes correspondantes
    recettes_correspondantes = []
    
    # Itérer à travers chaque sous-liste de recette
    for recette in donnees[1:]:  # Sauter l'en-tête
        # Combiner tous les éléments de la sous-liste en une seule chaîne
        recette_combinee = " ".join(recette).lower()
        # Vérifier si tous les mots sont dans la chaîne combinée
        if all(mot in recette_combinee for mot in mots):
            recettes_correspondantes.append(recette)
    
    return recettes_correspondantes



# Demander à l'utilisateur de taper cinq mots
mots_entree = []
for i in range(5):
    mot = input(f"Entrez le mot {i+1}: ")
    mots_entree.append(mot)

# Trouver et imprimer les recettes correspondantes
recettes_correspondantes = trouver_recettes(recipes, mots_entree)
for recette in recettes_correspondantes:
    print("Vous pouvez preparer avec vos ingredient:")
    print(recette)























# def find_recipes_with_ingredients(recipes, ingredients):
  #   matching_recipes = []
    
   #  for recipe in recipes:
    #     if all(ingredient in recipe for ingredient in ingredients):
    #        matching_recipes.append(recipe)
    
   #  return matching_recipes

# def main():
    # Liste des recettes (chaque recette est une liste d'ingrédients)

    
    # Lire les quatre ingrédients de l'utilisateur
    # ingredients = input("Entrez quatre ingrédients séparés par une virgule: ").split(",")
    
    # Supprimer les espaces autour des ingrédients
   #  ingredients = [ingredient.strip() for ingredient in ingredients]
    
    # Trouver les recettes correspondantes
    # matching_recipes = find_recipes_with_ingredients(recipes, ingredients)
    
    # Afficher les recettes correspondantes
  #   if matching_recipes:
     #    print("Recettes correspondantes:")
      #   for recipe in matching_recipes:
     #        print(", ".join(recipe))
    # else:
    #   print("Aucune recette ne correspond à ces ingrédients.")
    
# if __name__ == "__main__":
    # main()


# Afficher le contenu de la liste
#ingredient1=input("taper un ingredient1:")#  1er ingredient
#ingredient2=input("taper un ingredient2:")#  eme ingredient
#ingredient3=input("taper un ingredient3:")#  3eme ingredient
#ingredient4=input("taper un ingredient4:")#  4eme ingredient
#ingredient5=input("taper un ingredient5:")#  5eme ingredient
#ingredient6=input("taper un ingredient6:")#  6eme ingredient
#ingredient7=input("taper un ingredient7:")#  7eme ingredient
#liste_ingredient =[4]
#liste_ingredient=[ingredient1,ingredient2,ingredient3,ingredient4]
#port:int=0
#i:int=0
#print(liste_ingredient)
#for bir in contenu: 
 #   for i in range(0,3):
  #      for liste_ingredient[i] in bir :    
   #         print(liste_ingredient[i])
    #        port=port + 1
     #       if  port==3 :
     #           print(bir)
#port=0

