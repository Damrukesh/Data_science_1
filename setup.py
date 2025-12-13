from setuptools import setup, find_packages
from typing import List  
sym='-e.'

def get_requirements(file_path: str) -> List[str]:
    requirements=[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [r.replace("\n","") for r in requirements]
        if sym in requirements:
            requirements.remove(sym)
        return requirements
    
setup(
    name="MLproject",
    version="0.1.0",
    author="DamrukeshD",
    author_email="ddamrukesh@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('req.txt') 
)