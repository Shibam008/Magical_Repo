
#* we can use multiple except block

#* if we want to see error type we use Exception class

#* Using particular sub/child exception class is considerd as good practice while using Exception class is not appreciateable all time

#* finally block will execute always

#* try to include all the possible child exception class(ValueError, ZeroDivisionError) and at the last use super class(Exception) if necessary


try :
   num = int(input("Enter an integer : "))
   div = 15/num
   print(div)
except ValueError as e:
   print("Wrong input!", e)
except ZeroDivisionError as e:
   print("Wrong input!", e)
except Exception as e:
   print("Wrong input!", e)
finally:
   print("It will be executed always")