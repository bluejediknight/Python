import os
import codecs
import datetime
import sqlite3
from utilities import *
import math

r = "C:\\SQL\\rpg.db"

def buildrpgjson(src):
    json = "var data = ["

    monsters = getData("SELECT * FROM monsters ORDER BY Name;")    
    locations = getData("SELECT * FROM terrains;")
    monster_location = getData("SELECT MID,TID FROM monster_terrain;")
    sources = getData("SELECT ID,Name,ShortName FROM sources;")
    qualities = getData("SELECT * FROM qualities;")
    monster_quality = getData("SELECT MID,QID FROM monster_quality;")
    types = getData("SELECT * FROM types;")
    monster_type = getData("SELECT MID,TID FROM monster_type;")
    monster_freq = getData("SELECT MID,FID FROM monster_frequency;")
    
    for monster in monsters:
        monsterid = str(monster[0])
        #{"ID","Name","HD","PAGE",
        json += "{\"ID\":" + monsterid + ",\"Name\":\"" + str(monster[1]) + "\",\"HD\":" + str(monster[2]) + ",\"PAGE\":" + str(monster[3]) + ",\r\n"

        # "source":{"ID":15,"Name":"Monsters and Treasure 5th Printing","ShortName":"M&T"},
        for source in sources:
            if str(source[0]) == str(monster[4]):
                json += "\"source\":{\"ID\":" + str(source[0]) + ",\"Name\":\"" + source[1] + "\",\"ShortName\":\"" + source[2] + "\"},\r\n"

        # "qualities":[
        #   {"ID":26,"Name":"Boss","desc":null},
        #   {"ID":37,"Name":"Guardian","desc":null}
        # ],
        json += "\"qualities\":"
        tempqualities = ""
        for quality in monster_quality:
            if str(quality[0]) == monsterid:
                tempqualities += "{\"ID\":" + str(quality[1]) + "},"
        if tempqualities == "":
            json += "null,\r\n"
        else:
            json += "[" + tempqualities[:-1] + "],\r\n"
        
        # "terrains":[{"ID":13,"Name":"Hills"},{"ID":4,"Name":"Mountains"}],
        json += "\"terrains\":"
        tempterrains = ""
        for terrain in monster_location:
            if str(terrain[0]) == monsterid:
                tempterrains += "{\"ID\":" + str(terrain[1]) + "},"
        if tempterrains == "":
            json += "null,"
        else:
            json += "[" + tempterrains[:-1] + "],\r\n"
   

        # "types":[{"ID":1,"Name":"Abberation","Desc":null}],
        json += "\"types\":"
        temptypes = ""
        for typee in monster_type:
            if str(typee[0]) == monsterid:
                temptypes += "{\"ID\":" + str(typee[1]) + "},"
        if temptypes == "":
            json += "null,"
        else:
            json += "[" + temptypes[:-1] + "],\r\n"


        # "SingleFrequency":2}"
        frequencyid = 1
        for freq in monster_freq:
            if str(freq[0]) == monsterid:
                frequencyid = str(freq[1])
        json += "\"SingleFrequency\":" + frequencyid + "},\r\n"
    
    json += "];\r\n\r\n"


    #locations
    json += "var locationdata = ["
    for location in locations:        
        json += "\r\n{\"ID\":" + str(location[0]) + ",\"Name\":\"" + str(location[1]) + "\"},"
    json = json[:-1] + "\r\n];\r\n\r\n"

    #qualities
    json += "var qualitydata = ["
    for quality in qualities:        
        json += "\r\n{\"ID\":" + str(quality[0]) + ",\"Name\":\"" + str(quality[1]) + "\"},"
    json = json[:-1] + "\r\n];\r\n\r\n"

    #types
    json += "var typedata = ["
    for typee in types:        
        json += "\r\n{\"ID\":" + str(typee[0]) + ",\"Name\":\"" + str(typee[1]) + "\"},"
    json = json[:-1] + "\r\n];\r\n\r\n"


    writeAndSave(json, os.path.join(src,"rpg\\data.js"))

def getData(sql):
    cnxn = sqlite3.connect(r)
    cursor = cnxn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cnxn.commit()
    cnxn.close()
    return rows
