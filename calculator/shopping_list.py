shopping = {
    'chips':2
}
shopping['butter'] = 1
shopping['egg'] = 10
shopping['meat'] = 1
# update
shopping['chips'] = 3
# buy
shopping.pop('chips')
# delete
del shopping['butter']
# print
print(shopping)