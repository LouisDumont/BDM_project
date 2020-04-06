*****************************************************
*** How to edit Prototype_1 for simple adventures ***
*****************************************************

*** Avant de commencer ***

- Si vous commencez � �crire une nouvelle aventure, assurez-vous au pr�alable 
que votre contenu local est � jour avec "git pull" / "git status"

- Assurez-vous que vous travaillez bien dans le dossier Prototype_1 (et pas un autre)

*** Comment modifier les fichiers ***

- Ouvrez les fichiers "main.py", "metadata.py" et "moments.py" avec votre logiciel de traitement de texte
ou IDE (notepad peut faire l'affaire, je recommande Atom ou Visual Studio si vous voulez voir un peu mieux
ce que vous faites).

- Dans "moments.py", d�finissez autant de classes qu'il y aura de noeuds dans votre intrigue.
Pour d�finir une classe, copiez collez un exemple d�j� pr�sent en changeant le nom (avec une majuscule)
et la description (le texte entre guillemets). La description sera le texte affich� dans le noeud.
Pour un retour � la ligne, ins�rez "\n" dans le texte.

- Dans metadata.py, allez en dessous de "# Setting up the environment"
Cr�ez tous les noeuds en tapant pour chacun la ligne:
<nom_du_noeud> = <nom_de_la_classe_cr�e_pr�c�demement>()
Tous vos noeuds sont cr�es, reste � les lier entre eux

- Toujours dans metadata.py, allez � "# Setting up the navigation links" puis "# Related to the moments"
Ajoutez tous les choix de navigation de la fa�on suivante: pour un choix ammenant d'un noeud A � un noeud B
<nom_du_noeud_A>.add_choice(<texte affich� pour ce choix>, <nom_du_noeud_B>)

- Il ne reste plus qu'� lancer lier le premier noeud au d�marage du jeu:
Dans "main.py", remplacez la derni�re ligne par <nom_du_premier_noeud>.trigger()
Attention, respectez bien l'indentation ici.

*** Pour d�ployer vos changements sur le repository ***
(que je puisse refaire le .exe)

- dans un terminal, allez jusqu'au dossier Prototype_1
- tapez "git add -A" puis enter
- tapez "git commit -m "feat(Prototype_1): <quelques mots en anglais d�crivant ce que vous avez fait>" "
- tapez "git push"

*** Si vous voulez tester vos changements sans attendre le .exe ***

- installez Python 3.6 (depuis le site de Python)

- installez un IDE (pizo par exemple) (idem, dispo directement sur internet) et ex�cutez main.py avec lui
ou
depuis un terminal naviguez jusqu'� Prototype_1 et tapez "python main.py"




