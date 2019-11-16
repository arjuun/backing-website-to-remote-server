import datetime
import tarfile
import pysftp

docRoot = "/var/www/html/"

sftp_host = "x.x.x.x"
sftp_user = "username"
sftp_port = 22
sftp_key  = "/path/to/file.pem"

def archive(s):
        
    dirName = os.path.basename(s.rstrip('/'))
    tobj = datetime.datetime.now()
    timeStamp = '{}-{}-{}-{}-{}'.format(tobj.year,tobj.month,tobj.day,tobj.hour,tobj.minute)
    
    backupname = '/tmp/{}-{}.tar.gz'.format(dirName,timeStamp)    
    os.chdir(s)
    
    tar = tarfile.open(backupname,'w:bz2')   
    tar.add(".")
    tar.close()
    
    return backupname

for location in os.listdir(docRoot):
    
    absPath = os.path.join(docRoot,location)    
    backupName = archive(absPath)
    
    sftp = pysftp.Connection(host=sftp_host,username=sftp_user,port=sftp_port,private_key=sftp_key)    
    sftp.put(backupName)    
    sftp.close()
