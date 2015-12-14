from setuptools import setup, find_packages
import Embedded_CSS_Optimizer
setup(name = 'Embedded-CSS-Optimizer',
      version = Embedded_CSS_Optimizer.__version__,
      packages = find_packages(),
      entry_points = {'gui_scripts': ['Embedded-CSS-Optimizer = Embedded_CSS_Optimizer.embeddedcssoptimizer:main',]},
      description='Remove unused CSS definitions',
      long_description='The main objective of this program is to lighten CSS files. This program will read your HTML files and your CSS files. Then, it will remove all definitions unused in the CSS file. Thanks to the GUI, you can customize this selection the way you prefer.',
      author='Thibaut Meric',
      author_email='thibaut.meric@microchip.com',
      url='www.microchip.com/iot/',
      maintainer= 'Iot & HASG Group',
      maintainer_email='xxxxxx@microchip.com',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers'
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                  ],
      platforms=['Operating System :: MacOS :: MacOS X','Operating System :: Microsoft :: Windows'],
      keywords='CSS HTML',
     )
# documentation -> https://packaging.python.org/en/latest/distributing/#setup-args
# classifiers list -> https://pypi.python.org/pypi?%3Aaction=list_classifiers
# Wheel name documentation -> https://www.python.org/dev/peps/pep-0427/
