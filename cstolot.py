def connect():
    s=input("servers : ")
    d=input("dbname : ")
    u=input("username : ")
    p=input("password : ")
    return "server={};db={};user={};password={}" .format(s,d,u,p)

def cstolot(cs):
    return[tuple (i.split('=')) for i in cs.split('i')]

print(cstolot(cs))
