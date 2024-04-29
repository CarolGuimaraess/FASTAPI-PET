from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

class Pet(BaseModel):
    id: int
    nome: str
    especie: str
    idade: Optional[int] = None
    cor: Optional[str] = None

app = FastAPI()

banco_de_dados = []
id_atual = 0

@app.post("/pets/", response_model=Pet)
def criar_pet(pet: Pet):
    global id_atual
    id_atual += 1
    pet.id = id_atual
    banco_de_dados.append(pet)
    return pet

@app.get("/pets/{pet_id}", response_model=Pet)
def obter_pet(pet_id: int):
    for pet in banco_de_dados:
        if pet.id == pet_id:
            return pet
    raise HTTPException(status_code=404, detail="Pet não encontrado")

@app.put("/pets/{pet_id}", response_model=Pet)
def atualizar_pet(pet_id: int, pet: Pet):
    for index, p in enumerate(banco_de_dados):
        if p.id == pet_id:
            banco_de_dados[index] = pet
            return pet
    raise HTTPException(status_code=404, detail="Pet não encontrado")

@app.delete("/pets/{pet_id}", response_model=Pet)
def deletar_pet(pet_id: int):
    for index, pet in enumerate(banco_de_dados):
        if pet.id == pet_id:
            del banco_de_dados[index]
            return pet
    raise HTTPException(status_code=404, detail="Pet não encontrado")

@app.get("/pets/", response_model=List[Pet])
def listar_pets():
    return banco_de_dados

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)