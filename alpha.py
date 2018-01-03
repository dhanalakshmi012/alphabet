# alphabet
while True:
   ch=raw_input("enter the char:")
   if(ch=='0'):
      break
   else:
      if(ch>=a and ch<=z) or (ch>=A and ch<=z):
         print("alphabet")
      else:
         print("not an alphabet")
