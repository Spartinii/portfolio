"""
from asgn01 import pub_table
from Connect import Connect
the_connector_tunnel = Connect("dcris.txt")
rs = pub_table(the_connector_tunnel) 
for r in rs:
    print(r)
    
the_connector_tunnel = Connect("dcris.txt")
rs = pub_table(the_connector_tunnel,member_id= 33) 
print("----------------------------------------Member_id")
for r in rs:
    print(r)



the_connector_tunnel = Connect("dcris.txt")
rs = pub_table(the_connector_tunnel,pub_type_id = "b") 
print("----------------------------------------Pub_type")
for r in rs:
    print(r)
 

the_connector_tunnel = Connect("dcris.txt")
rs = pub_table(the_connector_tunnel,member_id= 33, pub_type_id= "b" ) 
print("----------------------------------------MEMBER & PUB")
for r in rs:
    print(r)
    