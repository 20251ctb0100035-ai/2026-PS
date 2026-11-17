import javax.imageio.ImageIO;
import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.table.*;
import java.awt.*;
import java.io.File;
import java.io.IOException;
import java.util.List;

public class TelaBiblioteca extends JFrame {
    private JTable tabela;
    private DefaultTableModel modelo;
    private JTextField campoBusca = new JTextField(12);
    private JTextField campoId = new JTextField(4);
    private JLabel status = new JLabel("Pronto.");
    private LivroDAO dao = new LivroDAO();

    public TelaBiblioteca() {
        setTitle("BiblioTech - Gerenciamento");
        setSize(850, 520);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        JPanel root = new JPanel(new BorderLayout(10, 10));
        root.setBackground(new Color(240, 244, 248));
        root.setBorder(new EmptyBorder(12, 12, 12, 12));
        setContentPane(root);

        // Topo personalizado
        JPanel topo = new JPanel(new FlowLayout(FlowLayout.LEFT));
        topo.setBackground(new Color(30, 58, 138));
        
        JLabel lbl = new JLabel("Título:");
        lbl.setForeground(Color.WHITE);
        JButton btnBuscar = new JButton("Buscar");
        
        JLabel lblId = new JLabel("ID:");
        lblId.setForeground(Color.WHITE);
        JButton btnBuscarId = new JButton("Buscar ID");

        JButton btnTodos = new JButton("Todos");
        JButton btnCapa = new JButton("Selecionar capa");
        JButton btnNovo = new JButton("Novo Livro");

        topo.add(lbl); topo.add(campoBusca); topo.add(btnBuscar);
        topo.add(lblId); topo.add(campoId); topo.add(btnBuscarId);
        topo.add(btnTodos); topo.add(btnCapa); topo.add(btnNovo);
        root.add(topo, BorderLayout.NORTH);

        // Tabela com coluna Capa
        modelo = new DefaultTableModel(new Object[]{"ID", "Capa", "Título", "Autor", "Ano"}, 0) {
            public boolean isCellEditable(int r, int c) { return false; }
        };
        tabela = new JTable(modelo);
        tabela.setRowHeight(80);
        tabela.setFont(new Font("SansSerif", Font.PLAIN, 14));
        tabela.getTableHeader().setFont(new Font("SansSerif", Font.BOLD, 14));
        tabela.getTableHeader().setBackground(new Color(219, 234, 254));
        tabela.getColumnModel().getColumn(1).setPreferredWidth(80);
        tabela.getColumnModel().getColumn(1).setCellRenderer(new DefaultTableCellRenderer() {
            public Component getTableCellRendererComponent(JTable t, Object val, boolean sel, boolean foc, int r, int c) {
                JLabel l = new JLabel("", JLabel.CENTER);
                l.setOpaque(true);
                l.setBackground(sel ? t.getSelectionBackground() : t.getBackground());
                if (val instanceof ImageIcon) l.setIcon((ImageIcon) val);
                else l.setText("Sem capa");
                return l;
            }
        });

        root.add(new JScrollPane(tabela), BorderLayout.CENTER);
        root.add(status, BorderLayout.SOUTH);

        btnBuscar.addActionListener(e -> buscarPorTitulo());
        btnBuscarId.addActionListener(e -> buscarPorId());
        btnTodos.addActionListener(e -> carregarLivros());
        btnCapa.addActionListener(e -> selecionarCapa());
        btnNovo.addActionListener(e -> new TelaCadastroLivro(this).setVisible(true));

        carregarLivros();
    }

    private void buscarPorTitulo() {
        try {
            List<Livro> livros = dao.buscarLivrosPorTitulo(campoBusca.getText().trim());
            atualizarTabela(livros);
            status.setText("Livros encontrados: " + livros.size());
        } catch (PersistenciaException e) {
            tratarErroBanco(e);
        }
    }

    private void buscarPorId() {
        String texto = campoId.getText().trim();
        int id;

        try {
            id = Integer.parseInt(texto);
            if (id <= 0) {
                throw new IllegalArgumentException("O ID deve ser positivo.");
            }
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(this, "Informe um número inteiro válido.");
            return;
        } catch (IllegalArgumentException e) {
            JOptionPane.showMessageDialog(this, e.getMessage());
            return;
        }

        try {
            Livro livro = dao.buscarLivroPorId(id);
            modelo.setRowCount(0);
            if (livro != null) {
                modelo.addRow(new Object[]{livro.getId(), carregarMiniatura(livro.getCapa()), livro.getTitulo(), livro.getAutor(), livro.getAno()});
                status.setText("Livro encontrado.");
            } else {
                status.setText("Nenhum livro com ID " + id);
            }
        } catch (PersistenciaException e) {
            tratarErroBanco(e);
        }
    }

    public void carregarLivros() {
        try {
            List<Livro> livros = dao.listarLivros();
            atualizarTabela(livros);
            status.setText("Livros encontrados: " + livros.size());
        } catch (PersistenciaException e) {
            tratarErroBanco(e);
        }
    }

    private void tratarErroBanco(PersistenciaException e) {
        status.setText("Erro ao consultar o banco.");
        System.err.println(e.getMessage());
        e.printStackTrace();

        JOptionPane.showMessageDialog(
            this,
            "Não foi possível carregar os livros. Verifique a conexão com o MariaDB.",
            "Erro de conexão",
            JOptionPane.ERROR_MESSAGE
        );
    }

    private void atualizarTabela(List<Livro> livros) {
        modelo.setRowCount(0);
        for (Livro l : livros) {
            modelo.addRow(new Object[]{l.getId(), carregarMiniatura(l.getCapa()), l.getTitulo(), l.getAutor(), l.getAno()});
        }
    }

    private ImageIcon carregarMiniatura(String caminho) {
        try {
            if (caminho == null || caminho.isBlank()) return null;
            File f = new File(caminho);
            if (!f.isFile()) return null;
            Image img = ImageIO.read(f).getScaledInstance(55, 75, Image.SCALE_SMOOTH);
            return new ImageIcon(img);
        } catch (Exception e) { return null; }
    }

    private void selecionarCapa() {
        int linha = tabela.getSelectedRow();
        if (linha == -1) { JOptionPane.showMessageDialog(this, "Selecione um livro."); return; }
        int id = (int) modelo.getValueAt(tabela.convertRowIndexToModel(linha), 0);

        JFileChooser fc = new JFileChooser();
        fc.setFileFilter(new FileNameExtensionFilter("Imagens (JPG/PNG)", "jpg", "jpeg", "png"));
        if (fc.showOpenDialog(this) != JFileChooser.APPROVE_OPTION) return;

        try {
            String caminho = ImagemLivro.salvar(fc.getSelectedFile().toPath(), id);
            if (dao.atualizarCapa(id, caminho)) {
                carregarLivros();
                JOptionPane.showMessageDialog(this, "Capa salva!");
            }
        } catch (IOException ex) {
            JOptionPane.showMessageDialog(this, "Não foi possível salvar a imagem.", "Erro", JOptionPane.ERROR_MESSAGE);
            ex.printStackTrace();
        } catch (PersistenciaException ex) {
            tratarErroBanco(ex);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new TelaBiblioteca().setVisible(true));
    }
}