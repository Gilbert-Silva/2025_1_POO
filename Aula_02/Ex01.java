import java.util.Scanner; // Importa a classe Scanner para lidar com entrada de dados

public class Ex01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Cria um objeto Scanner para ler a entrada do usuário

        // Solicita o nome do usuário
        System.out.print("Informe seu nome: ");
        String nome = scanner.nextLine(); // Lê a linha inteira como uma string

        // Solicita a idade do usuário
        System.out.print("Informe sua idade: ");
        int idade = scanner.nextInt(); // Lê um número inteiro

        // Exibe a mensagem formatada
        System.out.println("Olá " + nome + "! Você tem " + idade + " anos.");

        scanner.close(); // Fecha o Scanner para liberar recursos
    }
}