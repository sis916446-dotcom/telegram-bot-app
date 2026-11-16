[app]

# የአፑ ስም
title = Telegram Bot App

# የፓኬጅ ስም (package name)
package.name = telegrambotapp

# የዶሜይን ስም
package.domain = org.telegram

# የኮድ ፋይሎቹ የሚገኙበት ፎልደር (ወቅታዊው ፎልደር መሆኑን ያሳያል)
source.dir = .

# የሚጠቀሟቸው ፋይል አይነቶች
source.exts = py,png,jpg,kv,atlas

# የአፑ ስሪት
version = 0.1

# የሚያስፈልጉ የ Python ላይብረሪዎች እና ሞጁሎች
requirements = python3,kivy,requests,urllib3,certifi,idna,charset-normalizer

# የአፕሊኬሽኑ አቅጣጫ (ቁልቁል - portrait)
orientation = portrait

# ለአፑ የሚያስፈልጉ ሲስተም ፍቃዶች (ከኢንተርኔት ጋር ለመገናኘት INTERNET ግዴታ ነው)
android.permissions = INTERNET

# የአንድሮይድ ኤስዲኬ እና ኤንዲኬ ማስተካከያ (ለ GitHub Actions ተስማሚ)
android.api = 33
android.minapi = 21
android.sdk = 30
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
