# ud036_StarterCode
Unzip the downloaded folder to your local machine

## Getting Started
To run this project you will have installed the following applications as needed:

	A Bash Terminal (Git Bash)
	Vagrant and VirtualBox
	
## Running

Launch the Vagrant VM in the Bash Terminal. Cd into the folder containing the vagrantfile. 

Use the command: vagrant up

This command will make Vagrant download the Linux operating system and install it. It may take a few minutes to install.

Now use the command: vagrant ssh

This command allows you login to the Linux VM. You will now need to cd into the vagrant/catalog directory (which will automatically be synced to /vagrant/catalog within the VM).

Run your application within the VM:
	
	python /vagrant/catalog/application.py

You can now access the application in any browser by visiting: 
	
	http://localhost:8000

Note for development: prior to running the application, the databse and catalog items would first need to be created/polulated with the following commands:

	python /vagrant/catalog/databse_setup.py
	python /vagrant/catalog/lotsofgames.py


## Using the Application
Navigate through the website and browse through your favorite games. If you decide to login through your google account you are able to create and edit new games. 


## Aknowledgements
Credit to Udacity for providing instructions, resources, and starter templates for creating this application. Stackoverflow for help when I ran into trouble. Also a big thank you to the Udacity forum for when things broke and I couldn't find the solution. 
 

