# Change the content according to your package.
import setuptools
import re

# Extract the version from the init file.
VERSIONFILE="relevantpackage/__init__.py"
getversion = re.search( r"^__version__ = ['\"]([^'\"]*)['\"]", open(VERSIONFILE, "rt").read(), re.M)
if getversion:
    new_version = getversion.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

# Configurations
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     install_requires=[],        # Dependencies
     python_requires='>=3',                                   # Minimum Python version
     name='dummy_package_name',                                  # Package name
     version=new_version,                                     # Version
     author='SasheO, Xaiver71, emilyyjx',                                     # Author name
     author_email='mezisashe.ojuba@bison.howard.edu, malcolm.gray@bison.howard.edu, emily.jones@bison.howard.edu',                           # Author mail
     description="Python package for string validation and alphanumeric token generation",    # Short package description
     long_description=long_description,                       # Long package description
     long_description_content_type="text/markdown",
     url="https://github.com/SasheO/CS3_Project",       # Url to your Git Repo
     download_url = 'https://github.com/SasheO/CS3_Project/'+new_version+'.tar.gz',
     packages=setuptools.find_packages(),                     # Searches throughout all dirs for files to include
     include_package_data=True,                               # Must be true to include files depicted in MANIFEST.in
     license_files=["LICENSE"],                               # License file
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )