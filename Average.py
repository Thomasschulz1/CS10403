average= 0
total= 0
howManyEntered= 0

howMany= int(input('How many test scores would you like to average?'))
while( howManyEntered < howMany):
    testScore= int(input('enter test score: '))
    total= total + testScore
    howManyEntered = howManyEntered +1

avg= total/ howMany
print( 'The average for the test scores you entered is:' , avg)
print(avg)
    
    
