import requests
def get_cat_pic():
   url = 'https://api.thecatapi.com/v1/images/search'
   response = requests.get(url)
   if response.status_code == 200:
       pic = response.json()[0]['url']
       width = response.json()[0]['width']
       height = response.json()[0]['height']
       return pic, width, height
   else:
       return None

print(get_cat_pic())