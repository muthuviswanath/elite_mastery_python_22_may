def header_decorator(func):

    def wrapper_function():
        print("==============================================================================")
        func()
        print("==============================================================================")
    return wrapper_function

def receipt_header():
    print("S.No\t\tItem Name\t\tQty\t\tPrice\t\tAmount")

def product_info():
    print("1\t\t|Sprouts\t\t|10\t\t|50.45\t\t|504.5")

def footer_decorator(func):

    def wrapper_function():
        print()
        func()
        print("------------------------------------------------------------------------------")
        
        
    return wrapper_function

def total_cost():
    
    print("Total Amount: \t\t\t\t504.5")

header = header_decorator(receipt_header)
footer = footer_decorator(total_cost)
header()
product_info()
footer()