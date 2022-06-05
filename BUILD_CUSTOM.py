#!/usr/bin/env python3

import argparse
import os

ANDROID_SDK_PATH = "/home/gabrielschwab/android_sdk_root"
ANDROID_NDK_PATH = ANDROID_SDK_PATH+"/ndk"
BUILD_EDITOR = "pyston -m SCons p={} bits=64 -j14 custom_modules={}"
BUILD_TEMPLATES = "pyston -m SCons p={} tools=no target={} bits=64 -j14  \
		custom_modules=\"{}\" {}"

modules = "./no_modules"

def build_editor(platform="x11"):
	global modules
	return BUILD_EDITOR.format(platform, modules)

def build_templates(platform="x11", more_args=""):
	global modules
	return "{}; {}".format(
		BUILD_TEMPLATES.format(platform, "release", modules, more_args),
		BUILD_TEMPLATES.format(platform, "debug", modules, more_args),
	)


def build_templates_android():
	os.system(f"""
	export ANDROID_SDK_ROOT=\"{ANDROID_SDK_PATH}\";
	
	{build_templates("android", "android_arch=armv7")};
	{build_templates("android", "android_arch=arm64v8")};

	cd platform/android/java;
	./gradlew build;
	cd ../../..;

	cp platform/android/java/app/build/outputs/apk/debug/android_debug.apk \
		bin/android_debug.apk;
	cp platform/android/java/app/build/outputs/apk/release/android_release.apk \
		bin/android_release.apk;
	""")


def build_templates_html5():
	os.system(build_templates("javascript"))


def build_templates_iphone():
	os.system(build_templates("iphone"))


def build_templates_linux():
	os.system(build_templates("x11"))


def build_templates_windows():
	os.system(build_templates("windows"))


def help():
	print("Im helping!")


def main():
	parser = argparse.ArgumentParser(description='Build Godot.')
	parser.add_argument(
		'--modules', "-m"
	)
	parser.add_argument(
		'--editor', "-e", action="append"
	)
	parser.add_argument(
		'--android', action="store_true"
	)
	parser.add_argument(
		'--html5', action="store_true"
	)
	parser.add_argument(
		'--iphone', action="store_true"
	)
	parser.add_argument(
		'--linux', action="store_true"
	)
	parser.add_argument(
		'--windows', action="store_true"
	)

	args = parser.parse_args()
	# Modules
	if args.modules:
		global modules
		modules = args.modules
	# Editor
	if args.editor:
		for arg in args.editor:
			print(arg)
			os.system(build_editor(arg))
	# Templates
	if args.android:
		build_templates_android()
	if args.html5:
		build_templates_html5()
	if args.iphone:
		build_templates_iphone()
	if args.linux:
		build_templates_linux()
	if args.windows:
		build_templates_windows

if __name__ == "__main__":
	main()