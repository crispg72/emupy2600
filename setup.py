from setuptools import setup, find_packages

setup(name='emupy2600',
      version='1.0.0',
      description='Simple Atari 2600 Emulator',
      author='Chris Green',
      author_email='crispg72@users.noreply.github.com',
      url='https://github.com/crispg72/emupy2600',
      license='MIT',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
     )
