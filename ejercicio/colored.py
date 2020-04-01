from graphviz import Graph

def adjacenters(n, g, colors, c):
   
    for i in xrange(n):
        if g[n][i] and c == colors[i]: return False
    return True

def GiveColor(g, colors, memo_colors, n):

	if colors+1 == n :
		return True

	for i in xrange(0, colors):
		if adjacenters(n, g, memo_colors, i):
			memo_colors[n] = i
			GiveColor(g,colors,memo_colors,n+1)


colorsRGB = ["green","red","blue","black"]
colors = 3

          #0 1 2 3 4 5
graph_ = [[0,1,0,0,1,0],#0
		  [1,0,1,0,1,0],#1
		  [0,1,0,1,0,0],#2
		  [0,0,1,0,1,1],#3
		  [1,1,0,1,0,0],#4
		  [0,0,0,1,0,0]]#5

m = len(graph_)

colors_m = [0] * m

nodo = 0

GiveColor(graph_, colors, colors_m, 0)
print (colors_m)

dot = Graph(comment='Coloring ..')

for i in colors_m:

	coloring = str(nodo) + '[color="' + colorsRGB[i]+'"]'
   	print coloring
   	nodo=nodo+1
   	dot.node(coloring)
dot.edges(['01','04','12','14','23','34','35'])   	
print(dot.source)
dot.format='svg'
dot.render()