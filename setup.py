from distutils.core import setup

setup(
    name='FileCreator',
    version='1.0.0',
    author='Colin Murphy',
    author_email='dietcoke3.14@gmail.com',
    packages=['PyCreateFile'],
    license='LICENSE.txt',
    description='Cross Platform File Creator',
    long_description=open('README.txt').read(),
    install_requires=[
        "wx >= 2.8"
    ],
)

