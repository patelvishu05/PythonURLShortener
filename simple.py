#!/usr/bin/python3

import json
from os import path

class ShortURL:


    def __init__(self):



    if path.exists("data.json"):
        with open("data.json") as f:
            shortenedUrls = json.load(f)

    visitCounter = {}
    if path.exists("counter.json"):
        with open("counter.json") as f:
            visitCounter = json.load(f)

    choice = 0

    while int(choice) != 3:
        print("\nChoose from the following :")
        print("1. Shorten URL")
        print("2. Visit URL")
        print("3. Exit")
        choice = input("> : ")

        if int(choice) == 1:
            desiredUrl = input("Please enter the URL you want to shorten: ")
            shortUrl = input("Please enter the desired short url: ")
            shortenedUrls["http://localhost/"+shortUrl] = desiredUrl
            visitCounter["http://localhost/"+shortUrl] = 0

            writer = json.dumps(shortenedUrls)
            f = open("data.json","w")
            f.write(writer)

            writer = json.dumps(visitCounter)
            f = open("counter.json","w")
            f.write(writer)
            f.close()
        
        if int(choice) == 2:
            visitUrl = input("Please enter the url you want to visit: ")
            print(shortenedUrls[visitUrl])
            
            tempCounter = visitCounter[visitUrl] + 1
            visitCounter[visitUrl] = tempCounter

            writer = json.dumps(visitCounter)
            f = open("counter.json","w")
            f.write(writer)
            f.close()
        