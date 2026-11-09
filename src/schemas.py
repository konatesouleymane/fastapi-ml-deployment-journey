from pydantic import BaseModel, Field, ConfigDict

class YieldInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    country :str = Field(...,min_length=1)
    crop :str = Field(...)
    year :int = Field(ge=1990, le=2100)
    rainfall_mm	:float = Field(ge=0)
    avg_temp_c	:float = Field(ge=-10, le=45)
    pesticides_tonnes :float = Field(ge=0)


