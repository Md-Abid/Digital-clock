import time

hour=int(input("Enter current hour:\n"))
minute=int(input("Enter current minute:\n"))
second=int(input("Enter current second:\n"))

def display( ):
	print(hour,":",minute,":",second)

def add( ):
	global hour
	global minute
	global second
	
	second+=1
	if second==60:
	 	minute+=1
	 	second=0
	elif minute==60:
	 	hour+=1
	 	minute=0
	elif hour==24:
	 	hour=0
	 	
print("\n")

while True:
	time.sleep(1)
	add( )
	display( )
	