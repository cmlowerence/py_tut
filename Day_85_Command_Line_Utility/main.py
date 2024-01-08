# Creating Command Lne Utilities in Python
import argparse
import requests

def download_file(url, local_filename):
  if local_filename is None:
    local_filename = url.split('/')[-1]
    
  with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open(local_filename, 'wb') as f:
      for chunk in r.iter_content(chunk_size=8192):
        # If we have chunk encoded response uncomment if
        # and set chunk_size parameter to None.
        # if chunk:
          f.write(chunk)
  return local_filename

parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument('url', help= 'Url of the file to be downloaded')
# parser.add_argument('output', help='By which name you want to save your file')
parser.add_argument("-o", "--output", help="Name of the file", default=None)
# Parse the arguments
args = parser.parse_args()

# Use the argument in our code
print(args.url)
# print(args.output, type(args.output))
download_file(args.url, args.output)