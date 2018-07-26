##### This is file create and write #####

fw = open('simple.txt', 'w') ### simple.txt file create and 'w' means will write. you can change fw to anything else.
fw.write ('This is python test\n')  # \n means enter
fw.write ('I like python\n')
fw.close() ## close file   # changed fw to file_write it works fine.

##### This is file read and display here #####

fr = open('simple.txt', 'r')
text = fr.read()   ##### read simple.txt file and store "text" variable
print(text)        #### print that text
fr.close()         # close file