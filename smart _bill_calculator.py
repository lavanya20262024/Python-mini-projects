product_1=input("enter product_1 :")
price_1=float(input("enter product_1 price:"))
product_2=input("enter product_2 :")
price_2=float(input("enter product_2 price:"))
product_3=input("enter product_3 :")
price_3=float(input("enter product_3 price:"))
total=price_1+price_2+price_3
discount_percent=float(input("/n enter discount_percent="))
discount=total*discount_percent/100
after_discount=total-discount
gst_percent=float(input("enter gst_percent="))
gst=after_discount*gst_percent/100
final_amount=after_discount+gst
print("=======================")
print("     SMART BILL")
print("========================")

print(f"product_1:{product_1}")
print(f"price_1 :{price_1}")
print(f"product_2 :{product_2}")
print(f"price_2 :{price_2}")
print(f"product_3 :{product_3}")
print(f"price_3 is{price_3}")
print("====================")
print(f"total ={total}")
print(f"discount ={discount}")
print(f"gst={gst}")
print(f"final_amount ={final_amount}")
print("=====================")
print("THANKYOU")
