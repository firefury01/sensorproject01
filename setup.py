from setuptools import find_packages , setup
from typing import List
def get_requiremets(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        return requirements
setup (
    name = 'fault detecton',
    version = '0.0.1',
    author = 'imran',
    author_mail = 'md@gmail.com',
    install_requirements  = get_requiremets('requirements.txt'),
    packages = find_packages()




)