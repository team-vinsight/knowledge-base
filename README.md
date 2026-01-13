# Vinsight Knowledge Base

This repository hosts the Research & Development knowledge base for the **Team Vinsight** project.

The documentation is built using [Sphinx](https://www.sphinx-doc.org/) and deployed to GitHub Pages.

## Accessing the Knowledge Base

🔗 **[View Knowledge Base Site](https://team-vinsight.github.io/knowledge-base/)**

## Local Development

To run the documentation locally:

1.  **Install Python** (if not already installed).
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Build the docs**:
    ```bash
    sphinx-build -b html docs docs/_build/html
    ```
4.  Open `docs/_build/html/index.html` in your browser.

## Repository Structure

*   `docs/`: Source files for the documentation site (reStructuredText and Markdown).
*   `docs/conf.py`: Configuration file for Sphinx.
*   `requirements.txt`: Python dependencies for building the documentation.
