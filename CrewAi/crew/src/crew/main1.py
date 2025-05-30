from crewai.flow.flow import Flow, listen, start, router, 
import random

class RouteFlow(Flow):

    @start()
    def greeting(self):
        print("Assalam-O-alikum!")
        cities = ["karachi", "islambad","lahore"]

        select_city = random.choice(cities)
        self.state['city'] = select_city
        

    @router(greeting)  # listen wont work here, router needed for functions after this to work
    def select_city(self):
        
        
        if self.state['city']=='karachi':
            return 'karachi'
        elif self.state['city']=='islambad':
            return 'islambad'
        else:
            return 'lahore'
        
        
        
    
       
        
    
    @listen('karachi')
    def f1(self):
        print(f"Write some fun fact about {self.state['city']} .")
        return f"Write some fun fact about {self.state['city']} ."
    
    @listen('islambad')
    def f2(self):
        print(f"Write some fun fact about {self.state['city']}.")
        return f"Write some fun fact about {self.state['city']}."
    
    @listen('lahore')
    def f3(self):
        print(f"Write some fun fact about {self.state['city']} .")
        return f"Write some fun fact about {self.state['city']}."
    
    


def kickoff():
    obj = RouteFlow()
    obj.kickoff()

def plot():
    obj = RouteFlow()
    obj.plot()