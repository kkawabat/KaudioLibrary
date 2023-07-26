from setuptools import setup, find_packages

setup(
    name='kaudio_library',
    version='1.0.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/kkawabat/KaudioLibrary',
    license='MIT',
    author='Kan Kawabata',
    author_email='kkawabat@asu.edu',
    description='this is a library that is used for audio i/o',
    install_requires=['pyaudio']
)
