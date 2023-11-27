s = [1, 2, 3, 4, 5, 6, 7, 8]

for i in s:
    exec("lista%s= [x for x in range(%s)]" % (i, i))

for i in s:
    exec("print('lista-%s',lista%s)" % (i, i))
