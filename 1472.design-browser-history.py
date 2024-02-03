#
# @lc app=leetcode id=1472 lang=python3
#
# [1472] Design Browser History
#

# @lc code=start
class MyBrowserLinkedList:
    def __init__(self, url: str):
        self.back = None
        self.forward = None
        self.url = url

class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = None
        self.visit(homepage)

    def visit(self, url: str) -> None:
        newNode = MyBrowserLinkedList(url)
        
        if not self.current:
            self.current = newNode
            return
        
        newNode.back = self.current
        self.current.forward = newNode
        self.current = newNode
        return

    def back(self, steps: int) -> str:
        while (steps >= 1):
            steps -= 1
            if self.current.back:
                self.current = self.current.back
        return self.current.url

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.forward:
                self.current = self.current.forward
            else:
                break
        return self.current.url

#Test Commit
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end

