decimalnumber=int(input("enter a number:: "))

hexdigit="0123456789ABCDEF"
hexdec=''
orgdec=decimalnumber

if decimalnumber==0:
    hexdec=0

while decimalnumber>0:
    rem=decimalnumber%16
    hexdec=hexdigit[rem]+hexdec
    decimalnumber=decimalnumber//16

print(hexdec)
     
