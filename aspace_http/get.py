import requests
import configparser
import json


def main():
  config = configparser.ConfigParser()
  config.read("config.ini")
  config.sections

  aspace_host = config['aspace']['host']

  request = requests.get(aspace_host)
  status = request.status_code

  if status == 200:
    print(request.content)
  else: 
    print("error code: " + str(status))


if __name__ == '__main__':
    main()