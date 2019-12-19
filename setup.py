from setuptools import setup

setup(
    name='vrt_generator',
    version='0.0.5',
    packages=['vrt'],
    url='https://github.com/miweru/vrt_generator',
    license='',
    author='Michael Ruppert',
    author_email='michael.ruppert@fau.de',
    description='creating vrt corpora',
    install_requires=[
        "smart_open>=1.9.0",
        "spacy>=2.2.3",
        "https://github.com/explosion/spacy-models/releases/download/de_core_news_md-2.2.5/de_core_news_md-2.2.5.tar.gz"
    ],
    python_requires=">=3.5",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
    ],
)
