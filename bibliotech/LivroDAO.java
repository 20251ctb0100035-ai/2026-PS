import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class LivroDAO {

    public boolean adicionarLivro(String titulo, String autor, int ano) {
        String sql = "INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql)) {

            comando.setString(1, titulo);
            comando.setString(2, autor);
            comando.setInt(3, ano);

            return comando.executeUpdate() > 0;

        } catch (SQLException e) {
            throw new PersistenciaException("Não foi possível adicionar o livro.", e);
        }
    }

    public boolean atualizarLivro(int id, String titulo, String autor, int ano) {
        String sql = "UPDATE livros SET titulo = ?, autor = ?, ano = ? WHERE id = ?";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql)) {

            comando.setString(1, titulo);
            comando.setString(2, autor);
            comando.setInt(3, ano);
            comando.setInt(4, id);

            return comando.executeUpdate() > 0;

        } catch (SQLException e) {
            throw new PersistenciaException("Não foi possível atualizar o livro.", e);
        }
    }

    public boolean excluirLivro(int id) {
        String sql = "DELETE FROM livros WHERE id = ?";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql)) {

            comando.setInt(1, id);
            return comando.executeUpdate() > 0;

        } catch (SQLException e) {
            throw new PersistenciaException("Não foi possível excluir o livro.", e);
        }
    }

    public List<Livro> listarLivros() {
        List<Livro> lista = new ArrayList<>();
        String sql = "SELECT id, titulo, autor, ano, capa FROM livros";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql);
             ResultSet rs = comando.executeQuery()) {

            while (rs.next()) {
                Livro l = new Livro(
                    rs.getInt("id"),
                    rs.getString("titulo"),
                    rs.getString("autor"),
                    rs.getInt("ano")
                );
                l.setCapa(rs.getString("capa"));
                lista.add(l);
            }
            return lista;

        } catch (SQLException e) {
            throw new PersistenciaException("Não foi possível consultar os livros.", e);
        }
    }

    public List<Livro> buscarLivrosPorTitulo(String titulo) {
        List<Livro> lista = new ArrayList<>();
        String sql = "SELECT id, titulo, autor, ano, capa FROM livros WHERE titulo LIKE ?";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql)) {

            comando.setString(1, "%" + titulo + "%");
            try (ResultSet rs = comando.executeQuery()) {
                while (rs.next()) {
                    Livro l = new Livro(
                        rs.getInt("id"),
                        rs.getString("titulo"),
                        rs.getString("autor"),
                        rs.getInt("ano")
                    );
                    l.setCapa(rs.getString("capa"));
                    lista.add(l);
                }
            }
            return lista;

        } catch (SQLException e) {
            throw new PersistenciaException("Não foi possível buscar os livros.", e);
        }
    }

    public Livro buscarLivroPorId(int id) {
        String sql = "SELECT id, titulo, autor, ano, capa FROM livros WHERE id = ?";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql)) {

            comando.setInt(1, id);
            try (ResultSet rs = comando.executeQuery()) {
                if (rs.next()) {
                    Livro l = new Livro(
                        rs.getInt("id"),
                        rs.getString("titulo"),
                        rs.getString("autor"),
                        rs.getInt("ano")
                    );
                    l.setCapa(rs.getString("capa"));
                    return l;
                }
            }
            return null;

        } catch (SQLException e) {
            throw new PersistenciaException("Não foi possível buscar o livro por ID.", e);
        }
    }

    public boolean atualizarCapa(int id, String caminhoCapa) {
        String sql = "UPDATE livros SET capa = ? WHERE id = ?";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql)) {

            comando.setString(1, caminhoCapa);
            comando.setInt(2, id);
            return comando.executeUpdate() > 0;

        } catch (SQLException e) {
            throw new PersistenciaException("Não foi possível atualizar a capa.", e);
        }
    }
}