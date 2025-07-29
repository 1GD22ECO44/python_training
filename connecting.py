import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="pavan_ece" 
)
# print("connected to the database successfully")
class Person:
    def print_name(self,name):
        print("my nam is",+name )
        def add(self,a,b):
            return a+b
        person = person()
        person.print_name("sudha")
        result = person.add(3,5)
#         print(result)
class city:
    def addCityDetails(self,name,country):
        self.name = name
        self.country = country
    def printCityDetails(self):
        print("City name:"+self.name)
        print("country:"+self.country)

delhi = city()
delhi.addCityDetails("delhi","india")
delhi.printCityDetails()
mumbai = city()
mumbai.addCityDetails("mumbai","india")
mumbai.printCityDetails()

class person():
    cityName = "mumbai"
    def printName(self,name):
        print(name)

class Ashok(person):
    def printDetails(self):
        print("some messages")

class sudha(person):
    def printDetails(self):
        print("sudha loves ")

obj = Ashok()
obj.cityName = "bangalore"
obj.printName("Ashok")
obj.printDetails()

obj = sudha()
obj.cityName = "dubai"
obj.printName("sudha")
obj.printDetails()
import mysql.connector

def insert_data(id,name,email):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="pavan_ece"
    )
    print("connected to the database successfully")   
    mycursor = mydb.cursor()
    sql = "INSERT INTO people (id,name,email)values (%s,%s,%s)"
    val = [id,name,email]
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    print(mycursor.rowcount,"record inserted.")

id = input("enter the id")
name = input("enter the name")
email = input("enter the email")
