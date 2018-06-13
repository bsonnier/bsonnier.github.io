codefile = open("./bsonnier.github.io/docs/codetag", "r")
lines = codefile.readlines()
print(lines)
codefile.close()

codefilewr = open("./bsonnier.github.io/docs/codetag", "w")
codefilewr.writelines(sorted(lines))
print(sorted(lines))
codefilewr.close()
