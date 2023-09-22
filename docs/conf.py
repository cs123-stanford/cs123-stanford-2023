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
import os
import sys
#import pip3

#def install(package):
#     if hasattr(pip3, 'main'):
#         pip3.main(['install', package])
#     else:
#         pip3._internal.main(['install', package])

#install('sphinx_rtd_theme')
#install('recommonmark')
#sys.path.insert(0, os.path.abspath('.'))

#def setup (app):
#   app.add_stylesheet('css/custom.css')




# -- Project information -----------------------------------------------------

project = 'CS123'
copyright = '2023, Stanford CS123 Teaching Team'
author = 'Nathan Kau, Ankush Dhawan, Jaden Clark, Gabrael Levine'

# The full version, including alpha/beta/rc tags
release = '2021'


# -- General configuration ---------------------------------------------------

# The master toctree document.
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['recommonmark', "sphinx_rtd_theme", 'sphinxcontrib.youtube']

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

import sphinx_rtd_theme
import solar_theme

html_theme = 'sphinx_rtd_theme'
#html_theme = 'solar_theme'
#html_theme_path = ["_themes", ]
#html_theme_path = [solar_theme.theme_path]
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css']
html_logo = "stanford-university-stacked.jpeg"
html_theme_options = {
    'logo_only': True
}
