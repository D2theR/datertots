
# coding: utf-8

import io
import os
import json
import datetime

title = 'Modifying-Jupyter-Notebook-on-save'
template = "./static_site/blogs/"+title+".html"
# Parses multiple authors from <author> tags
authors = "Dan Rerko"
# Parses a list of tags that will help filter posts on the site.
tags = ["jupyter-notebook", " python", " javascript", "vuejs"]
# Date from model dictionary
created = "2020-08-09 21:23:11.511166+00:00"

with io.open(os.getcwd().replace('notebooks', '')+'/static_site/blogs/posts.json', 'r+', encoding='utf-8') as f:
    data = f.read()  # pre-existing JSON file data
    jdata = json.loads(data)  # JSON load from file
    # For each record in JSON file, run generator
    blog = next((key for key in jdata if key["title"] == title), None)
    if blog is not None:  # Find record that matches title and update it's info
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
    if blog is None:
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
