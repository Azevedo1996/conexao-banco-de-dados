import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class ExemploJavaDB {
    public static void main(String[] args) {
        Connection connection = null;
        Statement statement = null;
        ResultSet resultSet = null;

        try {
            // Configuração da conexão com o banco de dados
            String jdbcURL = "jdbc:mysql://localhost:3306/seu_banco_de_dados";
            String username = "seu_usuario";
            String password = "sua_senha";

            // Estabelecendo a conexão com o banco de dados
            connection = DriverManager.getConnection(jdbcURL, username, password);

            // Criando uma declaração
            statement = connection.createStatement();

            // Executando uma consulta SQL
            String query = "SELECT * FROM usuarios";
            resultSet = statement.executeQuery(query);

            // Exibindo os dados
            while (resultSet.next()) {
                String nome = resultSet.getString("nome");
                String email = resultSet.getString("email");
                System.out.println("Nome: " + nome + ", Email: " + email);
            }

        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // Fechando os recursos
            try {
                if (resultSet != null) {
                    resultSet.close();
                }
                if (statement != null) {
                    statement.close();
                }
                if (connection != null) {
                    connection.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
