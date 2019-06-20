def connect(severname,dbname,username,password):
    connectstring = 'sername='+servername +';dbname='+dbname +';username='+username + ';password='+password
    return connectstring


servername=input('Enter the server name : ')
dbname=input('enter the db name : ')
username=input('enter the desired username : ')
password=input('create a password : ')

res=connect(servername,dbname,username,password)
print (res)
