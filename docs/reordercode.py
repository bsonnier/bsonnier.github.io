codefile = open("./bsonnier.github.io/docs/codefilter", "r")
lines = codefile.readlines()
print(lines)
codefile.close()

codefilewr = open("./bsonnier.github.io/docs/codefilter", "w")
codefilewr.writelines(sorted(lines))
print(sorted(lines))
codefilewr.close()
