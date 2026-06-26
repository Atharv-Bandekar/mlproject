from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    returns list of requirements from requirements.txt
    
    '''

    HYPEN_DOT_E = "-e"
    
    get_requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)

    return requirements 


setup(
    name='mlproject',
    version='0.0.1',
    author='Atharv',
    author_email='atharvbandekar21@gmail.com',
    packages=find_packages(),
    install_requries=get_requirements('requirements.txt')
)