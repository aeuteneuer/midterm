#please do not modify this file, it is used for automated testing

import random
import q1
import q2

def testQ1Given():
    assert (q1.computeMinimumPayment(1000) == 21)
    assert (q1.computeMinimumPayment(600) == .021*600)
    assert (q1.computeMinimumPayment(25) == 10)
    assert (q1.computeMinimumPayment(8) == 8)
    
def testQ1NotGiven():
    theMin = random.randint(1,9)
    assert (q1.computeMinimumPayment( theMin ) == theMin)
    theMin = random.randint(12,400)
    assert (q1.computeMinimumPayment( theMin ) == 10)
    theMin = random.randint(500,5000)
    assert (q1.computeMinimumPayment( theMin ) == .021*theMin)

def testQ2Subtract():
    assert( q2.subtractSticks(4) == False)
    assert( q2.subtractSticks(1) == False)
    assert( q2.subtractSticks(2) == False)
    assert( q2.subtractSticks(3) == False)
    assert( q2.subtractSticks(4) == False)
    assert( q2.subtractSticks(1) == False)
    assert( q2.subtractSticks(1) == False)
    assert( q2.subtractSticks(4) == False)
    assert( q2.subtractSticks(4) == True)

def testQ2Computer():
    assert( q2.determineComputerChoice() in {1,2,3,4} )
    assert( q2.determineComputerChoice() in {1,2,3,4} )
    assert( q2.determineComputerChoice() in {1,2,3,4} )
    assert( q2.determineComputerChoice() in {1,2,3,4} )
    assert( q2.determineComputerChoice() in {1,2,3,4} )
    assert( q2.determineComputerChoice() in {1,2,3,4} )