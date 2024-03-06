import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Disease-Classification-Project"
AUTHOR = "car-tel"
SRC_REPO = "cnnClassifier"

setuptools.setup(
    name=SRC_REPO,
    version = __version__,
    author = AUTHOR,
    description = "A CNN app for Image Classification",
    Long_description = long_description,
    Long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR}/{REPO_NAME}/issues",
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src")
)