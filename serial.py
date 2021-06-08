"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self,start=0):
        "Initializing and making new generator"
        self.start= self.next=start
    
    def __repr__(self):
        return f"Serial Generator start at {self.start} and next is {self.next+1}"

    def generate(self):
        self.next+=1
        return self.next-1
    
    def reset(self):
        self.start=self.next
    
