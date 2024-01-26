import json
import random
import string

def get_database():
    try:
        with open('database.json', 'r') as file:
            urldata = json.load(file)
    except json.decoder.JSONDecodeError:
        urldata = []
    return urldata

def write_database(url):
    previous_data = get_database()
    url_data ={
        "shortened_link": generate_randomUrl(),
        "main_link": url,
        "ip_addr":[],
        "views": 0
    }
    previous_data.append(url_data)
    with open('database.json', 'w') as file:
        data = json.dumps(previous_data, indent=2)
        file.write(data)
    return url_data['shortened_link']

def generate_randomUrl():
    shortedUrl = ("".join(random.sample(string.ascii_letters, 10)))
    for i in get_database():
        if shortedUrl in i["shortened_link"]:
            generate_randomUrl(get_database())
    else:
        return shortedUrl
    
def update_views(url_link, ip):
    previous_data = get_database()
    for i in previous_data:
        if i['shortened_link'] == url_link:
            i['views'] += 1
            i['ip_addr'].append(ip)
    with open('database.json', 'w') as file:
        data = json.dumps(previous_data, indent=2)
        file.write(data)

def write_customUrl(url, curl):
    previous_data = get_database()
    url_data ={
        "shortened_link": curl,
        "main_link": url,
        "ip_addr":[],
        "views": 0
    }
    previous_data.append(url_data)
    with open('database.json', 'w') as file:
        data = json.dumps(previous_data, indent=2)
        file.write(data)
    return url_data['shortened_link']