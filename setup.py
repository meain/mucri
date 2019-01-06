import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

cur_classifiers = [
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
    "Environment :: Console",
    "Intended Audience :: End Users/Desktop",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Operating System :: POSIX",
    "Natural Language :: English",
]

install_requires = ['aiohttp']

setuptools.setup(
    name="mucri",
    version="0.0.5",
    author='Abin Simon',
    author_email='abinsimon10@gmail.com',
    description="Quickly fetch multiple pages",
    url="https://github.com/meain/mucri",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=["mucri"],
    install_requires=install_requires,
    keywords=['asyncio', 'scraper', 'aiohttp'],
    classifiers=cur_classifiers)
