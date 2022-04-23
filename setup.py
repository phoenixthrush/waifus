from setuptools import setup, find_packages

__name__ = "waifus"
__version__ = "1.0.0"

setup(
    name=__name__,
    version=__version__,
    author="Phoenixthrush UwU",
    author_email="<contact@phoenixthrush.com>",
    description="getting some waifu pics",
    long_description_content_type="text/markdown",
    long_description=open("README.md", encoding="utf-8").read(),
    url = "https://github.com/phoenixthrush-develops/waifus",
    project_urls={
      "Bug Tracker": "https://github.com/phoenixthrush-develops/waifus/issues",
    },
    install_requires=['argparse', 'requests', 'tk', 'Pillow'],
    packages=find_packages(),
    keywords=['waifus', 'python', 'package', 'library', 'lib', 'module'],
    classifiers=[
      "Intended Audience :: Developers",
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
    ]
)