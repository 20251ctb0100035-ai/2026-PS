import javax.swing.*;
import javax.swing.border.EmptyBorder;
import java.awt.*;

public class TelaCadastroLivro extends JFrame {
    public TelaCadastroLivro(TelaBiblioteca telaPrincipal) {
        setTitle("BiblioTech - Novo Livro");
        setSize(360, 260);
        setLocationRelativeTo(telaPrincipal);
        setDefaultCloseOperation(DISPOSE_ON_CLOSE);

        JPanel p = new JPanel(new GridLayout(4, 2, 8, 8));
        p.setBackground(new Color(240, 244, 248));
        p.setBorder(new EmptyBorder(16, 16, 16, 16));

        JTextField campoTitulo = new JTextField();
        JTextField campoAutor = new JTextField();
        JTextField campoAno = new JTextField();
        JButton btnSalvar = new JButton("Salvar");
        btnSalvar.setBackground(new Color(30, 58, 138));
        btnSalvar.setForeground(Color.WHITE);

        p.add(new JLabel("Título:")); p.add(campoTitulo);
        p.add(new JLabel("Autor:"));  p.add(campoAutor);
        p.add(new JLabel("Ano:"));    p.add(campoAno);
        p.add(new JLabel());          p.add(btnSalvar);
        setContentPane(p);

        btnSalvar.addActionListener(e -> {
            try {
            String titulo = campoTitulo.getText().trim();
            String autor = campoAutor.getText().trim();
            int ano = Integer.parseInt(campoAno.getText().trim());

            ValidadorLivro.validar(titulo, autor, ano);

            LivroDAO dao = new LivroDAO();
            dao.adicionarLivro(titulo, autor, ano);

            JOptionPane.showMessageDialog(this, "Livro cadastrado com sucesso!");
            telaPrincipal.carregarLivros(); // atualiza a tabela da TelaBiblioteca
            dispose(); // fecha a janela de cadastro

        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "O ano deve ser um número inteiro.");
        } catch (LivroInvalidoException ex) {
            JOptionPane.showMessageDialog(this, ex.getMessage());
        } catch (PersistenciaException ex) {
            JOptionPane.showMessageDialog(this, "Não foi possível salvar o livro no banco.");
        }
        });
    }
}