from pathlib import Path
from setuptools import setup

__version__ = '0.0.1'

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

dir = Path(__file__).parent
long_description = (dir / "README.md").read_text()

test_requires = [
    'pytest',
]

setup(
    name="knownet",
    version=__version__,
    author="obonyojimmy",
    author_email="cliffjimmy27@gmail.come",
    license="MIT",
    url="https://github.com/obonyojimmy/knowledge_net",
    description="Advanced knowledge processing and insights with multi-agent framework for robust  data-driven applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["knownet"],
    #include_package_data=True,
    install_requires=requirements,
    zip_safe=True,
    extras_require={
        'test': test_requires,
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
