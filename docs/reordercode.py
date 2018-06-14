def reorderfile(filename):
    codefile = open(filename, "r", encoding='utf-8')
    lines = codefile.readlines()
    lines[-1] = lines[-1] + '\n'
    print(lines)
    codefile.close()

    codefilewr = open(filename, "w", encoding='utf-8')
    sortedlines = sorted(lines)
    sortedlines[-1] = sortedlines[-1][0:-1]
    codefilewr.writelines(sortedlines)
    print(sortedlines)
    codefilewr.close()


if __name__ == '__main__':
    reorderfile("./bsonnier.github.io/docs/codefilter")
    reorderfile("./bsonnier.github.io/docs/codetag")
    reorderfile("./bsonnier.github.io/docs/namelist")
