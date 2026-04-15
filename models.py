from pydantic import BaseModel, EmailStr

class Cliente(BaseModel):
    nome: str
    email: EmailStr
    telefone: str
    endereco: str