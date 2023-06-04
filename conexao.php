<?php
// Conexão com o banco de dados
$conn = mysqli_connect("localhost", "seu_usuario", "sua_senha", "seu_banco_de_dados");

// Consulta ao banco de dados
$query = "SELECT * FROM usuarios";
$result = mysqli_query($conn, $query);

// Exibição dos dados
while ($row = mysqli_fetch_assoc($result)) {
  echo "Nome: {$row['nome']}, Email: {$row['email']}<br>";
}

// Fechamento da conexão
mysqli_close($conn);
?>
