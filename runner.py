# This is the runner file. You can run this file in the Python IDLE to test your programs. If you'd like to only test one of the two questions at a time, just comment out the line that runs that program. For example, if you only wanted to test Q1, you'd place a comment symbol (#) in front of line 14. If you only wanted to test Q2, you'd put a comment symbol (#) in front of line 11.
# Other than that, you do not need to edit this file in any way.

import q1
import q2

def testQ1():
    balances = { 1000, 600, 25, 8,  }
    for balance in balances:
        print('\tRunning with a balance of $' + str(balance) + ', your program returned: $' + str(q1.computeMinimumPayment( balance )))

print('Q1:')
testQ1()
    
print('Q2:')
q2.playGame()
