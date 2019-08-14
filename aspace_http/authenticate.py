import requests
import configparser
import json


def main():
  config = configparser.ConfigParser()
  config.read("aspace_http/config.ini")
  config.sections

  aspace_host = config['aspace']['host']
  username = config['aspace']['username']
  password = config['aspace']['password']
  login = (f'{aspace_host}/users/{username}/login?password={password}')

  request = requests.post(login)
  status = request.status_code 

  if status == 200:
    response = json.loads(request.content)
    key = response["session"]
    print(f'Session Key is: {key}')
  else:
    print (f"error returned, code {status}")

if __name__ == '__main__':
    main()