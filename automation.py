#!/usr/bin/python3
''' Automate of running WSA Engine '''
import mysql.connector
import datetime

def main():
    ''' Script to automate running of all basketball engine daily '''
    run_scrapers()

def run_scrapers():
    ''' Run the scrapers '''
    cnx = mysql.connector.connect(user="wsa@wsabasketball",
                                  host='wsabasketball.mysql.database.azure.com',
                                  database="basketball",
                                  password="")
    cursor = cnx.cursor(buffered=True)

    cursor = cnx.cursor()    
    now = datetime.datetime.now()

    print str(now.year)+ "-" + str(now.month) + "-" + str(now.day)
    date =  str(now.year)+ "-" + str(now.month) + "-" + str(now.day)
    

    # first figure out what day it is through some way
    # get current date 
    findGame = "SELECT iddates FROM new_dates WHERE date = %s"
    findGameData = (date,)
    # then query database to get that dateI
    cursor.execute(findGame, findGameData) 
    dateID = cursor.fetchall()[0][0]
    

    # run player reference scaper

    # run generate box score urls

    # run performance 

    # run team performance

    # 3 Extrapilators

    # fandual scraper 

    # daily minutes

    # machine learning stuff

    pass
