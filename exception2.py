try:
     txt = open("/home/pi/Documents/textfile.txt", "w")
     txt.write("This is a test. Normal service will shortly resume!")
except IOError:
     print ("Error: unable to write the file. Check permissions")
else:
     print ("Content written to file successfully. Have a nice day.")
     txt.close() 
