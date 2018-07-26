groceries = {'cereal', 'milk', 'starcrunch', 'beer', 'duck tape', 'lotion', 'milk'}
print (groceries) ## print milk 1 times even if it is duplicate.

if 'milk' in groceries:
    print ('you already have milk hoss!!!')

else:
    print ('Oh yea you need milk')


############ this is set fuction #######

class_mate = {'Tony': ' cool but smell','Emma': ' sits behind me','Lucy': ' ask too many questions'}
            #  key         value       (Tony is key and cool and smell is value)

print(class_mate) ## this case it print out all description above
print(class_mate['Tony']) ### it print out only Tony
print(class_mate['Emma']) ### you can do each like this but it takes long line

for k, v in class_mate.items(): ### k is key and v is value
    print (k + v) ### ???? not sure why it show up Lucy first ####


