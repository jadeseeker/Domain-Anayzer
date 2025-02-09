


import sqlite3


class scrapyDatabase():

    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cur = self.conn.cursor()

    #Functions to create database tables
    def createTagTable(self, name):
        try:
            self.cur.execute('create table if not exists ' + name + ' (tag text, position int, url text)')
        except sqlite3.Error as e:
            print "An error occurred: ", e.args[0]

    def createContentTable(self, name):
        try:
            self.cur.execute('create table if not exists ' + name + ' (start_url text, content text)')
            self.conn.commit()
        except sqlite3.Error as e:
            print "An error occurred: ", e.args[0]
    
    def createFrameTable(self, name):
        try: 
            self.cur.execute('create table if not exists ' + name + ' (url text, frameRatio real, frame text, jsRatio real, linkRatio real, script text)')
        except sqlite3.Error as e:
            print "An error occurred: ", e.args[0]
    
    def createScriptTable(self, name):
        try: 
            self.cur.execute('create table if not exists ' + name + ' (url text, script text)')
        except sqlite3.Error as e:
            print "An error occurred: ", e.args[0]

    #Functions to insert information into tables
    def insertTag(self, table_name, row):
        try:
            self.cur.execute('insert into ' + table_name + ' (tag,position,url) values (?,?,?)', (row['tag'], row['position'], row['url']))
        except sqlite3.Error as e:
            print "An error occurred: ", e.args[0]

    def insertContent(self, table_name, row):
        try:
            self.cur.execute('insert into ' + table_name + ' (start_url,content) values (?,?)', (row['start_url'], row['content']))
            self.conn.commit()
        except sqlite3.Error as e:
            print "An error occurred: ", e.args[0]

    def insertFrame(self, table_name, row):
        try:   
            self.cur.execute('insert into ' + table_name + ' (url, frameRatio, frame, jsRatio, linkRatio, script) values (?,?,?,?,?,?)', (row['url'], row['frameRatio'], row['frame'], row['jsRatio'], row['linkRatio'], row['script']))
        except sqlite3.Error as e:
            print "An error occurred: ", e.args[0]
    
    def insertScript(self, table_name, row):
        try:
            self.cur.execute('insert into ' + table_name + ' (url,script) values (?,?)', (row['url'], row['script']))
            self.conn.commit()
        except sqlite3.Error as e:
            print "An error occurred: ", e.args[0]
