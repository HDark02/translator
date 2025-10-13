[app]
# Informations de base sur ton application
title = KivyTranslate
package.name = kivytranslate
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg,ttf,mp3,ogg,wav,txt
version = 1.0

# Dépendances Python nécessaires
requirements = python3,kivy==2.1,kivymd==1.1.1,translate,requests,httpx

# Orientation et affichage
orientation = portrait
fullscreen = 0

# Icône (optionnelle)
# icon.filename = %(source.dir)s/icon.png

# Permissions nécessaires (pour accès internet)
android.permissions = INTERNET

# API Android compatibles
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a

# Empêche les crashs dus à la mémoire
android.allow_backup = True

# Nom du package de sortie
package.version = 1.0
package.title = KivyTranslate

[buildozer]
log_level = 2
warn_on_root = 1
