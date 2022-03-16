from setuptools import setup

# Get the long description by reading the README
try:
    readme_content = open("README.rst").read()
except:
    readme_content = ""

# Create the actual setup method
setup(name='pynagios',
      version='0.1.4-dev',
      description='Python library to write Nagios plugins.',
      long_description=readme_content,
      author='Mitchell Hashimoto',
      author_email='mitchell@kiip.me',
      maintainer='Mitchell Hashimoto',
      maintainer_email='mitchell@kiip.me',
      url="https://kiip.github.com/pynagios/",
      license="MIT License",
      keywords=["nagios", "pynagios", "monitoring"],
      packages=['pynagios'],
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: System :: Systems Administration"]
      )
