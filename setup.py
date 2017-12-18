from setuptools import setup

setup(name='kcc_case_study',
      version='1.0',
      packages=['src'],
      entry_points={
          'console_scripts': [
              'kcc_case_study = src.__main__:main'
          ]
      }
      )
