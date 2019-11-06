import os

def DecisionPlusButton():
	#TODO: Change raw_input to actual input-windows
	#TODO: Change Path to a specified path from user
	Path = "/informatik2/students/home/6kornell/Schreibtisch/Projekt_dsd_gui/src"
	FileName = raw_input("Title of the Action-element: ")
	y = raw_input("Title of the class: ")
	completeName = os.path.join(Path, FileName + ".py") 

	#writes a file with a specific name and the structure needed for action-elements. 
	f = open(completeName, 'w')
	f.write("from dynamic_stack_decider.abstract_decision_element import AbstractDecisionElement\n")
	f.write("\n")
	f.write("class " + str(y) + "(AbstractDecisionElement):\n")
	f.write("    def __init__(self, blackboard, dsd, parameters=None):\n")
	f.write("        super("+ str(y) +", self).__init__(blackboard, dsd, parameters)\n")
	f.write("\n")
	f.write("#TODO: write your own code here.\n")
	f.write("\n")
	f.write("    def perform(self, reevaluate=False):\n")
	f.write("\n")
	f.write("#TODO: write your own code here.\n")
	f.write("\n")
	f.write("    def get_reevaluate(self):\n")
	f.write("        return True\n")
	f.write("\n")
	f.write("\n")

DecisionPlusButton()

