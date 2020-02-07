to start a scrapy project , run :
```
scrapy startproject project-name
```


## tips :
- __what i did__ : write basic crawler for digikala that crawl the cellphone list and get price and name of 5 first pages
- __change lists to crawl__ : by changing *Max_List* parameter in *spiders/example.py*
- __change base URL__ : by change *firstUrl* and *secondUrl* parameters in *spiders/example.py*
- __how to run__ : write in cmd :
```
  cd tutorial
  scrapy crawl example -o crawled.csv
```
this peice of code , run this program and save the result in csv file
- __robot name__ : robot name is set in the *.py* file said . and by bot name you can run the crawler
- __important tip__ : digikala couldn't be crawled until i set 2 variables in *settings.py* 
  - USER_AGENT
  - ROBOTSTXT_OBEY
- __save data__ : to save data you must write *TutorialItem* class in *items.py* and call this class in *example.py*
- __video to learn__ : i watch some videos of [this link](https://www.youtube.com/playlist?list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t). 



## some good cmds:

```
scrapy shell 'url'
```
this will run and crawl url and then you can see and manipulate resuts like in *ipython notebook*

```
scrapy crawl example
```
runs the code

```
scrapy startproject tutorial
```
this will create your new crawler
