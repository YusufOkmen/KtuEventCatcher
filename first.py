import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

url = "https://www.ktu.edu.tr/tr/etkinlikler"

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# for event in eventHeader:
#     print(event.text.strip())

events = soup.find_all("a", class_="etk")

# Temporary dictionary to store merged data
eventDict = {}

for event in events:
    eventHeader = event.find_all("h5")
    colAutos = event.find_all("div", class_="col-auto")
    for header in eventHeader:
        eventHead = header.text.strip()
    for colAuto in colAutos:
        h3Tags = colAuto.find_all("h3")
        pTags = colAuto.find_all("p")
        for h3Tag, pTag in zip(h3Tags, pTags):
            day = h3Tag.text.strip()
            month = pTag.text.strip()
            date = f"{day} {month}"

            # Control if the date has already readed and append it if it is not.
            if eventHead in eventDict:
                if date not in eventDict[eventHead]:
                    eventDict[eventHead].append(date)
            
            else:
                eventDict[eventHead] = [date]


# Build final list end merge temporary datas
eventDateList = []

for header, dates in eventDict.items():
    if len(dates) == 2:
        mergedDate = f"{dates[0]} - {dates[1]}"
    else:
        mergedDate = dates[0]

    eventDateList.append({
        "header": header,
        "date": mergedDate
    })

for elements in eventDateList:
    print(elements)