# Project Set-Up In Windows Environmentr 
If you have tried setting up the project in windows you many ran into problems including 
```
service_1  | /usr/bin/env: ‘bash\r’: No such file or directory
service_1  | 2022/03/30 16:20:21 Command exited with error: exit status 127
```
basically tou have to clone the project in linux file system , full process explained in details 
# Pre-requisite
*We assume you have Windows 10
*[Docker](https://docs.docker.com/get-docker/) is up and running properly in your system

# Solution 
 -search for Turn Windows features on or off 
    -navigate to buttom and click the checkbox named "Windows Subsystem For Linux"
 -Now you have to install any linux distro in your windows system 
   - Go to microsorft stores and install any linux distro(Ubuntu prefered)
   - launch ubuntu
  - if you do ls-la in ubuntu you can see the linux files are there
     -you have to access all the windows files from ubuntu console
     -use this  to display all the drives avilable in windows , it will mount the storage 
     ``
     cd /mnt/
     ``
     - naigate to your desired location e.g 
     ```
     cd /mnt/User/your_pc_name/Desktop/folder
     ```
 - Clone the repository using command -- git clone [repo-link](https://github.com/centerofci/mathesar)
    -Here you can ran into some problem regarding permission(chmod) in some .git-config files .
    -It may occure as ubuntu is not seted up properly in your windows machine just a quick restart can fix this issue .
 - Copy the `.env.example` file to `.env` like so:
```
cp .env.example .env
```

- From the repository's root directory, run:
```
docker-compose up
```

If it's your first time running the application, you'll also need to run database migrations and install Mathesar types and functions:
```
docker exec mathesar_service sh -c "python manage.py migrate && python install.py"
```
 You should now have a web server and database server running. Opening `http://localhost:8000` in your browser will open the application. For sample table data, you can create a new table in the UI using the `patents.csv` file found in `/mathesar/tests/data`. 

It is recommended that you keep the Docker containers running while you make changes to the code. Any change to the code made locally will sync to the container and the version deployed at `http://localhost:8000` will always be the latest local version of the code.
