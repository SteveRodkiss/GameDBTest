import sqlite3

def PrintAllProducts():
    with sqlite3.connect("jbhifi.db") as db:
        sql = '''select * from product'''
        cursor = db.cursor()
        cursor.execute(sql)
        products = cursor.fetchall()
        print(products)
       

def query(sql,data):
    with sqlite3.connect('jbhifi.db') as db:
        cursor = db.cursor()
        cursor.execute(sql,data)
        db.commit()

def InsertSale(date,listOfItemCodes):
    print(date)
    print(listOfItemCodes)
    with sqlite3.connect('jbhifi.db') as db:
        cursor = db.cursor()
        #create the query
        sql = "INSERT INTO sale (date) values (?)"
        #execute the insert and pass the date- must be a tuple hence the ,
        cursor.execute(sql,(date,))
        #this is tricky! sqlite creates a unique ID for every sale if we dont specify the ID- we need it to pass to the
        #productsale entry so we can find all the products that were sold in that particular transaction
        uniqueID = cursor.lastrowid
        #now for every item in the list, insert an instance it into the productSale table using uniqueID for the sale
        for itemCode in listOfItemCodes:
            sql = "INSERT INTO productSale (productID,saleID) values(?,?)"
            cursor.execute(sql,(itemCode,uniqueID))
        db.commit()

def GetSaleInfo():
    items = []
    while input("Would you like to buy something?") == "y":
        items.append(int(input("type in item code")))
    return items



if __name__ == "__main__":
    #main program starts here
    #print the whole database
    #salesItems = [1,4,3,2]
    #InsertSale("2017-8-5",salesItems)
    while input("Another Sale? y/n") == "y":
        items = GetSaleInfo()
        date = input("date? YYYY-MM-DD ")
        InsertSale(date,items)
    print("end program")
    


=======
import sqlite3

def PrintAllProducts():
    with sqlite3.connect("jbhifi.db") as db:
        sql = '''select * from product'''
        cursor = db.cursor()
        cursor.execute(sql)
        products = cursor.fetchall()
        print(products)
       

def query(sql,data):
    with sqlite3.connect('jbhifi.db') as db:
        cursor = db.cursor()
        cursor.execute(sql,data)
        db.commit()

def InsertSale(date,listOfItemCodes):
    print(date)
    print(listOfItemCodes)
    with sqlite3.connect('jbhifi.db') as db:
        cursor = db.cursor()
        #create the query
        sql = "INSERT INTO sale (date) values (?)"
        #execute the insert and pass the date- must be a tuple hence the ,
        cursor.execute(sql,(date,))
        #this is tricky! sqlite creates a unique ID for every sale if we dont specify the ID- we need it to pass to the
        #productsale entry so we can find all the products that were sold in that particular transaction
        uniqueID = cursor.lastrowid
        #now for every item in the list, insert an instance it into the productSale table using uniqueID for the sale
        for itemCode in listOfItemCodes:
            sql = "INSERT INTO productSale (productID,saleID) values(?,?)"
            cursor.execute(sql,(itemCode,uniqueID))
        db.commit()

def GetSaleInfo():
    items = []
    while input("Would you like to buy something?") == "y":
        items.append(int(input("type in item code")))
    return items



if __name__ == "__main__":
    #main program starts here
    #print the whole database
    #salesItems = [1,4,3,2]
    #InsertSale("2017-8-5",salesItems)
    while input("Another Sale? y/n") == "y":
        items = GetSaleInfo()
        date = input("date? YYYY-MM-DD ")
        InsertSale(date,items)
    print("end program")
    


>>>>>>> fb58f84bf756a3944ef10767f5e71941983b03eb
