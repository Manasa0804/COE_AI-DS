import streamlit as sl
proj=sl.number_input("enter your project score:",min_value=0)
internal=sl.number_input("enter your internal score:",min_value=0)
external=sl.number_input("enter your external score:",min_value=0)
total=0
if(proj>50 and internal>50 and external>50):
   total=((proj*70)/100) +((internal*10)/100)+((external*20)/100)
   sl.title(f"Total score is : {total}")
else:
   if(proj<=50):
       sl.title(f"failed in project,score is: {proj}")
   if (internal <= 50):
           sl.title(f"failed in internal,score is: {internal}")
   if (external<= 50):
               sl.title(f"failed in external,score is:{external}")

if(total>90):
   sl.title("A grade")
elif(total>80):
   sl.title("B grade")
elif(total>50):
   sl.title("c grade")