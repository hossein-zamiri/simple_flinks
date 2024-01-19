import requests
import re
url = input("enter your target: ")
def robots():
    domain = f"https://web.archive.org/cdx/search/cdx?url={url}/robots.txt&output=json&filter=statuscode:200&fl=timestamp,original&collapse=digest"
    req = requests.get(domain)
    response = req.text
    return response
def get_time_stamps():
    call_robots = robots()
    change_to_array = eval((call_robots))
    change_to_array.pop(0)
    return change_to_array

def get_content():
    call_get_time_stamps = get_time_stamps()
    list_responses = []
    for time_stamps in call_get_time_stamps:
        time_stamp = time_stamps[0]
        domain = f"https://web.archive.org/web/{time_stamp}if_/{url}/robots.txt"
        req = requests.get(domain)
        response1 = req.text
        list_responses.append(response1)
    return list_responses

def links():
    global url
    s = get_content()
    res = [*set(s)]
    for i in res:
        h = re.findall(r'\/.*',i)
        return h

links()
