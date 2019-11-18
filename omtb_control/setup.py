## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['omtb_control'],
<<<<<<< HEAD
    package_dir={'': 'src'}
=======
    package_dir={'': 'nodes'}
>>>>>>> 966386af94ecff44a331ccb2bc4c3d65238025a4
)

setup(**setup_args)
