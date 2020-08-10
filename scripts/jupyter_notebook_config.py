# Extra configurations file for jupyter-notebook.
import io
import os
import json
import datetime
from notebook.utils import to_api_path
from bs4 import BeautifulSoup

_html_exporter = None


def deploy_post(jupyter_data={}):
    """Parses jupyter notebook html file into readable HTML container for blog post deployment.
    """
    post = BeautifulSoup(jupyter_data['html'], 'lxml')

    # Finds 1st header <h1> tag in post and uses it as file name.
    title = [i.get('id') for i in post.find_all("h1", limit=1)][0]
    template = "./blogs/"+title+".html"
    # Parses multiple authors from <author> tags
    authors = " | ".join([i.get_text() for i in post.find_all("author")])
    # Parses a list of tags that will help filter posts on the site.
    tags = [i.get_text() for i in post.find_all(
        "code", limit=1)][0].strip('tags: ').split(',')
    # Date from model dictionary
    created = jupyter_data['created']

    # Parse div elements to make HTML post text/formatting look better
    for ele in post.find_all("div", class_="prompt input_prompt"):
        ele.decompose()
    for ele in post.find_all("div", class_="prompt output_prompt"):
        ele.decompose()

    # Parses a JSON file with all the info need.
    with io.open(os.getcwd().replace('notebooks', '')+'/static_site/blogs/posts.json', 'r+', encoding='utf-8') as f:
        data = f.read()  # pre-existing JSON file data
        jdata = json.loads(data)  # JSON load from file
        # For each record in JSON file, run generator
        blog = next((key for key in jdata if key["title"] == title), None)
        if blog is not None:  # Find record that exists with title and update it.
            new_blog = {
                'title': title,
                'template': template,
                'authors': authors,
                'tags': tags,
                'created': str(created)
            }
            blog.update(new_blog)
            f.seek(0)
            json.dump(jdata, f, indent=2)
            f.truncate()
            print('Updated existing record: ', blog)
            f.close()
        if blog is None:  # If record doesn't exist, make it.
            new_record = {
                'title': title,
                'template': template,
                'authors': authors,
                'tags': tags,
                'created': str(created),
            }
            jdata.append(new_record)
            f.seek(0)
            json.dump(jdata, f, indent=2)
            print('Wrote new record to JSON file')
            f.close()
        else:
            f.close()
    # Update changed HTML and add title for saving filename
    jupyter_data['html'] = str(post)
    jupyter_data.update({'title': title})
    return jupyter_data


def html_post_save(model, os_path, contents_manager, **kwargs):
    """Converts notebooks to HTML after save with nbconvert's HTMLExporter
    ### For more information on Jupyter notebooks config files and save hooks:
    ### https://jupyter-notebook.readthedocs.io/en/stable/extending/savehooks.html
    """
    from nbconvert.exporters.html import HTMLExporter

    if model['type'] != 'notebook':
        return

    global _html_exporter

    if _html_exporter is None:
        _html_exporter = HTMLExporter(parent=contents_manager)

    log = contents_manager.log

    base, ext = os.path.splitext(os_path)
    html, resources = _html_exporter.from_filename(os_path)
    # Parse html file above using BeautifulSoup4
    model.update({'html': html})
    parsed_html = deploy_post(model)
    # Parse filename for new post.
    html_fname = os.getcwd()+'/static_site/blogs/'+parsed_html['title']+'.html'
    log.info("Saving HTML blog post /%s",
             to_api_path(html_fname, contents_manager.root_dir))

    # Write blog post to disk
    with io.open(html_fname, 'w', encoding='utf-8') as f:
        f.write(parsed_html['html'])
        f.close()


c.FileContentsManager.post_save_hook = html_post_save
