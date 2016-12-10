from setuptools import find_packages, setup

EXCLUDE_FROM_PACKAGES = []
setup(
    name='AsianCops',
    version='1.0',
    include_package_data=True,
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    install_requires=open('requirements.txt').readlines(),
    scripts=['manage.py'],
    url='',
    license='',
    author='joan',
    author_email='you_hong@yahoo.com',
    description='Wagtail based web site for Asian Cops'
)
