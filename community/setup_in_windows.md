# Project Set-Up In Windows Environment
Windows users who want to run the Mathesar Docker development environment in WSL are advised to clone the repository in a Linux filesystem. 
If you have tried running the project in windows you many ran into some issues including this 
```
service_1  | /usr/bin/env: ‘bash\r’: No such file or directory
service_1  | 2022/03/30 16:20:21 Command exited with error: exit status 127
```
The complete guide is given below .
## Pre-requisite
- We assume you have Windows 10 or higher.
- [Docker](https://docs.docker.com/get-docker/) is up and running properly in your system.

# Solution 
 - First search for "Turn Windows features on or off" , navigate to buttom and click the check-box named "Windows Subsystem For Linux".
    
 - Now you have to install any linux distro in your windows system .
  Go to microsorft store and install any linux distro(Ubuntu prefered) and launch .
 - If you do ls -la in ubuntu terminal you can see the linux files structure,
     * so you have to access  window's files from ubuntu console in order to reach your destination folder in windows, use the  command given below to display all the storage drives avilable in windows , it will mount the storage .
     
     ``
     cd /mnt/
     ``
     * navigate to your desired file location e.g 
     ```
     cd /mnt/User/your_pc_name/Desktop/folder
     ```
 - Clone the repository using command
    ``` 
    git clone https://github.com/centerofci/mathesar.git
    ```
    * Here you may run into some problems regarding permissions in some .git-config files. It may occur as Ubuntu is not configured properly in your Windows machine. Restart your machine to fix this issue.
- Note: You have to perform these previous steps for the first time only ! after you have cloned the repo from ubuntu console in linux file sysyem then you can  simple close ubuntu and start working on the project as other django projects in windows.
- Now no Linux/ubuntu console is needed, just open the project in vs-code(or any ide you prefer) and follow along .
 - Copy the `.env.example` file to `.env` like so:
```
cp .env.example .env
```

- From the repository's root directory, run this command (powershell prefered*):
```
docker-compose up
```

If it's your first time running the application, you'll also need to run database migrations and install Mathesar types and functions:
```
docker exec mathesar_service sh -c "python manage.py migrate && python install.py"
```
 You should now have a web server and database server running. Opening `http://localhost:8000` in your browser will open the application. For sample table data, you can create a new table in the UI using the `patents.csv` file found in `/mathesar/tests/data`. 

It is recommended that you keep the Docker containers running while you make changes to the code. Any change to the code made locally will sync to the container and the version deployed at `http://localhost:8000` will always be the latest local version of the code.
### Troubleshooting
 * Running Script in powershell is disabled by default in windows , you have to change permission to run scripts  [Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.2) 
* Please refer to our [Common Issues wiki page](https://wiki.mathesar.org/engineering/common-issues) for instruction on troubleshooting common issues while setting up and running Mathesar.


