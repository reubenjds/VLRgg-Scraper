from bs4 import BeautifulSoup as soup
from  urllib.request import urlopen as uReq

my_url = "https://www.vlr.gg/stats/?event_group_id=3&event_id=all&region=na&country=all&min_rounds=300&agent=all&map_id=all&timespan=all"
urlclient = uReq(my_url)
page_html = urlclient.read()
urlclient.close()
page_soup = soup(page_html, "html.parser")
print(page_soup.head.title)
tbody = page_soup.find("tbody")
containers = tbody.findAll('tr')
filename = "data.csv"
f = open(filename, "w")
headers = "Player_Name, ACS, KD, HS%\n"
f.write(headers)
for container in containers:
    name_container = container.find("td", {"class": "mod-player mod-a"})
    name = name_container.a.div.text.replace("\n", " ").strip()
        

    mod_color_instances = container.findAll("td", {"class": "mod-color-sq"})
    acs = mod_color_instances[0].div.text.strip()
    kd = mod_color_instances[1].div.text.strip()
    hs = mod_color_instances[7].div.text.strip()

    f.write(name + "," + acs + "," + kd + "," + hs + "\n")
    print(name)
    print(acs)
    print(kd)
    print(hs)
f.close
