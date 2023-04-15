from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1',
    description='You can clean your computer with this code',
    url='https://github.com/Siia95/Clean_Folder',
    author='Rybakova Anastasiia',
    author_email='ribki2802@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={'console_scripts': ['clean_folder = clean_folder.clean_folder.clean:main']})
