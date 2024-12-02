import requests

def getInput(year, day):
    SESSION_TOKEN="53616c7465645f5faa5ac7f64d0b8bccfbc84ace489cf2e342615b886513f5c947b6ffa2f33c35c783fb57139cd4ab83e77ac8e395fb4d0c754faaddd2726f11"
    cookies = {"session": SESSION_TOKEN}
    URL = "https://adventofcode.com/{0}/day/{1}/input".format(year, day)
    response = requests.get(URL, cookies=cookies)
    data = response.text
    print(data)
    with open('input.txt', 'w') as file:
        file.write(data)
    print("Data has been successfully saved to input.txt")
