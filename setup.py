# -*- coding:utf-8 -*-

from setuptools import find_packages, setup

README = """# candy_path
"""


setup(
    name='candy_path',
    version='0.0.1',
    description='sweet library on path',
    long_description=README,
    author='程飞',
    url='https://github.com/faycheng/candy_path.git',
    packages=find_packages(exclude=['tests']),
    install_requires=['pytest==3.2.1'],
    entry_points={
        'console_scripts': [],
    },
    zip_safe=True,
    license='MIT License',
    classifiers=['development status :: 1 - planning', 'topic :: software development :: libraries', 'programming language :: python :: 3 :: only', 'environment :: macos x']
)