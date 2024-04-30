from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in material_transfer_request_version13/__init__.py
from material_transfer_request_version13 import __version__ as version

setup(
	name="material_transfer_request_version13",
	version=version,
	description="creating material transfer request",
	author="abdul basit ali shaik",
	author_email="material_transfer@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
