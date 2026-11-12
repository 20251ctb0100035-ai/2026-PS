import javax.swing.*;
import javax.swing.border.EmptyBorder;
import java.awt.*;

public class TelaCadastroLivro extends JFrame {
    public TelaCadastroLivro(TelaBiblioteca pai) {
        setTitle("BiblioTech - Novo Livro");
        setSize(360, 260);
        setLocationRelativeTo(pai);
        setDefaultCloseOperation(DISPOSE_ON_CLOSE);

        JPanel p = new JPanel(new GridLayout(4, 2, 8, 8));
        p.setBackground(new Color(240, 244, 248));
        p.setBorder(new EmptyBorder(16, 16, 16, 16));

        JTextField txtTitulo = new JTextField();
        JTextField txtAutor = new JTextField();
        JTextField txtAno = new JTextField();
        JButton btnSalvar = new JButton("Salvar");
        btnSalvar.setBackground(new Color(30, 58, 138));
        btnSalvar.setForeground(Color.WHITE);

        p.add(new JLabel("Título:")); p.add(txtTitulo);
        p.add(new JLabel("Autor:"));  p.add(txtAutor);
        p.add(new JLabel("Ano:"));    p.add(txtAno);
        p.add(new JLabel());          p.add(btnSalvar);
        setContentPane(p);

        btnSalvar.addActionListener(e -> {
            try {
                Livro l = new Livro(txtTitulo.getText(), txtAutor.getText(), Integer.parseInt(txtAno.getText()));
                new LivroDAO().inserir(l);
                pai.carregarLivros();
                dispose();
            } catch (Exception ex) {
                JOptionPane.showMessageDialog(this, "Preencha os dados corretamente.");
            }
        });
    }
}