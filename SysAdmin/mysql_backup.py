#!/usr/bin/python

import os
import os.path
import logging
import datetime


from operator import itemgetter


class MysqlBackup:
    test = "hiii"
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.pwd = "passwrd"
        self.port = "3306"
        self.store = "backup/"
        self.awsprofile = "backup"
        self.awss3path = "s3://bucket/backups/test/"

    def get_dblist(self):

        list_cmd = "mysql -u" + self.user
        if self.host != None:
            list_cmd += " -h " + self.host
        if self.pwd != None:
            list_cmd += " -p" + self.pwd
        list_cmd += " --silent -N -e 'show databases'"
        databases = os.popen(list_cmd).readlines()
        return [s.strip() for s in databases]

    def backup(self):
        # get the current date and timestamp and the zero backup name
        tstamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        print(tstamp)
        dblist = self.get_dblist()
        skip = ["information_schema", "performance_schema", "test"]
        if not os.path.exists(self.store):
            os.mkdir(self.store)


        for db in dblist:
            if db in skip:
                continue



            dbbackup_name = tstamp+"_"+db+".sql"
            dbbackup_path = self.store+dbbackup_name
            dump_cmd = "mysqldump -u " + self.user
            if self.host != None:
                dump_cmd += " -h " + "'" + self.host + "'"
            if self.pwd != None:
                dump_cmd += " -p" + self.pwd
            dump_cmd += " -e --opt -c " + db + " | gzip > " + dbbackup_path + ".gz"
            logging.info("Dump db, %s to %s." % (db, dbbackup_path))
            os.popen(dump_cmd)
            file = dbbackup_path+".gz"

            aws_cli = "aws --profile "+ self.awsprofile +" s3 cp "+file + " "+self.awss3path
            try:
                os.popen(aws_cli)
            except os.OSError as e:
                print("Erroooooooooor")







    def main():
        print("Enter into Main")





    if __name__ == '__main__':
        main()

myobj = MysqlBackup()
dblist = myobj.backup()
