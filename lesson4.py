import selenium
import monte-screen-recorder
# import requests
# import flask
# from flask import Flask, request
from selenium import webdriver
# from time import sleep
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':


print("Script started")
def main():
    print("Running my Python script!")

    # Rest of your script code here

if __name__ == "__main__":
    main()

a = webdriver.Chrome()
a.get("http://ynet.co.il")
a.get("http://mako.co.il")
# sleep(4)
# response = requests.get("https://api.github.com/users/avielb/repos")
# if response.status_code == 200:
#     print("All good")
# else:
#     print("Something didn't work right, status code is " , response.status_code)
# response_text = response.text
print("Ending script")
#
# app = Flask("Something")
#
# @app.route('/cars', methods=['GET','POST'])
# def user_name():
#     if request.method == 'GET':
#         return 'Citroen; Mazda, Toyota'
#     if request.method == 'POST':
#         return ('New car created')
#
# app.run(host="127.0.0.1", port=5001)
