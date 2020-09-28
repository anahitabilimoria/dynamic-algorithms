from collections import defaultdict, deque
import os
import json

def dijkstra(graph, initial):
	visited = {initial: 0}
	path = {}

	nodes = set(graph['nodes'])

	while nodes:
		initialNode = None
		for node in nodes:
			if node in visited:
				if initialNode == None:
					initialNode = node
				elif visited[node] < visited[initialNode]:
					initialNode = node
		if initialNode == None:
			break

		nodes.remove(initialNode)
		existingWeight = visited[initialNode]

		print(graph['edges'], initialNode)
		for edge in graph['edges'][initialNode]:
			try:
				weight = existingWeight + graph['distances'][(initialNode, edge)]
				print(weight)          
			except:
				continue
			if edge not in visited or weight < visited[edge]:
				visited[edge] = weight
				path[edge] = initialNode

	return visited, path

def shortestPath(graphData, origin, destination):
		graph = {
			'nodes' : set(),
			'edges' : defaultdict(list),
			'distances' : {}
		}

		for node in graphData['nodes']:
			graph['nodes'].add(node)

		for edge in graphData['edges']:
			graph['edges'][edge[0]] = [ item for item in edge[1:] ] 
		
		for distance in graphData['distances']:
			graph['distances'][(distance[0], distance[1])] = int(distance[2])

		print(graph['distances'])
		visited, paths = dijkstra(graph, origin)
		finalList = deque()
		destinationNew = paths[destination]

		while destinationNew != origin:
			finalList.appendleft(destinationNew)
			destinationNew = paths[destinationNew]

		finalList.appendleft(origin)
		finalList.append(destination)

		return visited[destination], list(finalList)

if __name__ == '__main__':
	with open(os.path.dirname(os.path.abspath(__file__)) + '/dijkstra.json') as f:
		data = json.load(f)

	result = shortestPath(data, data['fromNode'], data['toNode'])
	print(result)
