echo --===Custom compilation start===--

pyston -m SCons p=x11 tools=yes target=release_debug -j14 \
    custom_modules=./custom_modules

pyston -m SCons p=x11 tools=no target=debug -j14 \
    custom_modules=./custom_modules
pyston -m SCons p=x11 tools=no target=release -j14 \
    custom_modules=./custom_modules

pyston -m SCons p=windows tools=no target=debug bits=64 -j14  \
    custom_modules=./custom_modules
pyston -m SCons p=windows tools=no target=release bits=64 -j14 \
    custom_modules=./custom_modules

echo --===Custom compilation finished===--
