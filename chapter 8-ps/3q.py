def printt(n):
   if(n==0):
      return 
   print("*" * n)
   printt(n-1)

printt(3)