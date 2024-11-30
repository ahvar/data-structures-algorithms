import csv
import pprint
from pprint import PrettyPrinter

column_headers = ['Date','Open','High','Low','Close','Volume']
pp = PrettyPrinter(indent=4)
fb_price_hist = {}

def add_row(**kwargs):
    for k,v in kwargs.items():
        if k not in fb_price_hist:
            fb_price_hist[k] = [v]
        else:
            fb_price_hist[k].append(v)


with open('../data/FB.csv','r') as fb_in:
    fb_reader = csv.DictReader(fb_in, fieldnames=column_headers)
    header = ""
    for row in fb_reader:
        row = {k:v for k,v in row.items() if k != None}
        add_row(**row)



if __name__ == '__main__':
    simple = zip(['one','two','three'], [1,2,3])
    print(dict(simple))

