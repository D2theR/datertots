# ![](./static_site/src/logo.png)

### Installation

 Run the <code>install_env.sh</code> script to install local repository for writing blog posts in Jupyter Notebook.

### Usage

Within the install virtual enviroment run

<code>jupyter notebook --config="./scripts/jupyter_notebook_config.py"</code>

The extra config file generates an .html file in addition to a .ipynb file when saving a notebook.
It also strips some of the input `<div>` tags out of the file and makes the container a little "prettier".
