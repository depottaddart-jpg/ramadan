// Service Worker for مطبخ النكهات PWA
const CACHE_NAME = 'matbakh-alnakhat-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/styles.css',
  '/app.js',
  '/recipes-ar.json',
  '/manifest.json'
];

// Install Service Worker
self.addEventListener('install', event => {
  console.log('Service Worker: Installing...');
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Service Worker: Caching files');
        return cache.addAll(urlsToCache);
      })
      .then(() => self.skipWaiting())
  );
});

// Activate Service Worker
self.addEventListener('activate', event => {
  console.log('Service Worker: Activating...');
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cache => {
          if (cache !== CACHE_NAME) {
            console.log('Service Worker: Clearing old cache');
            return caches.delete(cache);
          }
        })
      );
    })
  );
  return self.clients.claim();
});

// Fetch Strategy: Cache First, falling back to Network
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Return cached version or fetch from network
        return response || fetch(event.request)
          .then(fetchResponse => {
            // Clone the response
            const responseClone = fetchResponse.clone();
            
            // Cache the new response
            caches.open(CACHE_NAME)
              .then(cache => {
                cache.put(event.request, responseClone);
              });
            
            return fetchResponse;
          });
      })
      .catch(() => {
        // Fallback page if offline and no cache
        return caches.match('/index.html');
      })
  );
});

// Background Sync (optional - for future features)
self.addEventListener('sync', event => {
  if (event.tag === 'sync-recipes') {
    event.waitUntil(syncRecipes());
  }
});

function syncRecipes() {
  return fetch('/recipes-ar.json')
    .then(response => response.json())
    .then(data => {
      // Update cache with new data
      return caches.open(CACHE_NAME)
        .then(cache => {
          cache.put('/recipes-ar.json', new Response(JSON.stringify(data)));
        });
    })
    .catch(err => console.error('Sync failed:', err));
}

// Push Notifications (optional - for future features)
self.addEventListener('push', event => {
  const options = {
    body: event.data.text(),
    icon: '/icons/icon-192x192.png',
    badge: '/icons/icon-72x72.png',
    vibrate: [200, 100, 200],
    dir: 'rtl',
    lang: 'ar'
  };
  
  event.waitUntil(
    self.registration.showNotification('مطبخ النكهات', options)
  );
});
