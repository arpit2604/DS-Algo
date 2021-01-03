class MinMaxStack:
	def __init__(self):
		self.arr = []
		self.range = []
		
    def peek(self):
        # Write your code here.
        #pass
		return self.arr[len(self.arr)-1]

    def pop(self):
        # Write your code here.
        #pass
		self.range.pop()
		return self.arr.pop()

    def push(self, number):
		MinMax = {'min': number, 'max' : number}
		if len(self.range) >= 1:
			if self.range[len(self.range)-1]['min'] < MinMax['min']:
				MinMax['min'] = self.range[len(self.range)-1]['min']
			if self.range[len(self.range)-1]['max'] > MinMax['max']:
				MinMax['max'] = self.range[len(self.range)-1]['max']
			self.range.append(MinMax)
		else:
			self.range.append(MinMax)
		self.arr.append(number)

    def getMin(self):
		return self.range[len(self.range)-1]['min']

    def getMax(self):
		return self.range[len(self.range)-1]['max']
