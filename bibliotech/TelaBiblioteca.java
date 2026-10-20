import javax.swing.JFrame;
import javax.swing.SwingUtilities;

public class TelaBiblioteca extends JFrame {
    private Biblioteca biblioteca;

    public TelaBiblioteca(Biblioteca biblioteca) {
        this.biblioteca = biblioteca;

        setTitle("BiblioTech");
        setSize(760, 480);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
    }

    public static void main(String[] args) {
        Biblioteca biblioteca = new Biblioteca();

        SwingUtilities.invokeLater(() -> {
            TelaBiblioteca tela = new TelaBiblioteca(biblioteca);
            tela.setVisible(true);
        });
    }
}