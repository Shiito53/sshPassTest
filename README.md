# sshPassTest
Welcome to SSH CEW (SSH cracking easy way) a personnal project without any abambition other than learning python and having fun.
The role of this code is to find a way to enter in a SSH connection, using a dictionnary of usernames and password ( password are the only one working for the moment), it is very slow due to the time between connection and deconnection. With this, you can see if the device you are trying to connect to is using default password and username ( such as root - root but don't try this, this is SSH, nobody connect on root by SSH right ?)

For the moment this is really simple to use. Just download the project with (or without) the list of passwords, and launch the project with python and a list of password to test (in parameter, see example bellow).
The format of the file is "pass1 pass2 pass3" using space as a separator between passwords.
You can use your own password list if you want, just change the argument when you call the python code and be sure that it respect the format.

Example of execution :
  python3 sshTest.py your_list.txt

Enjoy your stay ! 
(Probably more coming up as long as the project interest me !)
