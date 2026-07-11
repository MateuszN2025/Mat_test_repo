import w_r
from dataclasses import dataclass


class FakeCamera1():
    def __init__(self, name: str, port: str, status:str) -> None:
        self.name = name
        self.port = port
        self.status = status
        
    def get_data(self):
        print(f"name:{self.name}")
        print(f"port:{self.port}")
        print(f"status:{self.status}")
        return [self.name, self.port, self.status]
    
@dataclass
class FakeCamera2():
    name: str
    port: str
    status: str
    
    def get_data(self):
        print(f"name:{self.name}")
        print(f"port:{self.port}")
        print(f"status:{self.status}")
        return [self.name, self.port, self.status]
        
    
@w_r        
def main():       
    fc1 = FakeCamera1("logi1000", "1.0.22.1", "healty")
    fc1_data = fc1.get_data()
    print(fc1_data)
    print("------------------------------------------")
    fc2 = FakeCamera2("tcl232", "9.3.3.3", "failed")
    fc2_data = fc2.get_data()
    print(fc2_data)
    
if __name__ == "__main__":
    main()