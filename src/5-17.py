from pydantic import BaseModel, Field


class Creature(BaseModel):
    name: str = Field(..., min_length=2)
    country: str
    area: str
    description: str
    aka: str


bad_creature = Creature(name="!", area="your attic", description="it's a raccoon")
