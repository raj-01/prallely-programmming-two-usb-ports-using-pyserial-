
import time 
import os 
import serial_port as sp 


if sp.is_connection_established_run2 == False :
	

	print(	'serial connetion for run2 is not established ' ) ;


else  :

	print(	'serial connetion for run2 is established with port :' , sp.run2_port_addr ) ;
	
	f = open("record_run2.txt" , "w") ;
 


	#message = raw_input("Give Message to be sent : ")
	message1 = "s5s123456hmsproj" ;
	message2 = "qfffffffffffffff" ; 
	message3 = "s7s123456hmsproj" ;


 
	print("hi i am run2") ;

	timeout = time.time() + 10 ; 
	temp = sp.pulse_2.read() ;

	#print( temp ) ;
	f.write(temp ) ; 
	while (True) :
 			if time.time() > timeout :
				break ;
	
	
			a = sp.pulse_2.read() ; 
			
        
 			if( a =='2' and temp == '3' ): 
				print("is in loop 3 to 2 of run2 ");
				f.write(message1); 
                		sp.pulse_2.write(message1) ;
				f.write(a);
				print("stop run2") ;
				time.sleep(8.7) ;
				#print("message");
				f.write(message2); 
                		sp.pulse_2.write(message2) ; 
				#print(a) ;
				f.write(a);
				print("restart run2") ;
				time.sleep(8.7) ;
				 #print("message");
				f.write(message3); 
                		sp.pulse_2.write(message3) ; 
				#print(a) ;
				f.write(a);
				print("start run2") ;
				break ;
			elif ( a == '3' and temp == '2' ):
				print("is in loop 2 to 3 of run2 ");
				f.write(message1); 
				sp.pulse_2.write(message1) ;
                		#print(a) ;
				f.write(a);
				print("stop run2") ;
				time.sleep(8.7) ;
				 #print("message");
				f.write(message2); 
                		sp.pulse_2.write(message2) ; 
				#print(a) ;
				f.write(a);
				print("reatart run2");
				time.sleep(8.7) ;
				#print("message");
				f.write(message3); 
                		sp.pulse_2.write(message3) ; 
				#print(a) ;
				f.write(a);			
				print("run run2") ; 			
				break ; 
       
        		else :
	 			f.write(a);
 				#print(a) ;
    			temp = a ;  
       	


	shut_down = sp.pulse_2.close() ;

	if shut_down < 0 : 
		print(' connection of run2 is terminated  ')
	else : 
    		print('connection of run2 is still alive ')






