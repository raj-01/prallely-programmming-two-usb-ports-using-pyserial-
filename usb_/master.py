import os
from multiprocessing import Pool 


#number of usb a user want to connect having address /dev/ttyUSB* format only 
num_usb = 2 ; 

processes = ['run1.py' , 'run2.py']  


def run_processes(process):
    os.system('python {}'.format(process));
   

# aloting num_usb labours for running num_usb py scripts 
pool = Pool(processes = num_usb);
pool.map(run_processes , processes);















