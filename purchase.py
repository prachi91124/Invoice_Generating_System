"""
module name: purchase
function name: purchase
overview of this function:
1) Customer interaction for what and how much the want buy.
2) check the user interaction valid or not with exception handelling.
3) calculating the customer purchase product with discount(if discountable)
4) show the last update of the product
5) write the invoice for customer with unique naming
"""


def purchase(List):
    L = List  # assign list with variable name 'L'.
    a_name = input("Please enter your name: ")
    print("\nHello " + a_name + "! Welcome to our General Store.\nLook at above and select product as your choice.")
    q = {}  # assign empty dictionary with variable name 'q'.
    flag = "Y"
    while flag.upper() == "Y":  # check and go if flag is 'Y' or 'y'.
        product = input("\nWhat product do you want to buy? ")
        product_name = product.upper()  # change the string value in the upper case.

        if product_name == L[0][0].upper() \
                or product_name == L[1][0].upper() \
                or product_name == L[2][0].upper() \
                or product_name == L[3][0].upper() \
                or product_name == L[4][0].upper():  # check the user entered product name with stock of store

                
                
            
            p = True
            while p == True:
                try:
                    p_quantity = int(input("How many " + product + " do you want to buy: "))
                    p = False
                except:  # executes, if customer entered unexpected value.
                    print("\t\tError!!!\nPlease enter integer value!! ")
            if product_name == L[0][0].upper() and p_quantity <= int(L[0][2]):
                q[product_name] = p_quantity
            elif product_name == L[1][0].upper() and p_quantity <= int(L[1][2]):
                q[product_name] = p_quantity
            elif product_name == L[2][0].upper() and p_quantity <= int(L[2][2]):
                q[product_name] = p_quantity
            elif product_name == L[3][0].upper() and p_quantity <= int(L[3][2]):
                q[product_name] = p_quantity
            elif product_name == L[4][0].upper() and p_quantity <= int(L[4][2]):
                q[product_name] = p_quantity
            else:
                print(
                    "\nSorry!! " + a_name + "!, " + product + " is out of stock.\nWe will add stock of " + product + " later. \nLets hope, you will get this product after next shopping.\n")

            flag = (input(a_name + " do you want buy more products?(Y/N)"))
        else:
            print("sorry!! " + product + " is not available in our store.")
            print("\nChoose from following products please!")
            print("--------------------------------------------")
            print("PRODUCT\t\tPRICE\t\tQUANTITY")
            print("--------------------------------------------")
            for i in range(len(L)):
                print(L[i][0], "\t\t", L[i][1], "\t\t", L[i][2])  # print, last updated product name, quantity and price.
            print("--------------------------------------------")

    print("\nYou Choosed Items and it's Quantity respectively:\n", q, "\n")
    '''
        In the following operation:
        1) change every string value in the upper case latter.
        2) check what is the product entered by customer.
        3) executes respective condition if product is phone or laptop or hdd entered by customer.
    '''
    f_amount = 0  # final amount
    for keys in q.keys():
        if keys == L[0][0].upper():  # executes this operation if product is chips entered by customer.
            c_price = int(L[0][1])
            c_num = int(q[keys])
            c_amount = (c_price * c_num)
            f_amount += (c_price * c_num)
            print("\nTotal cost for chips: ", c_amount)
        elif keys == L[1][0].upper():  # executes this operation if product is water bottle entered by customer.
            w_price = int(L[1][1])
            w_num = int(q[keys])
            w_amount = (w_price * w_num)
            f_amount += (w_price * w_num)
            print("Total cost for water bottle: ", w_amount)
        elif keys == L[2][0].upper():  # executes this operation if product is milk entered by customer.
            m_price = int(L[2][1])
            m_num = int(q[keys])
            m_amount = (m_price * m_num)
            f_amount += (m_price * m_num)
            print("Total cost for milk: ", m_amount)
        elif keys == L[3][0].upper():  # executes this operation if product is curd entered by customer.
            cu_price = int(L[3][1])
            cu_num = int(q[keys])
            cu_amount = (cu_price * cu_num)
            f_amount += (cu_price * cu_num)
            print("Total cost for curd: ", cu_amount)
        else:  # executes this operation if product is bread entered by customer.
            b_price = int(L[4][1])
            b_num = int(q[keys])
            b_amount = (b_price * b_num)
            f_amount += (b_price * b_num)
            print("Total cost for bread: ", b_amount)

    
    total = float(f_amount)
    print("Your payable amount is: ", total)

    '''
        In the following operation:
        1) write a each unique involve name which includes current date and time with customer name as well.
        2) write a purchase product name and details in file (invoice).
        3) write a discounted amount and final payable amount in file (invoice).
    '''

    import datetime  # import system date and time for create a unique invoive name.
    dt = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day) + "-" + str(datetime.datetime.now().hour) + "-" + str(
        datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second)
    invoice = str(dt)  # unique invoice
    t = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day)  # date
    d = str(t)  # date
    u = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(
        datetime.datetime.now().second)  # time
    e = str(u)  # time

    file = open(invoice + " (" + a_name + ").txt", "w")  # generate a unique invoive name and open it in write mode.
    file.write("=============================================================")
    file.write("\nGENERAL STORE\t\t\t\tINVOICE")
    file.write("\n\nInvoice: " + invoice + "\t\tDate: " + d + "\n\t\t\t\t\tTime: " + e + "")
    file.write("\nName of Customer: " + str(a_name) + "")
    file.write("\n=============================================================")
    file.write("\nPARTICULAR\tQUANTITY\tUNIT PRICE\tTOTAL")
    file.write("\n-------------------------------------------------------------")

    for keys in q.keys():  # In this loop, write in a file only those product which is purchase by user.
        if keys == "CHIPS":
            file.write(
                str("\n" + str(keys) + " \t\t " + str(q['CHIPS']) + " \t\t " + str(L[0][1]) + " \t\t " + str(c_amount)))
        elif keys == "WATER BOTTLE":
            file.write(str0(
                "\n" + str(keys) + " \t\t " + str(q['WATER BOTTLE']) + " \t\t " + str(L[1][1]) + " \t\t " + str(w_amount)))
        elif keys == "MILK":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['MILK']) + " \t\t " + str(L[2][1]) + " \t\t " + str(m_amount)))
        elif keys == "CURD":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['CURD']) + " \t\t " + str(L[3][1]) + " \t\t " + str(cu_amount)))
        else:
            file.write(
                str("\n" + str(keys) + " \t\t " + str(q['BREAD']) + " \t\t " + str(L[4][1]) + " \t\t " + str(b_amount)))

    file.write("\n-------------------------------------------------------------")
    file.write("\n\t\t\t Your payable amount is: " + str(total))
    file.write("\n-------------------------------------------------------------")
    file.write("\n\n\tThank You " + a_name + " for your shopping.\n\t\tSee you again!")
    file.write("\n=============================================================")
    file.close()
    return q