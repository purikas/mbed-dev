"""
mbed SDK
Copyright (c) 2011-2013 ARM Limited

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from os.path import join, abspath, dirname
import logging

ARM_PATH = "C:/Keil/ARM/ARMCC"
ARM_BIN = join(ARM_PATH, "bin")
ARM_INC = join(ARM_PATH, "include")
ARM_LIB = join(ARM_PATH, "lib")

ARM_CPPLIB = join(ARM_LIB, "cpplib")
MY_ARM_CLIB = join(ARM_LIB, "armlib")


