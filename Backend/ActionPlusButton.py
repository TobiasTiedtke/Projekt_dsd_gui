import os

#TODO: Change raw_input to actual input-windows
x = raw_input("Title of the Action-element: ")
y = raw_input("Title of the class: ")
#writes a file with a specific name and the structure needed for action-elements. 
f = file(str(x) + ".py", 'w')
f.write("from dynamic_stack_decider.abstract_action_element import AbstractActionElement\n")
f.write("\n")
f.write("class " + str(y) + "(AbstractActionElement):\n")
f.write("    def __init__(self, blackboard, dsd, parameters=None):\n")
f.write("        super("+y+", self).__init__(blackboard, dsd, parameters)\n")
f.write("\n")
f.write("#TODO: write your own code here.\n")
f.write("\n")
f.write("    def perform(self, reevaluate=False):\n")
f.write("\n")
f.write("#TODO: write your own code here.\n")
f.write("\n")

