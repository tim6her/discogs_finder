from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='discogs_finder',
      version='0.1',
      description='FIND Every Release in your collection',
      long_description=readme(),
      url='https://github.com/tim6her/discogs_finder',
      author='Tim B. Herbstrith',
      license='MIT',
      packages=['discogs_finder'],
      install_requires=[
                'click',
            ],
      scripts=['scripts/discogs-finder'],
      zip_safe=False)