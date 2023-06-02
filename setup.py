import setuptools

# Developer self-reminder for uploading in pypi:
# - install: wheel, twine
# - build  : python setup.py bdist_wheel
# - deploy : twine upload dist/*

with open("README.md", "r") as file:
    long_description = file.read().replace(":fire:", "").replace(":rocket:", "")

setuptools.setup(
    name='objwrap',
    version='0.0.2',
    author="Emmanouil (Manios) Krasanakis",
    author_email="maniospas@hotmail.com",
    description="Easy object wrapping in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maniospas/objwrap",
    packages=setuptools.find_packages(),
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: OS Independent",
     ],
    install_requires=[],
 )