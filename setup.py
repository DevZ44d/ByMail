import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    lng_description = fh.read()

setuptools.setup(
    name="bymail",
    version="2.0.0",
    author="AhMed",
    author_email="asyncpy@gmail.com",
    license="MIT",
    description="ByMail is a lightweight Python library to fetch inbox messages from temporary email providers. It validates domains and supports both one-shot and continuous (looping) fetching.",
    long_description=lng_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
