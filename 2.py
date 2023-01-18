from PIL import Image
import requests
import time
from functools import wraps
import threading


def time_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + ' ' + 'took' + ' ' + str((end - start)*1000) + 'ms')
        return result
    return wrapper

def cropp_image():
    image_path = 'D:\Wallpaper\cropped-1920-1080-841718.jpg'
    image = Image.open(image_path)
    small_image = image.resize((500, 500))
    small_image.save('image.jpg')


def make_request():
    requests.get('https://python.org')

@time_func
def sync_make_request():
    for i in range(5):
        thr = threading.Thread(make_request())
        thr.start()
        thr.join()

@time_func
def async_make_request():
    for i in range(5):
        thr = threading.Thread(make_request())
        thr.start()

@time_func
def sync_cropp_image():
    for i in range(5):
        thr = threading.Thread(cropp_image())
        thr.start()
        thr.join()

@time_func
def async_cropp_image():
    for i in range(5):
        thr = threading.Thread(cropp_image())  # *5
        thr.start()

if __name__ == '__main__':
    time_func(sync_make_request())
    time_func(async_make_request())
    time_func(sync_cropp_image())
    time_func(async_cropp_image())

'''отримали такі резьтати:
sync_make_request took 2597.8176593780518ms
async_make_request took 2676.072120666504ms
sync_cropp_image took 196.4132785797119ms
async_cropp_image took 157.5784683227539ms
 висновок: результати можна назвати очікуваними тому, що для обробки http запиту та отримання данних з нього забирає 
 набагато більше у часі, у порівнянні з обробкою зображення, яке вже є на комп'ютері, тому, тут вийграло у часі те,
  що обробка зображення не витрачала час на запит і очікування, а вже потім правцювала з данними,
   а одразу почала роботу. '''