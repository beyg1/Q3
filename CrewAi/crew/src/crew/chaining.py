from crewai.flow.flow import Flow, start, listen
from litellm import completion

API_KEY = ''

class CityFunFact(Flow):

    @start()
    def generate_random_city(self):
        result = completion(
            model="gemini/gemini-1.5-flash",
            api_key=API_KEY,
            messages=[{"content":"Give any random city name from Pakistan.",
                       "role":"user"}]
        )
        city = result['choices'][0]['message']['content']
        print(city)
        return city
    
    @listen(generate_random_city)
    def generate_fun_fact(self, city_name): # city_name is the return value of generate_random_city which is "city"
        result = completion(
            model="gemini/gemini-2.0-flash-exp",
            api_key=API_KEY,
            messages=[{"content":f"write some fun fact about {city_name}.",
                       "role":"user"}]
        )
        fun_fact = result['choices'][0]['message']['content']
        print(fun_fact)
        self.state['fun_fact'] = fun_fact  # Save the fun fact in the state instead of returning it
        # return fun_fact

    @listen(generate_fun_fact)
    def save_fun_fact(self):    # This function will save the fun fact in a .md file
        with open("fun_fact.md","w") as file:
            file.write(self.state['fun_fact'])
            return self.state['fun_fact']


def kickoff():
    obj = CityFunFact()
    result = obj.kickoff()
   # print(result) # This will print the fun fact second time

