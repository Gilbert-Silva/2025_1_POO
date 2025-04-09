#include <iostream>
#include <string>

using namespace std;

int main() {
    string nome;
    int idade;

    // Solicita o nome do usuário
    cout << "Informe seu nome: ";
    // cin >> nome;
    getline(cin, nome);  // Utiliza getline para ler o nome, permitindo espaços

    // Solicita a idade do usuário
    cout << "Informe sua idade: ";
    cin >> idade;

    // Exibe a mensagem com o nome e idade
    cout << "Olá " << nome << "! Você tem " << idade << " anos" << endl;

    return 0;
}
