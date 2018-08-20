#array 의 내용을 file에 쓰거나 읽기
import array
import binascii

arr = array.array('i',range(5))
print (arr)

f = open("test.txt",'w+b')
arr.tofile(f)
f.flush()  # array 내용 (buffer) 에 있는 내용을 file 에 밀어 넣겠다는 의미

with open("test.txt","rb") as f1:
    data  = f1.read()
    print(binascii.hexlify(data))  # 해당 file 에 binary 형태로 저장된 상태를 확인하기 위함.

    f1.seek(0)
    arr2 = array.array('i')
    arr2.fromfile(f1,len(arr))
    print(arr2)

#tofile(파일 객체): 파일 객체에 쓰이는 함수