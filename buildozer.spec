[app]

title = Telegram Bot App
package.name = telegrambotapp
package.domain = org.telegram

source.dir = .
source.exts = py

version = 0.1

# ምንም አይነት ውጫዊ ላይብረሪ አያስፈልግም
requirements = python3

orientation = portrait
android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
