from crewai.flow.flow import Flow, start, listen
import time


class SimpeFlow(Flow):

    @start()      # This is the entry point of the flow, start is a decorator
    def function1(self):
        print("Step1..")
        time.sleep(3)

    @listen(function1) # This is the second step of the flow, depends on function1,again listen is a decorator
    def function2(self):
        print("Step2..")
        time.sleep(3)

    @listen(function2)
    def function3(self):
        print("Step3..")
        

def main2():
    obj = SimpeFlow()
    obj.kickoff()
