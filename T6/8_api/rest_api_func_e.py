import requests

class Pokemon:
    def __init__(self, name):
        self.name = name

    def get_poke_info(self):

        poke_url = f"https://pokeapi.co/api/v2/pokemon/{self.name}"
        req = requests.get(poke_url)
        poke_url_names = "https://pokeapi.co/api/v2/pokemon/"
        req2 = requests.get(poke_url_names)
        list1 = []
        for item in req2.json()["results"]:
            for key, value in item.items():
                if key == "name":
                    list1.append(value)

        # dict2 = {}
        # dict1 = {} # ⚠️
        # 
        # for poke in list1[:2]:            
        #     poke_url = f"https://pokeapi.co/api/v2/pokemon/{poke}"
        #     req = requests.get(poke_url)
        #     print("------------------------------------------")
        #     print(f"> poke:{req.json()['name']}")
        #     #1# bulbasaur
        #     #2# ivysaur
        #     print("------------------------------------------")
        #     for key, value in req.json().items():
        #         if isinstance(value, int) and not isinstance(value, bool):
        #             dict1[key] = value
        #             print(f">>>>>> dict1:{dict1}")
        #             #1# dict1:{'base_experience': 64, 'height': 7, 'id': 1, 'order': 1, 'weight': 69}
        #             #2# dict1:{'base_experience': 142, 'height': 10, 'id': 2, 'order': 2, 'weight': 130}
        #     dict2[req.json()["name"]] = dict1 
        #     print(f">>>>>>>>>>>> dict2:{dict2}")      
        #     #1# dict2:{'bulbasaur': {'base_experience': 64, 'height': 7, 'id': 1, 'order': 1, 'weight': 69}}  
        #     #2# dict2:{'bulbasaur': <dict1> {'base_experience': 142, 'height': 10, 'id': 2, 'order': 2, 'weight': 130} ⚠️ <== dict1 ,
        #     #          'ivysaur'  : <dict1> {'base_experience': 142, 'height': 10, 'id': 2, 'order': 2, 'weight': 130} <== dict1
        #
        #     # >>>>>>>>>>>>>>>>>>>>>>>> ⚠️ dict3:{'bulbasaur': 129834405571648, 'ivysaur': 129834405571648}
        # 
        #  In this case dict1 refereing to the same object in memory
        # 
        #  bulbasaur has the same values because dict1 is referring to the new updated values for ivysaur
        # 
        
        dict2 = {}
        
        dict3 = {}
        dict3_ = {}   
        
        dict4 = {}         
        
        for poke in list1[:3]:   
            dict1 = {} # ℹ️    
            dict4_ = {}
            poke_url = f"https://pokeapi.co/api/v2/pokemon/{poke}"
            req = requests.get(poke_url)
            print("------------------------------------------")
            print(f"> poke:{req.json()['name']}")
            #1# bulbasaur
            #2# ivysaur
            print("------------------------------------------")
            for key, value in req.json().items():
                if isinstance(value, int) and not isinstance(value, bool):
                    dict1[key] = value
                    print(f">>>>>> dict1:{dict1}")
                    #1# dict1:{'base_experience': 64, 'height': 7, 'id': 1, 'order': 1, 'weight': 69}
                    #2# dict1:{'base_experience': 142, 'height': 10, 'id': 2, 'order': 2, 'weight': 130}
            dict2[req.json()["name"]] = dict1 
            dict3[req.json()["name"]] = id(dict3_)
            dict4[req.json()["name"]] = id(dict4_)
            print(f">>>>>>>>>>>> dict2:{dict2}")   
            print(f">>>>>>>>>>>>>>>>>>>>>>>> ⚠️ dict3:{dict3}")  # every time refers to the SAME dict/object in memory   
            print(f">>>>>>>>>>>>>>>>>>>>>>>> ℹ️ dict4:{dict4}")  # every time NEW dict is created in memory    
               
            #1# dict2:{'bulbasaur': {'base_experience': 64, 'height': 7, 'id': 1, 'order': 1, 'weight': 69}}  
            #2# dict2:{'bulbasaur': <dict1> {'base_experience': 64, 'height': 7, 'id': 1, 'order': 1, 'weight': 69}}   ℹ️ <== dict1 ,
            #          'ivysaur'  : <dict1> {'base_experience': 142, 'height': 10, 'id': 2, 'order': 2, 'weight': 130} <== dict1
            #
            # >>>>>>>>>>>>>>>>>>>>>>>> ⚠️ dict3:{'bulbasaur': 129834405571648, 'ivysaur': 129834405571648}
            # >>>>>>>>>>>>>>>>>>>>>>>> ℹ️ dict4:{'bulbasaur': 129834405570368, 'ivysaur': 129834404650048} 
        
        return dict2

# p = Pokemon("ditto")
# p.get_poke_info()

        