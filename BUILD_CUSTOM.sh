echo --===Custom compilation start===--
scons platform=x11 tools=yes target=release_debug -j12 #custom_modules=./custom_modules

#scons platform=x11 tools=no target=debug -j12 #custom_modules=./custom_modules
#scons platform=x11 tools=no target=release -j12 #custom_modules=./custom_modules

#scons platform=windows tools=no target=debug -j12 #custom_modules=./custom_modules
#scons platform=windows tools=no target=release -j12 #custom_modules=./custom_modules

echo --===Custom compilation finished===--
