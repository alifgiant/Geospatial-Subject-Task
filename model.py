from sympy import Point, Polygon
import math


def comb_and_comp(lst, size):
	"""
	get combination and its complementer
	function from https://stackoverflow.com/questions/28992042/algorithm-to-return-all-combinations-of-k-out-of-n-as-well-as-corresponding-comp
	"""
	# no combinations
	if len(lst) < size:
		return
	# trivial 'empty' combination
	if size == 0 or lst == []:
		yield [], lst
	else:
		first, rest = lst[0], lst[1:]
		# combinations that contain the first element
		for in_, out in comb_and_comp(rest, size - 1):
			yield [first] + in_, out
		
		# combinations that do not contain the first element
		for in_, out in comb_and_comp(rest, size):
			yield in_, [first] + out

class Voronoi(object):
	def __init__(self, name, points):        
		self.name = name
		# print('point', len(points), points)
		self.bound = Polygon(*points)
		self.center = self.bound.centroid
	
	def __str__(self):
		return str(self.bound)
	
class RTree(object):
	def __init__(self, max_content_size = 4, content = list(), is_leaf = True):
		self.max_content_size = max_content_size
		self.all_content = list()
		self.childs = list()
		self.is_leaf = is_leaf
		self.parent = None
		self.bound = None

		for voronoi in content:
			self.all_content.append(voronoi)                        
			self.insert(voronoi)

		for voronoi in content:
			if isinstance(voronoi, RTree):
				self.is_leaf = False
				break

	def inspectTree(self):
		currentLevel = []
		nextLevel =[]
		print(len(self.childs))
		for n in self.childs:
			#  print(n)
			currentLevel.append(n)
		while len(currentLevel) != 0:
			x = currentLevel.pop(0)
			if isinstance(x,RTree):
				#  print("Subtree")
				#  print(x)
				mixed = False
				type = isinstance(x.childs[0],RTree)
				#  print(type)
				for n in x.childs:
					if(isinstance(n,RTree) != type and mixed == False):
						mixed = True
					nextLevel.append(n)
				#  print("Mixed: " + str(mixed))
			#  else:
				#  print("Region")
				#  print(x.name)
			if(len(currentLevel) == 0):
				#  print("Next Level/Depth")
				currentLevel = nextLevel
				nextLevel = []

	def seq_search(self, query_point, include_on_edge, voronoi_list):
		for voronoi in voronoi_list:
			# print(voronoi.name)
			if voronoi.bound.encloses_point(query_point) or (include_on_edge and voronoi.bound.intersection(query_point)):
				return "Region Found :"+voronoi.name
		return 'Region Not Found'
	def search(self, query_point, include_on_edge = False):
		stack = []
		for n in self.childs:
			print(n)
			stack.append((n, 0))
		possible = []
		while len(stack) != 0:
			checked, depth = stack.pop(0)
			if(checked.bound.encloses_point(query_point) or (include_on_edge and checked.bound.intersection(query_point))):
				if isinstance(checked, RTree) :
				  for n in checked.childs:
					  # if isinstance(n,Voronoi):
					  # print(n.name)
					  stack.insert(0, (n, depth + 1))
				else:
					# print(checked)
					possible.append((checked.name, depth))
		#     for s in stack:
		#         print(s)
		#     print("###########")
		# for v in possible:
		#     print(v)
		return possible

	def insert(self, new_inserted):
		# find node
		node = RTree.choose_leaf(self, new_inserted)

		if len(node.childs) + 1 > node.max_content_size:
			# #try reinsert 
			# if(node.isReinsert == False):
			#     node.isReinsert = True
			#     # Reinsert algorithm
			#     objects = node.childs + [new_inserted]
			#     idx = []
			#     dist = []
			#     for i in range(len(objects)):
			#         # if isinstance(objects[i],RTree):
			#             # print("Rtreetree masuk ke voronoi")
			#         deltaX = objects[i].center[0] - node.bound.centroid[0]
			#         deltaY = objects[i].center[1] - node.bound.centroid[1]
			#         # Euclidean distance of entry polygon and the node polygon
			#         d = math.sqrt(deltaX * deltaX + deltaY * deltaY)
			#         dist.append(d)
			#         idx.append(i)

			#     # sort descending, insertion sort, the object is represented by their index in dist array, dist and objects array is ordered similiarly
			#     for j in range(len(objects)):
			#         idxBig = 0
			#         for k in range(j + 1, len(objects)):
			#             if (dist[idxBig] < dist[k]):
			#                 idxBig = k
			#         t = idx[idxBig]
			#         idx[idxBig] = idx[j]
			#         idx[j] = t
			#     selected_to_remove = objects[0]
			#     node.childs = objects
			#     node.childs.remove(selected_to_remove)
			#     node.rebound_border()
			#     root_node = node

			#     while root_node.parent is not None:
			#         root_node = root_node.parent

			#     selected_reinsert_node = RTree.choose_leaf(root_node, selected_to_remove)
			#     selected_reinsert_node.insert(selected_to_remove)
			# else:
			#     # Splitting
			#     # print("Split")
			#     node.childs = list(node.split(new_inserted))
			#     node.rebound_upward()
			
			#########
			# Splitting
			# print("Split")
			node.childs = list(node.split(new_inserted))
			node.rebound_upward()
		else:
			node.childs.append(new_inserted)
			node.bound = RTree.update_bound(node,new_inserted)

	def rebound_upward(self):
		if self.parent is not None:
			# print 'rebound_upward', self.parent, self.parent.childs
			self.parent.childs.remove(self)
			for child in self.childs:
				self.parent.childs.append(child)            
			if len(self.parent.childs) > self.parent.max_content_size:
				self.parent.childs = list(self.parent.split())
				self.parent.rebound_upward()
	def reset(self):
		currentLevel = []
		nextLevel = []
		#print(len(self.childs))
		for n in self.childs:
			#print(n)
			currentLevel.append(n)
		while len(currentLevel) != 0:
			x = currentLevel.pop(0)
			if isinstance(x, RTree):
				x.isReinsert = False
				for n in x.childs:
					nextLevel.append(n)
			if (len(currentLevel) == 0):
				#print("Next Level/Depth")
				currentLevel = nextLevel
				nextLevel = []

	def split(self,new_inserted):
		# ready the new container
		first_node = None
		second_node = None
		objects = [new_inserted] + self.childs
		bestpairs = (None, None)
		bestArea = 0
		for i in range(len(objects)):
			for j in range(i + 1, len(objects)):
				polygon = RTree.update_bound(objects[i], objects[j])
				area = polygon.area
				if (bestArea == 0 or bestArea < area):
					bestpairs = (objects[i], objects[j])
					bestArea = area
		# entry picking
		###################
		# removing non seed entries
		firstGroup = [bestpairs[0]]
		secondGroup = [bestpairs[1]]
		objects.remove(bestpairs[0])
		objects.remove(bestpairs[1])
		for entry in objects:
			d1 = RTree.update_bound(entry, bestpairs[0]).area
			d2 = RTree.update_bound(entry, bestpairs[1]).area
			if (d1 <= d2):
				firstGroup.append(entry)
			else:
				secondGroup.append(entry)
		first_node = RTree(max_content_size=4, content=firstGroup, is_leaf=self.is_leaf)
		second_node = RTree(max_content_size=4, content=secondGroup, is_leaf=self.is_leaf)
		#
		# # put indexes in new list
		# content_indexes = list(range(len(self.childs)))
		# for max_member_count in range(self.max_content_size):
		#     for first_indexes, second_indexes in comb_and_comp(content_indexes, max_member_count + 1):
		#         new_first = RTree(max_content_size=self.max_content_size,
		#                                content=[self.childs[i] for i in first_indexes])
		#         new_second = RTree(max_content_size=self.max_content_size,
		#                                 content=[self.childs[i] for i in second_indexes])
		#         new_first.rebound_border()
		#         new_second.rebound_border()
		#         if (first_node is None and second_node is None):
		#             first_node = new_first
		#             second_node = new_second
		#
		#
		#     else:
		#             current_best = first_node.bound.area + second_node.bound.area
		#             new_best = new_first.bound.area + new_second.bound.area
		#             if new_best <= current_best:  # ' <= ' take last configuration, cause it divide the node with more member
		#                 first_node = new_first
		#                 second_node = new_second
		#
		# first_node.parent = self
		# second_node.parent = self
		#
		# self.is_leaf = False
		return first_node, second_node

	def rebound_border(self):
		self.bound = None
		for content in self.childs:
			self.bound = RTree.update_bound(self, content)

	@staticmethod
	def count_overlap_area(first, second):
		first_xmin, first_ymin, first_xmax, first_ymax = first.bound.bounds
		second_xmin, second_ymin, second_xmax, second_ymax = second.bound.bounds
		return (max(0, min(first_xmax, second_xmax)) - max(first_xmin, second_xmin)) * \
				(max(0, min(first_ymax, second_ymax)) - max(first_ymin, second_ymin))

	@staticmethod
	def choose_leaf(node, new_inserted):
		if node.is_leaf:
			return node
		else:
			choosed = None
			choosed_expanded_size = 0
			choosed_total_overlap = 0
			for i, child in enumerate(node.childs):
				expanded_size = RTree.update_bound(child, new_inserted).area
				total_overlap = 0
				for j, other_child in enumerate(node.childs[:i] + node.childs[i+1:]):
					overlap = RTree.count_overlap_area(child, other_child)                    
					total_overlap += overlap
				if choosed is None or \
					choosed_total_overlap > total_overlap or \
					(choosed_total_overlap == total_overlap and choosed_expanded_size > expanded_size):
					choosed = child
					choosed_expanded_size = expanded_size
					choosed_total_overlap = total_overlap
			return RTree.choose_leaf(choosed, new_inserted)
	
	@staticmethod
	def update_bound(current, other):
		if current.bound is None:
			return other.bound
		else:
			current_xmin, current_ymin, current_xmax, current_ymax = current.bound.bounds
			other_xmin, other_ymin, other_xmax, other_ymax = other.bound.bounds
			current_xmin = other_xmin if other_xmin < current_xmin else current_xmin
			current_ymin = other_ymin if other_ymin < current_ymin else current_ymin
			current_xmax = other_xmax if other_xmax > current_xmax else current_xmax
			current_ymax = other_ymax if other_ymax > current_ymax else current_ymax
			return Polygon((current_xmin, current_ymin), (current_xmax, current_ymin), (current_xmax, current_ymax), (current_xmin, current_ymax))
