import matplotlib.pyplot as plt 
  
# x axis values 
#x = [1,2,3] 
# corresponding y axis values 
#y = [2,4,1] 

frb=open("output_RB_search.txt","r")
fs=open("output_splay_search.txt","r")
fv=open("output_veb_search.txt","r")


data=fs.readlines()
x1=[]
y1=[]
base=100
for i in data:
	x1.append(base)
	base+=1000
	y1.append(float(i))
  
plt.plot(x1, y1, label = "Splay Tree") 
  
# line 2 points 
x2 = [] 
y2 = [] 

data=frb.readlines()
base=100
for i in data:
	x2.append(base)
	base+=1000
	y2.append(float(i))

plt.plot(x2, y2, label = "Red Black Tree") 

# line 3 points 
x3 = [] 
y3 = [] 

data=fv.readlines()
base=100
for i in data:
	x3.append(base)
	base+=1000
	y3.append(float(i))

plt.plot(x3, y3, label = "van Emde Boas Tree") 
  
# naming the x axis 
plt.xlabel('No. of elements ( n )') 	
# naming the y axis 
plt.ylabel('Execution time ( in seconds )') 
# giving a title to my graph
plt.title('Searching in RB tree, vEB tree, Splay tree')  
  
# show a legend on the plot 
plt.legend() 
  
# function to show the plot 
plt.show() 

