from bs4 import BeautifulSoup
with open('post.html') as f:
    post=BeautifulSoup(f, 'lxml')
with open('static_site/index.html') as f:
    index=BeautifulSoup(f, 'lxml')

nav_bar = index.find('nav')

last_div=[div for div in post.body.find_all('div')][-1]
first_div=post.body.find('div')
first_div.insert_before(nav_bar)
for link in index.find_all('link'):
    last_div.insert_after(link)
for script in index.find_all('script'):
    last_div.insert_after(script)


for ele in post.find_all("div", class_="prompt input_prompt"):
    ele.decompose()

for ele in post.find_all("div", class_="prompt output_prompt"):
    ele.decompose()


with open('out.html','w') as o:
    o.write(str(post.html))

