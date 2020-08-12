# ![](./static_site/src/logo.png)

### Installation

Run the <code>install_env.sh</code> script to install local repository for writing blog posts in Jupyter Notebook.

---

### Usage

Within the install virtual enviroment run

<code>jupyter notebook --config="./scripts/jupyter_notebook_config.py"</code>

The extra config file generates an .html file in /blogs directory in addition to creating a .ipynb file when saving a notebook.
It strips some of the input `<div>` tags out of the blogs HTML file to make them a little "prettier" and
also makes and entry for the post in blogs/posts.json

For more details see the `notebooks/Blog-post-template.ipynb` file to get started.
