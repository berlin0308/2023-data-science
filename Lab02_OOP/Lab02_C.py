from typing import Any


class Array:
    """A Array is a self-defined sequential data type which contains a name."""
    
    def __init__(self, name, contents=None): # default: None as an immutable variable
        """Initialize the contents.
        name: string
        contents: initial contents.
        """
        self.name = name

        # if no contents, create a new list for the new Array
        if contents is None:
            self.contents = []
        else:
            self.contents = contents

    def __str__(self):
        """Return a string representaion of this Array.
        """
        t = [ self.name + ' has contents:' ]
        for obj in self.contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def __getitem__(self, index):
        return self.contents[index]

    def __setitem__(self, index, value):
        self.contents[index] = value

    def add_item(self, item):
        """Adds a new item to the contents.
        item: any object to be added
        """
        self.contents.append(item)

def main():

    arr1 = Array('MyFirstArray')

    arr1.add_item('wallet')
    arr1.add_item('car keys')

    print(arr1) 
    # you shouldsee the output: 
    # MyFirstArray has contents:
    #   'wallet'
    #   'car keys'

    # The following 3 statements should work
    # after you finish TODO_C1
    print(arr1[0]) # 'wallet'
    arr1[0] = 'toys'
    print(arr1[0]) # 'toys'

    arr2 = Array('MySecondArray')
    arr1.add_item(arr2)
    print(arr1)

    # If you run this program as is, it seems to work.
    # To see the problem, trying printing arr2.
    print(arr2)

if __name__ == "__main__":
    main()

