
### This is download image from internet

import random  # this Lib create random number
import urllib.request  # this Lib for download url

def download_web_image(url):
    name = random.randrange(1, 1000)  # this one create random number, it will use file name.
    full_name = str(name) + ".jpg"    # str(name) means the random number change to string value. so the file name will be 230.jpg 230 is random number
                                      # 230 is create from random function, 230 is just example I don't know what will be

    urllib.request.urlretrieve(url, full_name)
    # first parameter url means the function download_web_image parameter is url, it should be same as that function parameter
    # save as the random number.jpg coz full name is random number.jpg

download_web_image("https://scontent.fsnc1-1.fna.fbcdn.net/hphotos-xat1/v/t1.0-9/1621698_10152575120409583_5494733456983722756_n.jpg?oh=5498f00401a294b9297a5749994ea3b7&oe=57172625")
### https:// ..... this one is parameter for function download_web_image(url):




### This is download file from internet (this example of ericsson's history price file download

from urllib import request # this is different way to import Lib

eric_url = 'http://real-chart.finance.yahoo.com/table.csv?s=ERIC&d=11&e=29&f=2015&g=d&a=8&b=28&c=1989&ignore=.csv'

def download_stock_data(csv_url):  ### csv_url will be provided. it should be same as http://....
    response = request.urlopen(csv_url)    ### response means connect to internet
    csv = response.read()   ## whatever read csv_url store to csv variable
    csv_str = str(csv)   ### the csv will convert to string and store to csv_str variable.
    lines =csv_str.split("\\n")  ### this is break line but I don't know when it break ???
    dest_url = r'eric.csv' ### this is save file name as eric.csv Not sure what is mean of 'r'
    fx = open(dest_url, "w") ### open the file and will do write
    for line in lines:         ### lines data 를 loop 하면서
        fx.write(line + "\n")  ### each line 마다 return
    fx.close()   ### close file

download_stock_data(eric_url) ## call function download_web_image and parameter is eric_url which means http://

