using System;
using System.Data.SqlClient;

class Program
{
    static void Main()
    {
        // Configuração da conexão com o banco de dados
        string connectionString = "Data Source=localhost;Initial Catalog=seu_banco_de_dados;User ID=seu_usuario;Password=sua_senha;";
        
        // Consulta ao banco de dados
        string query = "SELECT * FROM usuarios";

        using (SqlConnection connection = new SqlConnection(connectionString))
        {
            connection.Open();

            SqlCommand command = new SqlCommand(query, connection);
            SqlDataReader reader = command.ExecuteReader();

            // Exibição dos dados
            while (reader.Read())
            {
                Console.WriteLine($"Nome: {reader["nome"]}, Email: {reader["email"]}");
            }
            
            reader.Close();
        }
    }
}
