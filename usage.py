#### Import Module
from simpdb import SimpDB


#### Initialize Database
myDatabase = SimpDB("./myDatabase.sdb")


#### Set Key Values
# Create Username and Password
myDatabase.set("username", "ElliottStorey")
myDatabase.set("password", 314159)

# Update Password
myDatabase.set("password", "Password123!")


#### Read Key Values
username = myDatabase.read("username")
print(username)


#### Delete Key Values
myDatabase.delete("username")
myDatabase.delete("password")
