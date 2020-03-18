from setuptools import setup

setup(name='graph',
      version='0.1',
      description='undirected graph implementation',
      url='https://github.com/DillyPickly/graph',
      author='Dylan Sabuda',
      author_email='dylan.sabuda@gmail.com',
      license='MIT',
      packages=['graph'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
)