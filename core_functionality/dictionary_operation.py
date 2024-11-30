abc = {'a': 1, 'b': 2, 'c':3}
_def = {'d': 4, 'e': 5, 'f':6}
def data_opt(**kwargs):
    for arg,v in kwargs.items():
        abc.update([(arg,v)])

#data_opt(**_def)
abc.update(_def)
print(abc)
        

