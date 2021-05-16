# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os, subprocess
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('mh5_robot/mh5_ui/src/'))

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'MH5 Robot'
copyright = '2021, Alex Sonea'
author = 'Alex Sonea'

# The full version, including alpha/beta/rc tags
release = 'D.1'
version = release

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'sphinx.ext.autodoc',
               'sphinx.ext.autosummary',
               'sphinx.ext.napoleon',
               'sphinx.ext.intersphinx',
               'sphinx.ext.viewcode',
               'sphinx.ext.autosectionlabel',
               'sphinx_rtd_theme',
               'sphinx.ext.todo',
               'breathe'
]

# Display todos by setting to True
todo_include_todos = True

# generate autosummary pages
autosummary_generate = True
autodoc_default_options = {
#     # 'members': 'var1, var2',
      'member-order': 'bysource',
      'special-members': '__init__',
      'undoc-members': True,
#     'private-members': True,
     'exclude-members': '__weakref__'
}
# autoclass_content = 'both'
autodoc_mock_imports = [
    'snack',
    'rospy',
    'psutil',
    'sensor_msgs'
    # 'mh5_director.msg',
    # 'rospkg',

    # 'actionlib',
    # 'control_msgs',
    # 'trajectory_msgs',
    # 'yaml'
]

breathe_projects = { "mh5_documentation": "_xml" }
breathe_default_project = "mh5_documentation"
subprocess.call('doxygen', shell=True)

# # If true, the current module name will be prepended to all description
# # unit titles (such as .. function::).
# add_module_names = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_baseurl = "https://SYNTHesse-GIT.github.io/MH5/"

html_theme_options = {
    # 'collapse_navigation': True,
    # 'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
