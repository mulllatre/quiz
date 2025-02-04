player_name = input("Bienvenue sur notre Quiz, veuillez indiquer votre nom de joueur : ")

print("\nCombien de question veux tu", f"{player_name}", ":\n", "1. 5 questions\n", "2. 15 questions\n", "3. 25 questions\n")
nombre_question = int(input("-> "))

question = [
    {"question": "Quel est le plus grand océan de la Terre ?", 
     "reponse": ["Océan Atlantique", "Océan Indien", "Océan Pacifique"],
     "bonne_reponse": "Océan Pacifique"},

    {"question": "Qui a peint la Joconde ?", 
     "reponse": ["Vincent Van Gogh", "Pablo Picasso", "Léonard de Vinci"],
     "bonne_reponse": "Léonard de Vinci"},

    {"question": "Quel est le plus grand pays du monde ?", 
     "reponse": ["Chine", "Russie", "États-Unis"],
     "bonne_reponse": "Russie"},

    {"question": "Combien de continents y a-t-il sur Terre ?", 
     "reponse": ["5", "6", "7"],
     "bonne_reponse": "7"},

    {"question": "Quel est le plus haut sommet du monde ?", 
     "reponse": ["Mont Everest", "Mont Kilimandjaro", "Mont Fuji"],
     "bonne_reponse": "Mont Everest"},

    {"question": "Quel est l'élément chimique dont le symbole est H ?", 
     "reponse": ["Helium", "Hydrogène", "Oxygène"],
     "bonne_reponse": "Hydrogène"},

    {"question": "Quel est le nom de la capitale de la France ?", 
     "reponse": ["Lyon", "Paris", "Marseille"],
     "bonne_reponse": "Paris"},

    {"question": "Quel est le plus grand mammifère terrestre ?", 
     "reponse": ["Girafe", "Éléphant d'Afrique", "Rhinocéros"],
     "bonne_reponse": "Éléphant d'Afrique"},

    {"question": "Dans quelle ville se trouve le Colisée ?", 
     "reponse": ["Rome", "Athènes", "Paris"],
     "bonne_reponse": "Rome"},

    {"question": "Quel est l'organe principal du système respiratoire humain ?", 
     "reponse": ["Le cœur", "Les poumons", "Le foie"],
     "bonne_reponse": "Les poumons"},

    {"question": "Quelle est la couleur du sang humain en dehors du corps ?", 
     "reponse": ["Rouge", "Bleu", "Vert"],
     "bonne_reponse": "Rouge"},

    {"question": "Quel est l'élément chimique dont le symbole est O ?", 
     "reponse": ["Ozone", "Oxygène", "Or"],
     "bonne_reponse": "Oxygène"},

    {"question": "Quel est le plus petit pays du monde ?", 
     "reponse": ["Monaco", "Vatican", "Luxembourg"],
     "bonne_reponse": "Vatican"},

    {"question": "Quel est le nom de l'astre qui éclaire la Terre ?", 
     "reponse": ["La Lune", "Le Soleil", "Mars"],
     "bonne_reponse": "Le Soleil"},

    {"question": "Qui a écrit 'Les Misérables' ?", 
     "reponse": ["Victor Hugo", "Emile Zola", "Marcel Proust"],
     "bonne_reponse": "Victor Hugo"},

    {"question": "En quelle année l'Homme a-t-il marché sur la Lune pour la première fois ?", 
     "reponse": ["1969", "1971", "1965"],
     "bonne_reponse": "1969"},

    {"question": "Combien de joueurs compose une équipe de football ?", 
     "reponse": ["10", "11", "12"],
     "bonne_reponse": "11"},

    {"question": "Quel est le nom du créateur de Facebook ?", 
     "reponse": ["Steve Jobs", "Mark Zuckerberg", "Bill Gates"],
     "bonne_reponse": "Mark Zuckerberg"},

    {"question": "Quel est le plus grand désert du monde ?", 
     "reponse": ["Le Sahara", "L'Antarctique", "Le Gobi"],
     "bonne_reponse": "Le Sahara"},

    {"question": "Quel est le symbole chimique du fer ?", 
     "reponse": ["Fe", "F", "Fr"],
     "bonne_reponse": "Fe"},

    {"question": "Quel est l'animal terrestre le plus rapide ?", 
     "reponse": ["Cheetah", "Lion", "Antilope"],
     "bonne_reponse": "Cheetah"},

    {"question": "Qui a découvert la théorie de la relativité ?", 
     "reponse": ["Isaac Newton", "Albert Einstein", "Marie Curie"],
     "bonne_reponse": "Albert Einstein"},

    {"question": "Quel est le pays d'origine du sushi ?", 
     "reponse": ["Chine", "Japon", "Corée"],
     "bonne_reponse": "Japon"},

    {"question": "Quel est l'organe qui permet de digérer les aliments dans le corps humain ?", 
     "reponse": ["Le cœur", "L'estomac", "Le cerveau"],
     "bonne_reponse": "L'estomac"},

    {"question": "Qui a composé la célèbre 'Symphonie n°9' ?", 
     "reponse": ["Beethoven", "Mozart", "Chopin"],
     "bonne_reponse": "Beethoven"}
]
score = 0

if nombre_question == 1:
    nq = 5
elif nombre_question == 2:
    nq = 15
elif nombre_question == 3:
    nq = 25

for i in range(nq):
    quiz = question[i]
    print(f"\nQuestion : {quiz['question']}\n")

    for j in range(len(quiz["reponse"])):
        if j == 0:
            print("A.", quiz["reponse"][j])
        elif j == 1:
            print("B.", quiz["reponse"][j])
        elif j == 2:
            print("C.", quiz["reponse"][j])

    joueur_reponse = input("\nDonne ta reponse : ").upper()

    if joueur_reponse == 'A' and quiz["reponse"][0] == quiz["bonne_reponse"]:
        score += 1
    elif joueur_reponse == 'B' and quiz["reponse"][1] == quiz["bonne_reponse"]:
        score += 1
    elif joueur_reponse == 'C' and quiz["reponse"][2] == quiz["bonne_reponse"]:
        score += 1

print(f"\nTon score final {player_name} est : {score}")