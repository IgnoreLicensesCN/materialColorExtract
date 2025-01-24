from bs4 import BeautifulSoup


def materialNamesFromFile(fileName: str):
    with open(fileName, mode='r') as f:
        s = f.read()
        return s.split('|')

        # this way causes loss
        # soup = BeautifulSoup(f.read(), "lxml")
        # results = []
        # selected = soup.select("div.col-first")
        # # print(selected)
        # for i in selected:
        #     codePart = i.find("code")
        #     if codePart == None:
        #         continue
        #     results.append(codePart.find("a", class_="member-name-link").text)
        # return results


if __name__ == '__main__':
    res = materialNamesFromFile("materialsFromSpigotAPI1214.html")
    print(res)
    print(len(res))
