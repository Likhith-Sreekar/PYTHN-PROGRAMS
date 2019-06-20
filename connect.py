def connect():
    s=input("servers : ")
    d=input("dbname : ")
    u=input("username : ")
    p=input("password : ")
    return "server={};db={};user={};password={}" .format(s,d,u,p)
