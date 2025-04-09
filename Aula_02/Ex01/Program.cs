class Program
{
    static void Main(string[] args)
    {
        // Solicita o nome do usuário
        Console.WriteLine("Informe seu nome:");
        string nome = Console.ReadLine();

        // Solicita a idade do usuário
        Console.WriteLine("Informe sua idade:");
        int idade = int.Parse(Console.ReadLine());

        // Exibe a mensagem formatada
        Console.WriteLine($"Olá {nome}! Você tem {idade} anos.");
    }
}
