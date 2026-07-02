# pyright: reportMissingModuleSource=false
from setuptools import find_packages, setup
from typing import List

hypen_e_dot ='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        requirements = [req for req in requirements if req != hypen_e_dot]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

setup(
    name='my_package',
    version='0.1.0',
    packages=find_packages(),
    author='obulreddy',
    author_email='bogireddyobulreddy2004@gmail.com',
    install_requires=get_requirements('requirements.txt')
)