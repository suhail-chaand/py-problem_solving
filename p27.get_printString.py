#Define a class/function which has at least two methods: 
#getString: to get a string from console input;
#printString: to print the string in upper case.

class Console:
    def getString(self):
        self.string = input('Input a string: ')
    def printString(self):
        print('Output string: ',self.string.upper())

console = Console()
console.getString()
console.printString()