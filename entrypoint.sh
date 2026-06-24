#!/bin/bash
set -e

CONFIG_PRESET="ninja-release-x64"
BUILD_PRESET="ninja-build-release-x64"

echo "Copying source to /dolphin-local/"
rm -rf /dolphin-local/ || true
mkdir -p /dolphin-local/
cp -R /dolphin/. /dolphin-local/
rm -rf /dolphin-local/build/* || true
cd /dolphin-local

echo "Running command:"
echo "cmake --preset "$CONFIG_PRESET" $CMAKE_ARGS -DUSE_SYSTEM_LIBS=${USE_SYSTEM_LIBS}"
cmake --preset "$CONFIG_PRESET" $CMAKE_ARGS -DUSE_SYSTEM_LIBS=${USE_SYSTEM_LIBS}

echo "Building using preset: $BUILD_PRESET"
cmake --build --preset "$BUILD_PRESET"
echo "Build finished successfully"

if cmake --build --preset "$BUILD_PRESET" --target help 2>/dev/null | grep -q "^unittests"; then
    echo "Running tests"
    cmake --build --preset "$BUILD_PRESET" --target unittests
fi