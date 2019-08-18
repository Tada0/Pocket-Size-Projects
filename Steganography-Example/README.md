#Steganography Example

####Usage: 
```
python3 usage: app.py [-h] (-e Image_Path, Message_File_Path, Key | -d Image_Path, Key)
```

####eg. Usage: 
```
python3 app.py -e cat.jpg msg.txt 34n5689bv498
```

Will encrypt the message in msg.txt file into cat.jpg with key 34n5689bv498

```
python3 app.py -d cat.jpg 34n5689bv498
```

Will decrypt the message from cat.jpg with key 34n5689bv498
