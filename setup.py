import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zen_dataset",
    version="0.0.1",
    author="Radek Osmulski",
    author_email="rosmulski@gmail.com",
    description="Library for assembling pytorch datasets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rosmulski/zen_dataset",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: APACHE SOFTWARE LICENSE",
        "Operating System :: OS Independent",
    ],
)
