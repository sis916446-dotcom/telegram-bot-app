[app]

title = Telegram Bot App
package.name = telegrambotapp
package.domain = org.telegram

source.dir = .
source.exts = py

version = 0.1

# የ Python እና የ requests ላይብረሪ ብቻ
requirements = python3,requests

orientation = portrait
android.permissions = INTERNET

# የተረጋጉ የአንድሮይድ ኤስዲኬ እና ኤንዲኬ ስሪቶች
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
