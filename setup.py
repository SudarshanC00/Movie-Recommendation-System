from setuptools import setup

with open("README.md","r",encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'SUDARSHAN CHIKKATHIMMAIAH'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='sudarshansudhu66@gmail.com',
    description='A movie recommender system',
    long_description='movie recommendation system',
    package = [SRC_REPO],
    python_used = '3.12.4',
    install_requires = LIST_OF_REQUIREMENTS,
)
    
    