from fastapi import APIRouter, HTTPException
from database import colecao
from models import Cliente
from bson import ObjectId

router = APIRouter()

def cliente_helper(cliente):
    return {
        "id": str(cliente["_id"]),
        "nome": cliente["nome"],
        "email": cliente["email"],
        "telefone": cliente["telefone"],
        "endereco": cliente["endereco"]
    }

# CREATE
@router.post("/clientes")
def criar_cliente(cliente: Cliente):
    result = colecao.insert_one(cliente.dict())
    return {"id": str(result.inserted_id)}

# READ ALL
@router.get("/clientes")
def listar_clientes():
    return [cliente_helper(c) for c in colecao.find()]

# READ ONE
@router.get("/clientes/{id}")
def buscar_cliente(id: str):
    cliente = colecao.find_one({"_id": ObjectId(id)})
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente_helper(cliente)

# UPDATE
@router.put("/clientes/{id}")
def atualizar_cliente(id: str, cliente: Cliente):
    result = colecao.update_one(
        {"_id": ObjectId(id)},
        {"$set": cliente.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return {"msg": "Atualizado com sucesso"}

# DELETE
@router.delete("/clientes/{id}")
def deletar_cliente(id: str):
    result = colecao.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return {"msg": "Deletado com sucesso"}