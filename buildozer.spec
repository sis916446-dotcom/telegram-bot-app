[app]

title = Telegram Bot App
package.name = telegrambotapp
package.domain = org.telegram

source.dir = .
source.exts = py

version = 0.1

requirements = python3,requests,openssl,certifi

orientation = portrait
android.permissions = INTERNET

# NDK እና SDK ስሪቶችን ወደ 25b እና 33 እናስተካክላለን
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
