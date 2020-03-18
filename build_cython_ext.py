import os
from setuptools import setup
from setuptools.extension import Extension
import sys

# Copy of setup.py, but only for building cython extensions
try:
    import numpy as np
    from Cython.Build import cythonize
    extensions = cythonize([
        Extension("taiyaki.squiggle_match.squiggle_match",
                  [os.path.join("taiyaki/squiggle_match", "squiggle_match.pyx"),
                   os.path.join("taiyaki/squiggle_match", "c_squiggle_match.c")],
                  include_dirs=[np.get_include()],
                  extra_compile_args=["-O3", "-fopenmp", "-std=c99", "-march=native"],
                  extra_link_args=["-fopenmp"]),
        Extension("taiyaki.ctc.ctc", [os.path.join("taiyaki/ctc", "ctc.pyx"),
                                      os.path.join("taiyaki/ctc", "c_crf_flipflop.c"),
                                      os.path.join("taiyaki/ctc", "c_cat_mod_flipflop.c")],
                  include_dirs=[np.get_include()],
                  extra_compile_args=["-O3", "-fopenmp", "-std=c99", "-march=native"],
                  extra_link_args=["-fopenmp"])
    ])
except ImportError:
    extensions = []
    sys.stderr.write("WARNING: Numpy and Cython are required to build taiyaki extensions\n")
    if any([cmd in sys.argv for cmd in ["install", "build", "build_clib", "build_ext", "bdist_wheel"]]):
        raise

setup(
    ext_modules=extensions
)