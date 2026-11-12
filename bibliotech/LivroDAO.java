import java.sql.*;
import java.util.*;

public class LivroDAO {

    public void inserir(Livro livro) {
        String sql = "INSERT INTO livros (titulo, autor, ano, capa) VALUES (?, ?, ?, ?)";
        try (Connection c = Conexao.conectar(); PreparedStatement ps = c.prepareStatement(sql)) {
            ps.setString(1, livro.getTitulo());
            ps.setString(2, livro.getAutor());
            ps.setInt(3, livro.getAno());
            ps.setString(4, livro.getCapa());
            ps.executeUpdate();
        } catch (SQLException e) {
            System.out.println("Erro ao inserir: " + e.getMessage());
        }
    }

    public boolean adicionarLivro(String titulo, String autor, int ano) {
        String sql = "INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)";
        try (Connection c = Conexao.conectar(); PreparedStatement ps = c.prepareStatement(sql)) {
            ps.setString(1, titulo);
            ps.setString(2, autor);
            ps.setInt(3, ano);
            return ps.executeUpdate() > 0;
        } catch (SQLException e) {
            System.out.println("Erro ao adicionar livro: " + e.getMessage());
            return false;
        }
    }

    public List<Livro> listarLivros() {
        List<Livro> lista = new ArrayList<>();
        String sql = "SELECT id, titulo, autor, ano, capa FROM livros ORDER BY titulo";
        try (Connection c = Conexao.conectar(); PreparedStatement ps = c.prepareStatement(sql); ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                Livro l = new Livro(rs.getInt("id"), rs.getString("titulo"), rs.getString("autor"), rs.getInt("ano"));
                l.setCapa(rs.getString("capa"));
                lista.add(l);
            }
        } catch (SQLException e) {
            System.out.println("Erro ao listar: " + e.getMessage());
        }
        return lista;
    }

    public Livro buscarLivroPorId(int id) {
        String sql = "SELECT id, titulo, autor, ano, capa FROM livros WHERE id = ?";
        try (Connection c = Conexao.conectar(); PreparedStatement ps = c.prepareStatement(sql)) {
            ps.setInt(1, id);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    Livro l = new Livro(rs.getInt("id"), rs.getString("titulo"), rs.getString("autor"), rs.getInt("ano"));
                    l.setCapa(rs.getString("capa"));
                    return l;
                }
            }
        } catch (SQLException e) {
            System.out.println("Erro ao buscar por ID: " + e.getMessage());
        }
        return null;
    }

    public List<Livro> buscarLivrosPorTitulo(String termo) {
        List<Livro> lista = new ArrayList<>();
        String sql = "SELECT id, titulo, autor, ano, capa FROM livros WHERE titulo LIKE ? ORDER BY titulo";
        try (Connection c = Conexao.conectar(); PreparedStatement ps = c.prepareStatement(sql)) {
            ps.setString(1, "%" + termo + "%");
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    Livro l = new Livro(rs.getInt("id"), rs.getString("titulo"), rs.getString("autor"), rs.getInt("ano"));
                    l.setCapa(rs.getString("capa"));
                    lista.add(l);
                }
            }
        } catch (SQLException e) {
            System.out.println("Erro na busca: " + e.getMessage());
        }
        return lista;
    }

    public boolean atualizarLivro(int id, String titulo, String autor, int ano) {
        String sql = "UPDATE livros SET titulo = ?, autor = ?, ano = ? WHERE id = ?";
        try (Connection c = Conexao.conectar(); PreparedStatement ps = c.prepareStatement(sql)) {
            ps.setString(1, titulo);
            ps.setString(2, autor);
            ps.setInt(3, ano);
            ps.setInt(4, id);
            return ps.executeUpdate() > 0;
        } catch (SQLException e) {
            System.out.println("Erro ao atualizar livro: " + e.getMessage());
            return false;
        }
    }

    public boolean excluirLivro(int id) {
        String sql = "DELETE FROM livros WHERE id = ?";
        try (Connection c = Conexao.conectar(); PreparedStatement ps = c.prepareStatement(sql)) {
            ps.setInt(1, id);
            return ps.executeUpdate() > 0;
        } catch (SQLException e) {
            System.out.println("Erro ao excluir livro: " + e.getMessage());
            return false;
        }
    }

    public boolean atualizarCapa(int id, String caminho) {
        String sql = "UPDATE livros SET capa = ? WHERE id = ?";
        try (Connection c = Conexao.conectar(); PreparedStatement ps = c.prepareStatement(sql)) {
            ps.setString(1, caminho);
            ps.setInt(2, id);
            return ps.executeUpdate() > 0;
        } catch (SQLException e) {
            System.out.println("Erro ao atualizar capa: " + e.getMessage());
            return false;
        }
    }
}