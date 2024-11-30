from setuptools import setup, find_packages

setup(
    name='my_package-hs094',
    version='0.0.1',
    description='Module to perform image segmentation and object detection.',
    license='MIT',
    author='Hardik Soni',
    author_email='iamhardiksoni@gmail.com',
    packages=find_packages(),
    install_requires=['matplotlib','numpy','torch','torchvision','pillow','opencv-python']
)