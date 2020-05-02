from bs4 import BeautifulSoup
with open('post.html') as f:
    soup=BeautifulSoup(f, 'lxml')

for ele in soup.find_all("div", class_="prompt input_prompt"):
    ele.decompose()

for ele in soup.find_all("div", class_="prompt output_prompt"):
    ele.decompose()

with open('out.html','w') as o:
    o.write(str(soup.html))

