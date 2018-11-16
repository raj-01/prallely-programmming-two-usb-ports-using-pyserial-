import serial 
import os 


store_port = os.popen( " ls /dev/ttyUSB* " ).read() ;        # in /dev/  directory reading all files name start with ttyUSB 
store_port = store_port.split() ; 		# space seprated string elements ( usb file name )  to array of usb name


is_connection_established_run1 = False ; 
is_connection_established_run2 = False ; 

for itr in range( len(store_port) ) :  
	
	try:	
		pulse_1 = serial.Serial(store_port[itr], 115200 ,timeout = 11) ; 
		if pulse_1.isOpen() : 
			is_connection_established_run1 = True ; 			
			run1_port_addr = store_port[itr];
			del store_port[itr] ;	  # deleting the usb file name to which connection is established 		
			break ; 		# break from the loop and estab. connection for other usb in nxt loop 
	
	except serial.SerialException as ex : 
		print( store_port[itr],"port is unavailable ") ; 		


for itr in range( len(store_port) ) :  
	try:	
		pulse_2 = serial.Serial(store_port[itr], 115200 ,timeout = 11) ; 
		if pulse_2.isOpen() : 
			is_connection_established_run2 = True ; 			
			run2_port_addr = store_port[itr];
			del store_port[itr] ;			
			break ; 
	except serial.SerialException as ex : 
		print( store_port[itr],"port is unavailable ") ; 		










