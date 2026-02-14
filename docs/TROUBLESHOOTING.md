# 🔧 Guide de Dépannage - PWA

## Erreurs courantes et solutions

### ❌ Erreur : "Failed to register ServiceWorker" (404)

**Message complet :**
```
TypeError: Failed to register a ServiceWorker for scope 
with script: A bad HTTP response code (404) was received
```

**Pourquoi ça arrive :**
- Vous testez en local sans HTTPS
- Le fichier `service-worker.js` n'est pas au bon endroit
- Vous êtes sur un domaine qui n'autorise pas les Service Workers

**✅ SOLUTION 1 : C'est normal en développement local**

Si vous voyez cette erreur en ouvrant `index.html` directement dans votre navigateur, c'est **NORMAL** ! Le site fonctionne quand même, mais sans les fonctionnalités PWA.

**Ce qui fonctionne :**
- ✅ Navigation dans les recettes
- ✅ Recherche et filtres
- ✅ Favoris (localStorage)
- ✅ Toutes les fonctionnalités de base

**Ce qui ne fonctionne pas :**
- ❌ Mode hors ligne
- ❌ Installation comme app
- ❌ Cache avancé

**✅ SOLUTION 2 : Déployer sur un serveur HTTPS**

Pour tester la PWA complète :

1. **Netlify (Recommandé - 2 minutes)** :
   ```
   - Allez sur https://app.netlify.com
   - Glissez-déposez le dossier
   - Votre site est en HTTPS automatiquement
   - PWA fonctionne à 100% !
   ```

2. **Vercel** :
   ```bash
   npm i -g vercel
   cd moroccan-recipes
   vercel
   ```

3. **GitHub Pages** :
   ```bash
   git init
   git add .
   git commit -m "PWA ready"
   git push origin main
   # Activer Pages dans Settings
   ```

**✅ SOLUTION 3 : Serveur local avec HTTPS**

```bash
# Installer mkcert pour HTTPS local
npm install -g mkcert
mkcert create-ca
mkcert create-cert

# Puis servir avec HTTPS
npx http-server -S -C cert.crt -K cert.key
```

---

### ❌ Erreur : "Manifest file not found"

**Causes possibles :**
- Le fichier `manifest.json` n'est pas au bon endroit
- Chemin incorrect dans `index.html`

**✅ SOLUTION :**

1. Vérifiez que `manifest.json` est dans le même dossier que `index.html`
2. Dans `index.html`, vérifiez la ligne :
   ```html
   <link rel="manifest" href="manifest.json">
   ```
   Pas de `/` au début !

---

### ❌ Erreur : "Icons not loading"

**Symptômes :**
- Les icônes ne s'affichent pas dans le manifest
- Erreurs 404 pour les icônes

**✅ SOLUTION :**

1. Vérifiez la structure :
   ```
   moroccan-recipes/
   ├── index.html
   ├── manifest.json
   └── icons/
       ├── icon-72x72.png
       ├── icon-96x96.png
       └── ...
   ```

2. Dans `manifest.json`, vérifiez :
   ```json
   "icons": [
     {
       "src": "icons/icon-192x192.png",  // Pas de / au début
       "sizes": "192x192",
       "type": "image/png"
     }
   ]
   ```

---

### ❌ Problème : "Install button doesn't appear"

**Pourquoi :**
- Le site n'est pas en HTTPS
- Le manifest est incorrect
- Vous utilisez iOS (Safari ne supporte pas complètement PWA)
- L'app est déjà installée

**✅ SOLUTION :**

1. **Pour Chrome Android** :
   - Menu (⋮) > "Installer l'application"
   - Ou "Ajouter à l'écran d'accueil"

2. **Pour iOS** :
   - Bouton Partager
   - "Sur l'écran d'accueil"
   - Note : Fonctionnalités PWA limitées sur iOS

3. **Vérifier le manifest** :
   ```json
   {
     "display": "standalone",  // Requis
     "start_url": "/",         // Requis
     "name": "...",            // Requis
     "icons": [...]            // Au moins 1 icône 192x192
   }
   ```

---

### ❌ Problème : "App not working offline"

**Causes :**
- Service Worker non enregistré
- Cache non configuré
- Vous êtes en mode navigation privée

**✅ SOLUTION :**

1. Vérifiez le Service Worker :
   - F12 > Application > Service Workers
   - Doit être "Activated and running"

2. Vérifiez le cache :
   - F12 > Application > Cache Storage
   - Vous devez voir "matbakh-alnakhat-v1"

3. Test :
   - Visitez le site une fois en ligne
   - Mettez l'appareil en mode avion
   - Rafraîchissez la page
   - Ça devrait fonctionner !

---

### ❌ Problème : "Favorites not saving"

**Causes :**
- Mode navigation privée
- localStorage désactivé
- Limite de stockage atteinte

**✅ SOLUTION :**

1. Vérifiez dans la console :
   ```javascript
   localStorage.setItem('test', 'ok')
   localStorage.getItem('test')  // Doit retourner "ok"
   ```

2. Vérifiez que vous n'êtes pas en mode privé

3. Videz le cache si nécessaire :
   - F12 > Application > Storage
   - "Clear site data"

---

### ❌ Erreur : "CORS policy blocking"

**Message :**
```
Access to fetch has been blocked by CORS policy
```

**Causes :**
- Fichier ouvert avec `file://` (double-clic)
- Serveur mal configuré

**✅ SOLUTION :**

1. **Ne jamais ouvrir avec `file://`** !
   Toujours utiliser un serveur :
   ```bash
   python -m http.server 8000
   ```

2. Pour le déploiement, Netlify/Vercel gèrent CORS automatiquement

---

### ❌ Problème : "App doesn't update"

**Symptômes :**
- Modifications non visibles
- Ancienne version persiste

**✅ SOLUTION :**

1. **Forcer le rafraîchissement** :
   - Ctrl + Shift + R (Windows/Linux)
   - Cmd + Shift + R (Mac)

2. **Vider le cache** :
   - F12 > Application > Clear storage
   - "Clear site data"

3. **Désinstaller/Réinstaller l'app** :
   - Longue pression sur l'icône
   - Désinstaller
   - Réinstaller depuis le site

4. **Pour les développeurs** :
   - F12 > Application > Service Workers
   - Cochez "Update on reload"
   - Cliquez "Unregister"

---

### ❌ Problème : "Images not loading"

**Symptômes :**
- Icônes cassées
- Images manquantes

**✅ SOLUTION :**

1. Vérifiez les chemins :
   ```html
   <img src="icons/icon-192x192.png">  <!-- Correct -->
   <img src="/icons/icon-192x192.png"> <!-- Peut causer problème -->
   ```

2. Vérifiez que les fichiers existent :
   ```bash
   ls -la icons/
   ```

3. Extensions en minuscules :
   - ✅ `icon.png`
   - ❌ `icon.PNG`

---

## 🔍 Outils de débogage

### Chrome DevTools

1. **Ouvrir** : F12 ou Clic droit > Inspecter

2. **Onglets utiles** :
   - **Console** : Voir les erreurs JavaScript
   - **Application** :
     - Manifest : Vérifier la config PWA
     - Service Workers : État et contrôles
     - Cache Storage : Contenu en cache
     - Local Storage : Données sauvegardées
   - **Network** : Requêtes et erreurs de chargement

### Test Lighthouse

1. F12 > Lighthouse
2. Sélectionner "Progressive Web App"
3. "Analyze page load"
4. Score cible : **90+/100**

### Test en ligne

1. **PWA Builder** : https://www.pwabuilder.com/
   - Entrez votre URL
   - Analyse complète
   - Suggestions d'amélioration

2. **Manifest Validator** : https://manifest-validator.appspot.com/
   - Valide votre manifest.json

---

## ✅ Checklist de vérification

Avant de demander de l'aide, vérifiez :

- [ ] Le site est en **HTTPS** (pas http://)
- [ ] `manifest.json` est au bon endroit
- [ ] Toutes les **icônes** existent dans le dossier `icons/`
- [ ] `service-worker.js` est dans le dossier racine
- [ ] Vous n'êtes **pas en mode privé**
- [ ] Le navigateur est **à jour**
- [ ] Vous avez essayé **Ctrl+Shift+R**

---

## 📞 Obtenir de l'aide

Si rien ne fonctionne :

1. **Vérifiez la console** (F12) et notez l'erreur exacte
2. **Testez dans un autre navigateur**
3. **Essayez en mode navigation privée** (pour éliminer les extensions)
4. **Déployez sur Netlify** pour tester en conditions réelles

---

## 💡 Bonnes pratiques

### Pour le développement :

```bash
# Toujours utiliser un serveur local
python -m http.server 8000

# Ou
npx http-server

# Jamais double-cliquer sur index.html !
```

### Pour les tests PWA :

```bash
# Déployer sur Netlify
# C'est gratuit et prend 2 minutes
```

### Pour la production :

```bash
# 1. Tester avec Lighthouse
# 2. Vérifier sur vrai téléphone
# 3. Tester mode avion
# 4. Vérifier les mises à jour
```

---

## 🎯 Résumé rapide

**Erreur Service Worker en local ?**
→ C'est normal ! Déployez sur Netlify pour tester.

**Bouton "Installer" absent ?**
→ Vérifiez : HTTPS + manifest valide + Chrome Android.

**App ne fonctionne pas hors ligne ?**
→ Visitez une fois en ligne d'abord, puis testez.

**Modifications non visibles ?**
→ Ctrl+Shift+R pour vider le cache.

---

**Besoin d'aide supplémentaire ?** Consultez le fichier `INSTALLATION_READY.md` ou `ANDROID_CONVERSION_GUIDE.md`
