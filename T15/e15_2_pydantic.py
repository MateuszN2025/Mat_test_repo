# PYDANTIC LEARNING PATH: Most Common Cases
from pydantic import BaseModel, Field, ValidationError, field_validator, ConfigDict
from typing import Optional
import w_r


# =============================================================================
# Define all models
# =============================================================================

# 1. Basic model with required fields
class User(BaseModel):
    id: int
    name: str
    grade: str = Field(min_length=2)
    
    def __str__(self):
        return f"---{self.name}---\n" + super().__str__()
    
@w_r
def main():
    u1 = User(id=1, name="Mat", grade="AB")
    print(u1)
    
    # u2 = User(id="2", name="Brad")
    # print(u2)
    
    # try:
    #     u3 = User(id="a", name="John")
    #     print(u3)
    # except Exception as e:
    #     print(f"⚠️{str(e)[:80]}")
        
    # try:
    #     u4 = User(id=1, name=1111)
    #     print(u4)
    # except Exception as e:
    #     print(f"⚠️{str(e)[:80]}")
     
        

main()