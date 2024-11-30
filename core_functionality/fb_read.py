import csv
import pprint
from pprint import PrettyPrinter

column_headers = ['Date','Open','High','Low','Close','Volume']
pp = PrettyPrinter(indent=4)
fb_price_hist = {}

def add_row(**kwargs):
    for k,v in kwargs.items():
        if fb_price_hist.setdefault(k,v):
            pass



with open('../DATA/FB.csv','r') as fb_in:
    fb_reader = csv.DictReader(fb_in, fieldnames=column_headers)
    header = ""
    for row in fb_reader:
        row = {k:v for k,v in row.items() if k != None}
        add_row(**row)



if __name__ == '__main__':
    pp.pprint(fb_price_hist)

