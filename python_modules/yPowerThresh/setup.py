from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy
import runpy

cfg = runpy.run_path('../.config.py')

setup(
        name="yPowerThresh",
        include_dirs=[numpy.get_include(), cfg['PYTHON_PLUGIN_SRC_DIR']],
        ext_modules=cythonize(
                Extension(
                        'yPowerThresh',
                        sources=["yPowerThresh.pyx"],
                        export_symbols=[
                                'pluginStartup',
                                'pluginisready',
                                'getParamNum',
                                'getParamConfig',
                                'pluginFunction',
                                'eventFunction',
                                'spikeFunction',
                                'setIntParam',
                                'setFloatParam',
                                'getIntParam',
                                'getFloatParam',
                                'updateSettings',
                                'channelChanged'
                        ]
                ),
                language_level=3
        )
)
