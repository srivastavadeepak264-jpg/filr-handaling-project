 STORE MANAGEMENT SYSTEM

  customer(cid,cname,cadd,cmob,DOB)
  product(pid,pname,price)
  order(oid,cid,pid,qty)

  1. Add Customer
  2. View all Customer
  3. Delete a Customer
  4. Add Product
  5. View all Product
  6. Update product
  7. Place an Order
  8. View all Orders
  9. View all Orders by CID
  0. Exit
  
"""

# IMPORTANT PACKAGES
import pickle
import os

# A METHOD TO ADD A CUSTOMER DETAIL
def addCustomer():
    file = open('customer.bin','ab')
    cid = input("\n\tEnter a Customer ID: ")
    cname = input("\tEnter a Customer Name: ")
    cadd = input("\tEnter a Customer Address: ")
    cmob = input("\tEnter a Customer Mobile No.: ")
    DOB = input("\tEnter a Customer DOB: ")
    pickle.dump(cid,file)
    pickle.dump(cname,file)
    pickle.dump(cadd,file)
    pickle.dump(cmob,file)
    pickle.dump(DOB,file)
    print("\n\tCustomer Data add Successfully...")
    file.close()
    input("\n\tPress Enter to Continue...")

# METHOD TO VIEW ALL CUSTOMER
def viewAllCustomer():
    file = open('customer.bin','rb')
    try:
        print("\n\tCID\tCNAME\tCADD\tCMOB\tDOB")
        while True:
            for i in range(5):
                data = pickle.load(file)
                print("\t",data,end="")
            print()
    except:
        print("\n\t Here is your all Customer Data!")
    file.close()
    input("\n\tPress Enter to Continue...")

def deleteCustomer():
    file1 = open('customer.bin','rb')
    file2 = open('temp.bin','ab')
    cid = input("\tEnter Customer ID to Delete: ")
    flag = 0
    try:
        while True:
            data = pickle.load(file1)
            if(data == cid):
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                flag = 1
            else:
                pickle.dump(data,file2)        
    except:
        if(flag == 0):
            print("\tCustomer Not Found!")
        else:
            print("\tCustomer Detail Deleted Successfully!")
    file1.close()
    file2.close()
    os.remove('customer.bin')
    os.rename('temp.bin','customer.bin')
    input("\n\tPress Enter to Continue...")

# METHOD TO ADD A PRODUCT DETAILS
def addProduct():
    file = open('product.bin','ab')
    pid = input("\tEnter a Product ID: ")
    pname = input("\tEnter a Product Name: ")
    price = input("\tEnter a Price: ")
    pickle.dump(pid,file)
    pickle.dump(pname,file)
    pickle.dump(price,file)
    file.close()
    print("\tProduct Details Add Sucessfully...")
    input("\n\tPress Enter to Continue...")

# METHOD TO VIEW ALL PRODUCT DETAIL
def viewAllProduct():
    file = open('product.bin','rb')
    try:
        while True:
            print("\tProduct ID: ",pickle.load(file))
            print("\tProduct Name: ",pickle.load(file))
            print("\tProduct Price: ",pickle.load(file))
            print("\n\t**************************")
    except:
        print("\n\tThis is the Product Detail")
        file.close()
        input("\n\tPress Enter to Continue...")

# MEHTOD TO UPDATE A PRODUCT DETAILS
def updateProduct():
    file1 = open('product.bin','rb')
    file2 = open('temp.bin','ab')
    pid = input("\tEnter Product ID to Update Price: ")
    flag = 0
    try:
        while True:
            data = pickle.load(file1)
            if(data == pid):
                pickle.dump(data,file2)
                name = pickle.load(file1)
                pickle.dump(name,file2)
                print("\tOld Price: ",pickle.load(file1))
                price = input("\tEnter New Price: ")
                pickle.dump(price,file2)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        if(flag == 1):
            print("\tUpdated Successfully....")
        else:
            print("\t Product ID Not Found!")

    file1.close()
    file2.close()
    os.remove('product.bin')
    os.rename('temp.bin','product.bin')
    input("\n\tPress Enter to Continue...")

# METHOD TO PLACE AN ORDER
def getProduct(id_):
    pro =[]
    file = open('product.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if(data == id_):
                pro.append(data)
                pro.append(pickle.load(file))
                pro.append(pickle.load(file))
            
    except:
        pass
    file.close()
    return pro

# METHOD TO PLACE AN ORDER
def getCustomer(id_):
    cus =[]
    file = open('customer.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if(data == id_):
                cus.append(data)
                cus.append(pickle.load(file))
                cus.append(pickle.load(file))
                cus.append(pickle.load(file))
            
    except:
        pass
    file.close()
    return cus

def placeAnOrder():
    cid = input("\tEnter CID to Place Order: ")
    cus = getCustomer(cid)
    if len(cus)>0:
        print("\tCustomer Name: ", cus[1])
        print("\tCustomer Address: ", cus[2])
        pid = input("\tEnter PID to Place Order: ")
        pro = getProduct(pid)
        if len(pro)>0:
            print("\tProduct Name: ", pro[1])
            print("\tProduct Price: ", pro[2])
            qty = input("\n\tEnter Quantity: ")
            print("\tTotal Bill:",int(pro[2])*int(qty))
            print("\n\tOrder Placed Successfully!")
            file = open('order.bin','ab')
            pickle.dump(cid,file)
            pickle.dump(pid,file)
            pickle.dump(qty,file)
            file.close()
        else:
            print("\n\tProduct Not found!")
    else:
        print("\n\t Customer Not Found!")
    input("\n\tPress Enter to Continue...")
    
def viewAllOrders():
    file = open('order.bin','rb')
    oid = 1001
    try:
        while True:
            cus = getCustomer(pickle.load(file))
            pro = getProduct(pickle.load(file))
            qty = int(pickle.load(file))
            print("\tOrder ID :",oid)
            print("\tCustomer Name :",cus[1])
            print("\tCustomer Address :",cus[2])
            print("\tProduct Name :",pro[1])
            print("\tProduct Price :",pro[2])
            print("\tQuantity :",qty)
            print("\n\tTotal Bill :",int(pro[2])*qty,'/-')
            print("\t-----------------------\n")
            oid+=1
    except:
        print("\n\tHere is all the details")
    file.close()
    input("\tPress Enter To Continue...")

# A METHOD TO VIEW ORDERS BY CID
def viewOrderByCID():
    file = open('order.bin','rb')
    cid = input("\n\tEnter CID To Display Orders : ")
    try:
        while True:
            cus = getCustomer(pickle.load(file))
            pro = getProduct(pickle.load(file))
            qty = int(pickle.load(file))
            if cus[0]==cid:
                print("\tCustomer Name :",cus[1])
                print("\tCustomer Address :",cus[2])
                print("\tProduct Name :",pro[1])
                print("\tProduct Price :",pro[2])
                print("\tQuantity :",qty)
                print("\n\tTotal Bill :",int(pro[2])*qty,'/-')
                print("\t-----------------------\n")
    except:
        print("\n\tHere is all the details")
    file.close()
    input("\tPress Enter To Continue...")


# DASHBOARD/HOME PAGE
print("\t\t STORE MANAGEMENT SYSTEM")

while True:
    print('''
          1. Add Customer
          2. View all Customer
          3. Delete a Customer
          4. Add Product
          5. View all Product
          6. Update product
          7. Place an Order
          8. View all Orders
          9. View all Orders by CID
          0. Exit
    ''',end="")
    ch = int(input("Enter Your Choice: "))

    if(ch == 0):
        print("\n\t Bye Bye Admin. See you Soon!")
        break

    elif(ch == 1):
        addCustomer()

    elif(ch == 2):
        viewAllCustomer()

    elif(ch == 3):
        deleteCustomer()

    elif(ch == 4):
        addProduct()

    elif(ch == 5):
        viewAllProduct()

    elif(ch == 6):
        updateProduct()

    elif(ch == 7):
        placeAnOrder()

    elif(ch == 8):
        viewAllOrders()

    elif(ch == 9):
        viewOrderByCID()
    else:
        print("\n\tWrong N