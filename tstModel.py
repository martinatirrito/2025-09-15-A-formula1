from model.model import Model

mymdl = Model()
mymdl.buildGraph(2007, 2007)
print(mymdl.getGraphDetails())

print(mymdl.getTop3Archi())
