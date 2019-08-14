## ACM Python Group

### How to run examples

#### 1. install project and requirements:
  * $ cd /path/to/where/you/want/to/install
  * $ git clone https://github.com/NYU-ACM/python-group.git
  * $ cd /Path/To/python-group
  * if you do not have pipenv installed 
    * $ pip install --user pipenv
  * pipenv install requests 

#### 2. edit the config file
* $ mv aspace_htpp/config.ini_template aspace_http/config.ini
* $ nano config.ini * and change the values to valid ones

#### 3. run the examples
* python aspace_http/get.py
* python aspace_http/authenticate.py
