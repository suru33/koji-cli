from setuptools import setup, find_packages

setup(
    name='koji-cli',
    version='1.0',
    description='CLI for fedora koji API',
    url='https://github.com/suru33/koji-cli',
    author='SuRu',
    author_email='33urus@gmail.com',
    license='GPLv3+',
    python_requires='>=3.6',
    packages=find_packages(include=['koji_ext']),
    install_requires=[
        'Click',
        'koji'
    ],
    entry_points={
        'console_scripts': [
            'koji-x=cli:main',
        ],
    },
)
