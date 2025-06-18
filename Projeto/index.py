import streamlit as st
from views import View
from templates.mantercategoriaUI import ManterCategoriaUI
from templates.manterclienteUI import ManterClienteUI
from templates.manterprodutoUI import ManterProdutoUI

class IndexUI:
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Categorias", "Cadastro de Clientes", "Cadastro de Produtos", "Listagem de Vendas"])
        if op == "Cadastro de Categorias": ManterCategoriaUI.main()
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Produtos": ManterProdutoUI.main()

    def sidebar():
        IndexUI.menu_admin()
    
    def main():
        # verifica a existe o usuário admin
        View.cadastrar_admin()
        # monta o sidebar
        IndexUI.sidebar()

IndexUI.main()
