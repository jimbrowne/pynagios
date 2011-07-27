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

setup(name='pynagios',
      version='0.1.0',
      description='Python library to write Nagios plugins.',
      author='Mitchell Hashimoto',
      author_email='mitchell@kiip.me',
      maintainer='Mitchell Hashimoto',
      maintainer_email='mitchell@kiip.me',
      packages=['pynagios'],
      cmdclass= { 'test': PyTest }
      )
