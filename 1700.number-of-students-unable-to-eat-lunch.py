#
# @lc app=leetcode id=1700 lang=python3
#
# [1700] Number of Students Unable to Eat Lunch
#

# @lc code=start
class Node:
    def __init__(self, val: int):
        self.val = val
        self.right = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        node = Node(val)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.right = node
            self.tail = node

    def dequeue(self):
        if not self.head:
            return None
        else:
            val = self.head.val
            self.head = self.head.right
        return val

    def getHeadValue(self):
        if self.head:
            return self.head.val
        else:
            return None

    def printQueue(self):
        temp = self.head
        while temp:
            print ("Value - ", temp.val)
            temp = temp.right

    def getCount(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.right
        return count

class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentQueue = Queue()
        for student in students:
            studentQueue.enqueue(student)
        #print("Enqueuing Students")
        #studentQueue.printQueue()

        sandwitchQueue = Queue()
        for sandwiche in sandwiches:
            sandwitchQueue.enqueue(sandwiche)

        #print("Enqueuing Sandwitches")
        #sandwitchQueue.printQueue()
        counter = 0
        while (sandwitchQueue.head):
            student = studentQueue.dequeue()
            sandwitch = sandwitchQueue.getHeadValue()
            #print ("Comparing student ", student, " with sandwitch ", sandwitch)
            if student == sandwitch:
                #print ("Student ", student, " TAKES the sandwitch ", sandwitch, " and left")
                sandwitchQueue.dequeue()
                counter = 0
            else:
                #print ("Student ", student, " LEAVES the sandwitch ", sandwitch, " and joins back in the queue")
                studentQueue.enqueue(student)
                counter += 1
            
            if counter >= studentQueue.getCount():
                break


        #print ("Returning value ==== ", studentQueue.getCount())
        return studentQueue.getCount()
             
# @lc code=end

