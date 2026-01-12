# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'V-Insight R&D Knowledge Base'
copyright = '2026, Team V-Insight'
author = 'Team V-Insight'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['assets']
html_logo = 'assets/logo.png'
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
}

# MyST Parser configuration
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3
