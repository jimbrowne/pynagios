from setuptools import setup, Command

class PyTest(Command):
    """
    This builds a subcommand for setup.py which allows tests to be
    run on the library without installing it. Tests can be run with:

        python setup.py test

    """
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess
        errno = subprocess.call([sys.executable, 'test.py'])
        raise SystemExit(errno)

# Get the long description by reading the README
try:
    readme_content = open("README.rst").read()
except:
    readme_content = ""

# Create the actual setup method
setup(name='pynagios',
      version='0.1.0',
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
      cmdclass= { 'test': PyTest },
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: System :: Systems Administration"]
      )
