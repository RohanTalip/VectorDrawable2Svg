import setuptools
from drawable2svg.version import VERSION

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='drawable2svg',
    version=VERSION,
    author="Alessandro Lucchet",
    description="A library and utility for conversion from vector drawable XMLs (Android-specific) to SVG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RohanTalip/VectorDrawable2Svg",
    packages=setuptools.find_packages(),
    package_dir={'drawable2svg': 'drawable2svg'},
    install_requires=[
        'lxml>=4.6.2'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

