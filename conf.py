# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Pixel Art Studio'
copyright = '2026, Alfred Reinold Baudisch'
author = 'Alfred Reinold Baudisch'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_rtd_theme', 'sphinxcontrib.images', 'sphinxcontrib.video']

templates_path = ['_templates']
# README and IMAGES-TODO are notes for me, not pages of the manual
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md', 'IMAGES-TODO.md',
                    'venv', 'path']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

html_baseurl = "https://alfredbaudisch.github.io/godot-vertex-studio-docs/"