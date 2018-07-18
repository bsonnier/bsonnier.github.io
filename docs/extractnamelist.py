from bs4 import BeautifulSoup


def extractname(filename, filenamewr):
    namelist = []
    soup = BeautifulSoup(open(filename, encoding='utf-8'), "lxml")
    for star in soup.find_all('span', 'star'):
        namelist.append(star.string + '\n')

    codefilewr = open(filenamewr, "w", encoding='utf-8')
    sortedlines = sorted(namelist)
    sortedlines[-1] = sortedlines[-1][0:-1]
    codefilewr.writelines(sortedlines)
    print(sortedlines)
    codefilewr.close()


if __name__ == '__main__':
    extractname("./bsonnier.github.io/docs/favstars-mjyang-1531891897.html",
                "./bsonnier.github.io/docs/favstars-mjyang-1531891897")
