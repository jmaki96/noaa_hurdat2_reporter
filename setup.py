from setuptools import setup

setup(name='noaa_hurdat2_reporter',
      version='1.0',
      packages=['src'],
      entry_points={
          'console_scripts': [
              'noaa_hurdat2_reporter = src.__main__:main'
          ]
      }
      )
