from conans import ConanFile, CMake
import os

class LibCombineTestConan(ConanFile):
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        self.run(os.path.join("bin", "create_archive") + ' ../../Brusselator.xml', run_environment=True)
