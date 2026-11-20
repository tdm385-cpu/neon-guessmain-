[app]
title = NEON GUESS
package.name = neonguess
package.domain = org.tdm
source.dir = .
source.include_exts = py
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.permissions =
android.api = 35
android.minapi = 23
android.archs = arm64-v8a