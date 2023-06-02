import json

class bc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


json_data = {}
with open('GERESTATHI.json') as json_file:
    json_data = json.load(json_file)



vals = list(json_data.values())

json_inverted = {}
counter = 0

for k in json_data:
    if vals[counter].lower() in json_inverted:
        if type(json_inverted[vals[counter].lower()]) is str:
            json_inverted[vals[counter].lower()] = [json_inverted[vals[counter].lower()], k.lower()]
        else:
            json_inverted[vals[counter].lower()].append(k.lower())

    else:
        json_inverted[vals[counter].lower()] = k.lower()
    counter += 1

looked_words = []

inv = ''

while inv != '1' and inv != '2':
    inv = input(f"{bc.WARNING}EN-GER{bc.ENDC} (1) or {bc.OKGREEN}GER-EN{bc.ENDC} (2)")

print("\033[H\033[J")

if inv == '1':
    keys = list(json_data.keys())
else:
    keys = list(json_inverted.keys())

while True:

    newWords = input(f"what word?: {bc.OKBLUE}").split(" ")
    print(f"{bc.ENDC}")

    for i in newWords:
        looked_words.append(i)


    print("\033[H\033[J")

    for i in looked_words:
        if i.lower() in keys:
            if inv == '1':
                print(bc.WARNING+i+bc.ENDC+': '+bc.OKGREEN+json_data[i.lower()].lower()+bc.ENDC)
            else:
                if type(json_inverted[i.lower()]) is str:
                    print(bc.OKGREEN+i+bc.ENDC+': '+bc.WARNING+json_inverted[i.lower()].lower()+bc.ENDC)
                else:
                    print(bc.OKGREEN+i+bc.ENDC+': '+bc.WARNING)
                    print(json_inverted[i.lower()], end="")
                    print(bc.ENDC)
