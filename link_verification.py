#!python3
#link_verification
#program is capable of checking if all URLs on certain site are valid

import bs4, requests
url = 'http://www.onet.pl/'
limit = 100 #check only frst 100 links


res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

bad_links = []
count =0
for link_attr in soup.select('a'):
    link = link_attr.get('href')
    count+=1
    #if link.startswith('#') or link.startswith('/#'):
    #    continue
    try:
        res2 = requests.get(link)
        print(f'{count}) status: {res2.status_code}, link: {link}')
        if res2.status_code == 404:
            bad_links.append(link)
    except Exception:
        bad_links.append(link)
    if count == limit:
        break
if len(bad_links) != 0:
    print(f"On the page: {url} these links are invalid:")
    for i, l in enumerate(bad_links):
        print(f"  {i+1}){l}")
else:
    print(f"All the links on the page: {url} \nare valid!")
    

