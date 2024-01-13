# import time
# import asyncio
# async def func1():
#   await asyncio.sleep(1)
#   print("Func1")
# async def func2():
#   await asyncio.sleep(5)
#   print("Func2")
# async def func3():
#   await asyncio.sleep(1)
#   print("Func3")
  
# # func1()
# # func2()
# # func3()
# async def main():
#   task = asyncio.create_task(func1())
#   print(task)
#   # await func1()
#   await func2()
#   await func3()

# asyncio.run(main())

import asyncio
import requests
import os
import aiohttp
import certifi
import ssl

ssl_context = ssl.create_default_context(cafile=certifi.where())

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# async def main():
#   print("Chudamani")
#   task = asyncio.create_task(foo("Lawrence")) 
#   print("Finish Program")
# async def foo(text):
#   print(text)
#   await asyncio.sleep(4)
# asyncio.run(main())

# async def fetch_data():
#   print("Start fetching")
#   await asyncio.sleep(2)
#   print("done fetching")
#   return {'data' : 1}

# async def print_numbers():
#   for i in range(10):
#     print(i)
#     await asyncio.sleep(.25)

async def main():
  # task1 = asyncio.create_task(fetch_data())
  # task2 = asyncio.create_task(print_numbers())
  
  # value = await task1
  # print(value)
  # await task2
  
  # ! using await
  # await download_img("https://r4.wallpaperflare.com/wallpaper/296/400/37/movie-avengers-infinity-war-black-panther-movie-black-widow-wallpaper-49f0f89d41ba3debf667380fb061667d.jpg")
  
  # await download_img("https://r4.wallpaperflare.com/wallpaper/719/640/12/marvel-comics-the-avengers-spider-man-avengers-infinity-war-wallpaper-88763de8e0e0ec38603c11ce2862f49a.jpg")
  
  # await download_img("https://r4.wallpaperflare.com/wallpaper/857/457/204/iron-man-artwork-comic-books-superhero-wallpaper-88666da850e0ec4830bc51ce986204ea.jpg")
  
  # ! calling function simultaneously
  task1 = asyncio.create_task(download_img("https://r4.wallpaperflare.com/wallpaper/296/400/37/movie-avengers-infinity-war-black-panther-movie-black-widow-wallpaper-49f0f89d41ba3debf667380fb061667d.jpg"))
  
  task2 = asyncio.create_task(download_img("https://r4.wallpaperflare.com/wallpaper/719/640/12/marvel-comics-the-avengers-spider-man-avengers-infinity-war-wallpaper-88763de8e0e0ec38603c11ce2862f49a.jpg"))
  
  task3 = asyncio.create_task(download_img("https://r4.wallpaperflare.com/wallpaper/857/457/204/iron-man-artwork-comic-books-superhero-wallpaper-88666da850e0ec4830bc51ce986204ea.jpg"))
  
  await asyncio.gather(task1, task2, task3)
  
def file_writing(file_name, content):
  with open(file_name,'wb') as f:
    f.write(content)


async def download_img(url):
  print()
  import time
  start_time = time.time()
  print("Start time: ",start_time)
  print()
  
  file_name = url.split("/")[-1]
  async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
    async with session.get(url) as response:
      content = await response.read()
      
      # Writing file using asyncio.to_thread
      print(f"Downloading {file_name}...")
      await asyncio.to_thread(file_writing, file_name, content)
  print("Download Finish")
  end_time = time.time()
  print("End time: ", end_time)
  print()
  print(f"Time taken : {end_time - start_time}")
  print()

asyncio.run(main())