import javax.imageio.ImageIO;
import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.table.*;
import java.awt.*;
import java.io.File;
import java.nio.file.*;
import java.util.List;

public class TelaBiblioteca extends JFrame {
    private JTable tabela;
    private DefaultTableModel modelo;
    private JTextField campoBusca = new JTextField(16);
    private LivroDAO dao = new LivroDAO();

    public TelaBiblioteca() {
        setTitle("BiblioTech - Gerenciamento");
        setSize(760, 500);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        JPanel root = new JPanel(new BorderLayout(10, 10));
        root.setBackground(new Color(240, 244, 248));
        root.setBorder(new EmptyBorder(12, 12, 12, 12));
        setContentPane(root);

        // Topo personalizado
        JPanel topo = new JPanel(new FlowLayout(FlowLayout.LEFT));
        topo.setBackground(new Color(30, 58, 138));
        JLabel lbl = new JLabel("Pesquisar:");
        lbl.setForeground(Color.WHITE);
        JButton btnBuscar = new JButton("Buscar");
        JButton btnTodos = new JButton("Todos");
        JButton btnCapa = new JButton("Selecionar capa");
        JButton btnNovo = new JButton("Novo Livro");

        topo.add(lbl); topo.add(campoBusca);
        topo.add(btnBuscar); topo.add(btnTodos);
        topo.add(btnCapa); topo.add(btnNovo);
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

        btnBuscar.addActionListener(e -> atualizarTabela(dao.buscarLivrosPorTitulo(campoBusca.getText().trim())));
        btnTodos.addActionListener(e -> carregarLivros());
        btnCapa.addActionListener(e -> selecionarCapa());
        btnNovo.addActionListener(e -> new TelaCadastroLivro(this).setVisible(true));

        carregarLivros();
    }

    public void carregarLivros() {
        atualizarTabela(dao.listarLivros());
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
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(this, "Erro: " + ex.getMessage());
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new TelaBiblioteca().setVisible(true));
    }
}