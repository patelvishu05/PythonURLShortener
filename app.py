#!/usr/bin/python3

import json
from os import path

class ShortURL:

    def __init__(self,debug):
        self.shortenedUrls = {}
        self.visitCounter = {}
        self.debug = False

        if path.exists("data.json"):
            with open("data.json") as f:
                self.shortenedUrls = json.load(f)

        if path.exists("counter.json"):
            with open("counter.json") as f:
                self.visitCounter = json.load(f)


    def menu(self):
        choice = 0

        # Visually help the user choose the menu
        while int(choice) != 3:
            print("\nChoose from the following :")
            print("1. Shorten URL")
            print("2. Visit URL")
            print("3. Exit")
            choice = input("> : ")

            # If the user chooses 1
            # have the menu direct them to the menu where they can 
            # shorten the URL based on the desired name they would like to use
            if int(choice) == 1:
                desiredUrl = input("Please enter the URL you want to shorten: ")
                shortUrl = input("Please enter the desired short url: ")
                self.shorten(desiredUrl, shortUrl)
               

            # If the user chooses 2
            # Have the menu irect them to the page where they can enter the short URL
            # which will take them to the intended URL with the full URL format
            if int(choice) == 2:
                visitUrl = input("Please enter the url you want to visit: ")
                self.visit(visitUrl)
                

    def shorten(self, desiredUrl, shortUrl):
        self.shortenedUrls["http://localhost/"+shortUrl] = desiredUrl
        self.visitCounter["http://localhost/"+shortUrl] = 0

        # write the existing data for shortened URLs to the json file
        # so that it persists after the termination of the program
        writer = json.dumps(self.shortenedUrls)
        f = open("data.json","w")
        f.write(writer)
        f.close()

        # write the existing data for Metric counts of URL visits to the json file
        # so that it persists after the termination of the program
        writer = json.dumps(self.visitCounter)
        f = open("counter.json","w")
        f.write(writer)
        f.close()

        return "http://localhost/"+shortUrl
            
            
    # The below function will help decrypt the shortened URL back 
    # to its original full format and return it so they the browser
    # can visit the intended URL
    def visit(self, visitUrl):
        tempCounter = self.visitCounter[visitUrl] + 1
        self.visitCounter[visitUrl] = tempCounter


        # write the existing data for Metric counts of URL visits to the json file
        # so that it persists after the termination of the program
        writer = json.dumps(self.visitCounter)
        f = open("counter.json","w")
        f.write(writer)
        f.close()

        return self.shortenedUrls[visitUrl]
    
    def countsVisited(self,website):
        return int(self.visitCounter[website])
        

# Execute the App from the menu for the URL Shortener to begin
urlObj = ShortURL(True)
if urlObj.debug is True:
    urlObj.menu()