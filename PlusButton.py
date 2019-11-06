import os

x = raw_input("Title of the Python-element: ")
y = raw_input("Title of the class: ")
f = file(str(x) + ".py", 'w')
f.write("from dynamic_stack_decider.abstract_action_element import AbstractActionElement\n")
f.write("\n")
f.write("class " + str(y) + "(AbstractActionElement):\n")
f.write("    def __init__(self, blackboard, dsd, parameters=None):\n")
f.write("        super("+y+", self).__init__(blackboard, dsd, parameters)\n")
f.write("\n")
f.write("#write your own code here.\n")
f.write("\n")
f.write("    def perform(self, reevaluate=False):\n")
f.write("\n")
f.write("#write your own code here.\n")
f.write("\n")

