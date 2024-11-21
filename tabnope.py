import requests
import sys
import re
import pyfiglet

imported_file = sys.argv[1]


def make_request(url):
    response = requests.get(url)
    text = response.text
    pattern = r"<a\b[^>]*>.*?<\/a>"
    a_tags = re.findall(pattern, text)
    target_blanks = []
    nabs = []

    for tag in a_tags:
        if 'target="_blank"' in tag:
            target_blanks.append(tag)

    for link in target_blanks:
        if 'noopener' not in link:
            nabs.append(link)
    
    if len(nabs) > 0:
        return [True, url, nabs]
    else:
        return [False]

def checker(file):
    valid = []
    with open(file, 'r') as file:
        for line in file:
            result = make_request(line)
            if result[0] == True:
                print("---- URL ----")
                print(result[1])
                print("Links")
                for link in result[2]:
                    print("   * " + link)
                print("\n")
                valid.append(line)


Art= pyfiglet.figlet_format("tabNope!")
print(Art)

print("Ok let's get it!!")

checker(imported_file)
