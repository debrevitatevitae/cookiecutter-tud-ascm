from setuptools import find_packages, setup

with open('requirements.txt') as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name='{{cookiecutter.repo_name}}',
    version='{{cookiecutter.version}}',
    description='{{cookiecutter.short_description}}',
    author='{{cookiecutter.full_name}}',
    license='',
    packages=find_packages(include=['{{cookiecutter.repo_name}}']),
    install_requires=REQUIREMENTS,
    extras_require={
        'interactive': ['jupyter', 'matplotlib']
        },
    setup_requires=['pytest-runner', 'flake8'],
    tests_require=['pytest']
)