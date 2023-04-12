#######################################################################################
# a2lparser: https://github.com/mrom1/a2lparser                                       #
# author: https://github.com/mrom1                                                    #
#                                                                                     #
# This file is part of the a2lparser package.                                         #
#                                                                                     #
# a2lparser is free software: you can redistribute it and/or modify it                #
# under the terms of the GNU General Public License as published by the               #
# Free Software Foundation, either version 3 of the License, or (at your option)      #
# any later version.                                                                  #
#                                                                                     #
# a2lparser is distributed in the hope that it will be useful,                        #
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY      #
# or FITNESS FOR A PARTICULAR PURPOSE.                                                #
# See the GNU General Public License for more details.                                #
#                                                                                     #
# You should have received a copy of the GNU General Public License                   #
# along with a2lparser. If not, see <https://www.gnu.org/licenses/>.                  #
#######################################################################################


from setuptools import setup, find_packages
import a2lparser

# Read requirements.txt
with open("requirements.txt", encoding="utf-8") as f:
    install_requirements = f.read().strip().split("\n")

setup(
    name=a2lparser.__package_name__,
    version=a2lparser.__version__,
    packages=find_packages(),
    install_requires=install_requirements,
    author=a2lparser.__author__,
    author_email=a2lparser.__author_email__,
    description=a2lparser.__description__,
    license=a2lparser.__license__,
    license_files=("LICENSE",),
    url=a2lparser.__url__,
    package_data={"a2lparser": ["*.cfg", "*.config"]},
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["a2lparser = a2lparser.a2lparser:main"]},
)
