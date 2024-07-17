# Loja Virtual Django

Este é um projeto de uma loja virtual desenvolvido com Django. Ele inclui funcionalidades básicas de um e-commerce, como listagem de produtos, detalhes dos produtos, adição e remoção de itens do carrinho, visualização do carrinho e finalização de compras.

## Funcionalidades

- **Listagem de Produtos**: Exibe uma lista de produtos disponíveis.
- **Detalhes do Produto**: Exibe informações detalhadas sobre um produto específico.
- **Adicionar ao Carrinho**: Permite adicionar produtos ao carrinho de compras.
- **Remover do Carrinho**: Permite remover produtos do carrinho de compras.
- **Visualizar Carrinho**: Exibe os produtos adicionados ao carrinho.
- **Finalizar Compra**: Permite finalizar a compra dos produtos no carrinho.

## Estrutura do Projeto

- **produto**: Contém as views, models e urls relacionadas aos produtos.
- **loja**: Configurações gerais do projeto, incluindo urls e settings.
- **perfil**: Gerenciamento de perfis de usuários.
- **pedido**: Gerenciamento de pedidos.

## Requisitos

- Python 3.x
- Django 3.x ou superior
- Pillow (para manipulação de imagens)

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/loja-virtual-django.git
    cd loja-virtual-django
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Realize as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

5. Crie um superusuário para acessar o admin do Django:

    ```bash
    python manage.py createsuperuser
    ```

6. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

7. Acesse o projeto no navegador:

    ```
    http://127.0.0.1:8000/
    ```

## Configurações Adicionais

### Arquivos Estáticos e de Mídia

Certifique-se de que as configurações para arquivos estáticos e de mídia estão corretas no arquivo `settings.py`:

```python
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join('templates/static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')