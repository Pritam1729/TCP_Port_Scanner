TCP Port Scanner

   This is a simple TCP port scanner implemented in Python using the socket, sys, threading, datetime, and os modules.
When the program is run, it first clears the console using the clear() function. Then it prints an ASCII art title for
the scanner using the art module.

The user is then prompted to enter a domain name or IP address to scan. The program attempts to resolve the domain 
name to an IP address using the gethostbyname() function, and exits with an error message if the domain name cannot be 
resolved
The program then presents the user with several options for scanning types - normal ports (1-1024), all ports (1-65535),
or custom range of ports. The user is prompted to enter the desired option, and if they choose the custom range, they are 
prompted to enter the starting and ending port numbers.
 
The get_ports() function generates a list of all ports to scan based on the user's selection.The conn() function is the 
main thread target that performs the port scanning. It creates a socket object for each port and attempts to connect to the 
target host on that port using the connect_ex() method. If the connection is successful, the port is considered open and its 
number is added to the main_array list

The main program creates a list of threads for each port to be scanned and starts them all. Then it waits for all the
threads to complete using the join() method.

Finally, the program prints a list of all open ports and the time taken for the scan to complete.Note that port scanning 
can be illegal or unethical in certain situations, so it should only be performed with permission and within the confines of
the law.
