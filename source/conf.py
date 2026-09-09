project = 'Pragmatic Musculoskeletal Modelling'
copyright = '2026, Contributors to the Pragmatic Musculoskeletal Modelling Repository'
author = 'The Musculoskeletal Modelling Community'
github_username = 'opynsim'
github_repository = 'https://github.com/opynsim/pragmatic.opynsim.eu'

# Number figures (e.g. Fig. 1, Fig. 2)
numfig = True

extensions = [
    "sphinx_copybutton",
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_logo = '_static/banner_vertical.svg'
html_favicon = '_static/logo.svg'
html_theme_options = {
    # Remove search/persistent components from the header
    "navbar_persistent": [],
    "navbar_start": [],
    "navbar_center": [],
    "navbar_end": [],

    # Disable specific top-right action buttons
    "use_download_button": False,
    "use_fullscreen_button": False,
    "use_repository_button": False,
}
