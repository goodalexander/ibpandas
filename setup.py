from setuptools import setup

setup(name='ibpandas',
      version='0.1',
      description='A library for trading your Interactive Brokers account with Pandas',
      url='https://github.com/goodalexander/ibpandas',
      author='goodalexander',
      author_email='goodalexander@gmail.com',
      license='MIT',
      packages=['pandas','ibapi','threading','queue','time'],
      zip_safe=False)
