class MyTree:
	
	def __init__(self):
		self.elements = []
		self.count = 0
	
	def length(self):
		return self.count
	
	def siftUp(self, ndx):
		if ndx > 0:
			if ndx % 2 != 0:
				parent = ndx // 2
			else:
				parent = ndx // 2 - 1
			if self.elements[ndx] > self.elements[parent]:
				#tmp = self.elements[ndx]
				#self.elements[ndx] = self.elements[parent]
				#self.elements[parent] = tmp
				
				self. elements[ndx], self.elements[parent] = \
				self.elements[parent], self.elements[ndx]
				
				self.siftUp(parent)

	def insert (self, data):
		self.elements.append(data)
		self.count += 1
		self.siftUp(self.count - 1)
	
	def max_elem(self, ind_1, ind_2):
		if ind_1 < self.count and ind_2 < self.count:
			if self.elements[ind_1] >= self.elements[ind_2]:
				return ind_1
			return ind_2
			
		elif ind_1 < self.count:
			return ind_1
			
		elif ind_2 < self.count:
			return ind_2
			
		elif ind_1 >= self.count and ind_2 >= self.count:
			return self.count

	def siftDown(self, ndx):
		left = 2 * ndx + 1
		right = 2 * ndx + 2
		largest = ndx
		ind_max = self.max_elem(left, right)
		if ind_max != self.count:
			if self.elements[ind_max] >= self.elements[largest]:
				largest = ind_max
				
		if largest != ndx:
			self.elements[ndx], self.elements[largest] = \
			self.elements[largest], self.elements[ndx]
			self.siftDown(largest)
	
	def delete (self):
		assert self.count > 0
		value = self.elements[0]
		self.count -= 1
		self.elements[0] = self.elements[self.count]
		self.siftDown(0)
		self.elements.pop()
		return value
   
