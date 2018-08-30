import requests
import random
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn"
req = requests.get(url).text
doc = BeautifulSoup(req, 'html.parser')

title_tag = doc.select('dt.tit > a')
star_tag = doc.select('div.star_t1 > a > span.num')
reserve_tag = doc.select('div.star_t1.b_star > span.num')
img_tag = doc.select('div.thumb > a > img')
'''
print(len(title_tag))
print(len(star_tag))
print(len(reserve_tag))
'''
movie_dic = {}
for i in range(0,10):
    movie_dic[i] = {
        "title":title_tag[i].text,
        "star":star_tag[i].text,
        "reserve":reserve_tag[i].text,
        "img":img_tag[i].get('src')
    }

pick_movie = movie_dic[random.randrange(0,10)]

print(pick_movie)

'''
return_doc = doc.select('dt.tit > a')

list_movies = []
for i in return_doc:
    list_movies.append(i.text)

list_stars = []
return_doc = doc.select('a > span.num')
for a in return_doc:
    list_stars.append(a.text)
    
    print(list_stars)

list_reserve = []
return_doc = doc.select('div.article > div > div.lst_wrap > ul > li > dl > dd.star > dl.info_exp > dd > div > span.num')
for i in return_doc:
    list_reserve.append(i.text)
    
    print(list_reserve)     

print(list_movies)      '''
