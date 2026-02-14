# 📝 Aide-Mémoire Git - Commandes Essentielles

## 🚀 COMMANDES DE BASE

### Configuration initiale (une seule fois)
```bash
# Configurer votre identité
git config --global user.name "Votre Nom"
git config --global user.email "votre@email.com"

# Vérifier la configuration
git config --list
```

---

## 📦 DÉMARRAGE D'UN PROJET

### Nouveau projet local
```bash
# Dans votre dossier moroccan-recipes/
cd /chemin/vers/moroccan-recipes

# Initialiser Git
git init

# Ajouter tous les fichiers
git add .

# Premier commit
git commit -m "Initial commit - Application complète"

# Lier à GitHub (après avoir créé le repo sur github.com)
git remote add origin https://github.com/VOTRE_USERNAME/moroccan-recipes.git

# Renommer la branche principale
git branch -M main

# Envoyer sur GitHub
git push -u origin main
```

### Cloner un projet existant
```bash
# Cloner depuis GitHub
git clone https://github.com/VOTRE_USERNAME/moroccan-recipes.git

# Entrer dans le dossier
cd moroccan-recipes
```

---

## 📝 MODIFICATIONS QUOTIDIENNES

### Workflow standard
```bash
# 1. Vérifier l'état
git status

# 2. Ajouter les fichiers modifiés
git add .                    # Tous les fichiers
git add index.html          # Un fichier spécifique
git add styles.css app.js   # Plusieurs fichiers

# 3. Créer un commit
git commit -m "Description claire de vos modifications"

# 4. Envoyer sur GitHub
git push
```

### Exemples de commits
```bash
git commit -m "Ajout de 5 nouvelles recettes"
git commit -m "Correction bug affichage favoris"
git commit -m "Mise à jour des styles CSS"
git commit -m "Optimisation des images"
git commit -m "Ajout de la fonctionnalité d'impression"
```

---

## 🔍 CONSULTER L'HISTORIQUE

```bash
# Voir l'historique des commits
git log

# Version courte
git log --oneline

# Avec graphique
git log --oneline --graph

# Derniers 5 commits
git log -5

# Voir les modifications d'un fichier
git log -p index.html
```

---

## ↩️ ANNULER DES MODIFICATIONS

### Avant le commit (fichier modifié)
```bash
# Annuler les modifications d'un fichier
git checkout -- index.html

# Annuler toutes les modifications
git checkout -- .
```

### Après le add mais avant le commit
```bash
# Retirer un fichier du staging
git reset HEAD index.html

# Retirer tous les fichiers
git reset HEAD .
```

### Après le commit (localement seulement)
```bash
# Annuler le dernier commit (garder les modifications)
git reset --soft HEAD~1

# Annuler le dernier commit (supprimer les modifications)
git reset --hard HEAD~1
```

### Après le push (sur GitHub)
```bash
# Créer un commit qui annule les changements
git revert HEAD

# Puis push
git push
```

---

## 🌿 BRANCHES

### Créer et utiliser des branches
```bash
# Créer une nouvelle branche
git branch nouvelle-fonctionnalite

# Changer de branche
git checkout nouvelle-fonctionnalite

# Créer ET changer de branche (raccourci)
git checkout -b nouvelle-fonctionnalite

# Voir toutes les branches
git branch

# Retourner à main
git checkout main

# Fusionner une branche dans main
git checkout main
git merge nouvelle-fonctionnalite

# Supprimer une branche
git branch -d nouvelle-fonctionnalite
```

---

## 🔄 SYNCHRONISATION

### Récupérer les modifications de GitHub
```bash
# Télécharger les modifications
git fetch

# Télécharger ET fusionner
git pull

# Pull d'une branche spécifique
git pull origin main
```

### Envoyer sur GitHub
```bash
# Première fois
git push -u origin main

# Ensuite
git push

# Push d'une branche spécifique
git push origin nouvelle-fonctionnalite
```

---

## 🏷️ TAGS (Versions)

```bash
# Créer un tag
git tag v1.0.0

# Tag avec message
git tag -a v1.0.0 -m "Version 1.0.0 - Release initiale"

# Lister les tags
git tag

# Envoyer un tag sur GitHub
git push origin v1.0.0

# Envoyer tous les tags
git push --tags

# Supprimer un tag local
git tag -d v1.0.0

# Supprimer un tag distant
git push origin --delete v1.0.0
```

---

## 🔍 INFORMATION

```bash
# État actuel
git status

# Différences non commitées
git diff

# Différences dans un fichier
git diff index.html

# Différences commitées
git diff --staged

# Informations sur le remote
git remote -v

# Branches locales et distantes
git branch -a
```

---

## 🧹 NETTOYAGE

```bash
# Supprimer les fichiers non suivis
git clean -n   # Prévisualiser
git clean -f   # Supprimer

# Supprimer fichiers et dossiers non suivis
git clean -fd
```

---

## 🆘 SITUATIONS COURANTES

### Situation 1 : Oublié d'ajouter un fichier
```bash
# Après avoir commité
git add fichier_oublie.html
git commit --amend --no-edit
git push -f  # Attention : force push !
```

### Situation 2 : Mauvais message de commit
```bash
git commit --amend -m "Nouveau message correct"
git push -f  # Si déjà pushé
```

### Situation 3 : Conflit lors du merge
```bash
# Git marque les conflits dans les fichiers
# Ouvrir les fichiers et résoudre manuellement
# Chercher <<<<<<< et =======

# Après résolution
git add fichier_resolu.html
git commit -m "Résolution du conflit"
```

### Situation 4 : Tout casser et recommencer
```bash
# Annuler TOUTES les modifications locales
git reset --hard HEAD
git clean -fd

# Revenir à l'état de GitHub
git fetch origin
git reset --hard origin/main
```

---

## 📋 COMMANDES UTILES

### Stash (mettre de côté)
```bash
# Sauvegarder les modifications temporairement
git stash

# Lister les stash
git stash list

# Réappliquer le dernier stash
git stash pop

# Réappliquer un stash spécifique
git stash apply stash@{0}

# Supprimer un stash
git stash drop stash@{0}
```

### Recherche
```bash
# Chercher dans les fichiers
git grep "recherche"

# Chercher dans l'historique
git log --all --grep="mot-clé"

# Qui a modifié cette ligne ?
git blame index.html
```

---

## 🎯 WORKFLOW COMPLET EXEMPLE

### Ajouter une nouvelle recette
```bash
# 1. Vérifier l'état
git status

# 2. Créer une branche (optionnel)
git checkout -b ajout-recette-couscous

# 3. Modifier recipes-ar.json
# (ajoutez votre recette)

# 4. Vérifier les modifications
git status
git diff recipes-ar.json

# 5. Ajouter et commiter
git add recipes-ar.json
git commit -m "Ajout recette couscous royal"

# 6. Push
git push origin ajout-recette-couscous

# 7. Sur GitHub : Create Pull Request

# 8. Après merge : revenir à main
git checkout main
git pull

# 9. Supprimer la branche
git branch -d ajout-recette-couscous
```

---

## 🚨 COMMANDES À ÉVITER

### ⚠️ Dangereuses
```bash
# Force push (écrase l'historique distant)
git push -f
# Utilisez seulement si vous êtes CERTAIN !

# Reset hard (perd les modifications)
git reset --hard
# Sauvegardez avant !

# Clean (supprime les fichiers)
git clean -f
# Prévisualisez avec -n d'abord !
```

---

## 💡 ASTUCES

### Alias pratiques
```bash
# Configurer des raccourcis
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit

# Utiliser
git st     # au lieu de git status
git co main # au lieu de git checkout main
```

### Ignorer les fichiers
```bash
# Créer/éditer .gitignore
echo "node_modules/" >> .gitignore
echo "*.log" >> .gitignore
echo ".env" >> .gitignore

# Ignorer un fichier déjà tracké
git rm --cached fichier.log
```

---

## 📚 RESSOURCES

### Aide Git
```bash
# Aide générale
git help

# Aide sur une commande
git help commit
git commit --help
```

### Documentation
- https://git-scm.com/doc
- https://docs.github.com
- https://training.github.com

### Visualisation
- GitKraken (GUI)
- GitHub Desktop (GUI)
- SourceTree (GUI)

---

## ✅ CHECKLIST QUOTIDIENNE

```bash
# Avant de commencer à travailler
git status          # État actuel
git pull           # Récupérer les mises à jour

# Pendant le travail
git status         # Vérifier régulièrement

# Après modifications
git add .          # Ajouter les fichiers
git commit -m "..." # Commiter
git push           # Envoyer

# Fin de journée
git status         # Vérifier que tout est clean
```

---

## 🎓 POUR ALLER PLUS LOIN

### Commandes avancées
```bash
# Rebase (réorganiser l'historique)
git rebase main

# Cherry-pick (copier un commit)
git cherry-pick abc1234

# Bisect (trouver un bug)
git bisect start
git bisect bad
git bisect good v1.0.0

# Submodules
git submodule add https://github.com/...
git submodule update --init
```

---

**💡 Conseil** : Gardez ce fichier ouvert pendant votre travail !

**🔖 Marque-page** : Les commandes les plus utilisées sont dans les sections "MODIFICATIONS QUOTIDIENNES" et "WORKFLOW COMPLET EXEMPLE"
