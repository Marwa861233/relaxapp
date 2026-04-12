[app]
title = Relax Platform
package.name = relaxapp
package.domain = org.relax
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,requests
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 23b
android.sdk = 30

[buildozer]
log_level = 2
warn_on_root = 1
