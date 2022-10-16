# Python3 program to add two numbers
 
# Driver Code
if __name__ == "__main__" :
   
  num1 = 15
  num2 = 12
   
  # Adding two numbers
  sum_twoNum = lambda num1, num2 : num1 + num2
   
  # printing values
  print("Sum of {0} and {1} is {2};" .format(num1, num2, sum_twoNum(num1, num2)))
