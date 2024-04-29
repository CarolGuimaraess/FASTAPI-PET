# FASTAPI-PET

# API para gerencionamento de PET

A API utiliza o framework FastAPI em Python.

# Instalação
Após ter dado git clone no projeto, para executar, você precisará do Python instalado em seu sistema. 

Em seguida, instale as dependências usando o pip:
- pip install fastapi uvicorn

# Para iniciar o servidor da API, execute o seguinte comando:
- uvicorn main:app --reload

Isso iniciará o servidor na porta padrão 8000. 
Você pode acessar a documentação interativa da API em http://127.0.0.1:8000/docs.

# Endpoints
- Criar um novo pet: Envie uma solicitação POST para /pets/ com os detalhes do pet no corpo da solicitação.
- Obter informações de um pet: Envie uma solicitação GET para /pets/{pet_id} com o ID do pet desejado.
- Atualizar informações de um pet: Envie uma solicitação PUT para /pets/{pet_id} com os novos detalhes do pet no corpo da solicitação.
- Deletar um pet: Envie uma solicitação DELETE para /pets/{pet_id} com o ID do pet que deseja excluir.
- Listar todos os pets: Envie uma solicitação GET para /pets/ para obter uma lista de todos os pets cadastrados.
