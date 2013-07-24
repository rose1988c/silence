import os
import time

def getFileList( p ):

        p = str( p )

        if p=="":

              p = os.getcwd()

        p = p.replace( "/","\\")

        if p[ -1] != "\\":

             p = p+"\\"

        a = os.listdir( p )

        for what in a:
            if os.path.isfile( p + what ):
                #print what
                statinfo = os.stat(what)

                #filetime = time.localtime(statinfo.st_ctime)
                #timefix = "%04d-%02d-%02d-" % (filetime.tm_year, filetime.tm_mon, filetime.tm_mday)

                timefix = time.strftime(r"%Y-%m-%d-",time.localtime(statinfo.st_mtime))

                filename = os.path.splitext(what)[0]
                is_hasyear = filename.split("-", 1)[0]

                if is_hasyear.isdigit():
                    continue

                print what + '----->' + timefix + what
                os.rename(what, timefix + what)



        #b = [ x   for x in a if os.path.isfile( p + x ) ]

        #return b

path = raw_input("press input dir: ")
print   getFileList( path )

print        
raw_input("press Enter to exit")
sys.exit()