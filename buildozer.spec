[app]

title = Marble and Granite
package.name = marblegranite
package.domain = org.example
source.dir = app
source.include_exts = py,kv,png,jpg,ttf
version = 0.1

requirements = python3,kivy==2.3.0,kivymd,arabic_reshaper,python-bidi,reportlab,peewee,requests,plyer,matplotlib,kivy_garden.matplotlib,pillow

orientation = portrait

# Android specific settings
android.api = 35
android.minapi = 24
android.archs = arm64-v8a, armeabi-v7a
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET,CAMERA
android.gradle_dependencies = com.android.support:multidex:1.0.3

# Fullscreen is often desired on mobile
fullscreen = 0

# Keystore for release signing (placeholders)
# android.release_keystore = /path/to/your/release.keystore
# android.release_keystore_password = your_keystore_password
# android.release_key_alias = your_key_alias
# android.release_key_password = your_key_password

[buildozer]

# Log level (0 = error, 1 = warning, 2 = info, 3 = debug, 4 = trace)
log_level = 2

# Warn on deprecated properties
warn_on_deprecated = 1


