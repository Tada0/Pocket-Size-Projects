Secure Shell Continuous Deployment
==================================

Script for Deploying Projects from Windows to Linux through scp

Does not support passphrase (Leave Empty)


#### Usage: 
```
python sscd [user@host] [path/to/auth_key] 
```

#### eg. Usage: 
```
python sscd pi@192.168.0.130 C:\\Users\\user\\.ssh\\key
```

Uses config.json (same directory as sscd) to declare supported projects
#### eg. config.json file
```
{
  "project_name": {
    "local_dir": "C:\\Users\\user\\Projects\\TestProject\\",
    "remote_dir": "/home/user/Projects/TestProject"
  }
}
```

With that config script will recursively deploy evey changed file from local_dir to remote_dir on file save.

Note that remote_dir must exist on the remote machine 

#TODO

In future, script will support deployment of all files on script start. 