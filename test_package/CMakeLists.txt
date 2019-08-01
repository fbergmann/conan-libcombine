PROJECT(LibCombinePackageTest)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

ADD_EXECUTABLE(create_archive create_archive.cpp)
TARGET_LINK_LIBRARIES(create_archive ${CONAN_LIBS})
