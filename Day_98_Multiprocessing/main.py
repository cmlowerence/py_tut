# Multiprocessing in Python

# ?Multiprocessing is a python module that provides a simple way to run multiple processes in parallel. It allows us to take advantage of multiple cores or processors of our system and can significantly improve the performance of our code.

import multiprocessing
import requests
import os
import concurrent.futures
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def downloadFIle(url, file_name):
  print()
  print(f"Download Start for {file_name}")
  print()
  files = requests.get(url)
  if not os.path.isdir('files'):
    os.mkdir("./files")
  open(f"files/{file_name}.jpg", 'wb').write(files.content)
  print(f"File {file_name} Downloaded!")
  print()


if __name__ == "__main__":
  urls = ['https://picsum.photos/id/28/2500/1667', 'https://picsum.photos/id/100/2500/1667', 'https://picsum.photos/id/7/2500/1667','https://picsum.photos/id/37/2500/1667','https://picsum.photos/id/737/200/167']
  process_list = []

  # for index,url in enumerate(urls,1):
  #   p = multiprocessing.Process(target=downloadFIle, args=[url,f'file{index}'])
  #   p.start()
  #   process_list.append(p)

  # for p in process_list:
  #   p.join()
  with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(downloadFIle, [urls, [i for i in range(len(urls))]])
    for result in results:
      print(result)