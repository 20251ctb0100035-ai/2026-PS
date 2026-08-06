public class Livro {  // o codigo faz um sistema de controle de biblioteca, permitindo gerenciar livros, incluindo empréstimos e devoluções, garantindo que as operações sejam válidas e consistentes com a quantidade disponível.
    // Atributos privados da classe
    private int isbn;
    private String titulo;
    private String autor;
    private int disponivel;

    // Construtor da classe Livro que inicializa os atributos com os valores fornecidos.
    public Livro(int isbn, String titulo, String autor, int disponivel) {
        setISBN(isbn);
        setTitulo(titulo);
        setAutor(autor);

        // VALIDACAO DA Quantidade do construtor
        if (disponivel >= 0) {
            this.disponivel = disponivel;
        } else {
            this.disponivel = 0; // Se a quantidade fornecida for negativa, inicializa como 0
        }
    }

    // Métodos para acessar os valores dos atributos
    public int getISBN() {
        return isbn;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public int getDisponivel() {
        return disponivel;
    }

    // Métodos setters para modificar os valores dos atributos com validação
    public void setISBN(int isbn) {
        if (isbn >= 0) { // Validação para garantir que o ISBN seja um número não negativo
            this.isbn = isbn;
        } else {
            System.out.println("ISBN inválido. O ISBN deve ser um número não negativo.");
        }
    }

    public void setTitulo(String titulo) {
        if (titulo != null && !titulo.isBlank()) { // Validação para garantir que o título não seja nulo ou vazio
            this.titulo = titulo;
        } else {
            System.out.println("Título inválido. O título não pode ser nulo ou vazio.");
        }
    }

    public void setAutor(String autor) {
        if (autor != null && !autor.isBlank()) { // Validação para garantir que o autor não seja nulo ou vazio
            this.autor = autor;
        } else {
            System.out.println("Autor inválido. O autor não pode ser nulo ou vazio.");
        }
    }

    public void setDisponivel(int disponivel) {
        if (disponivel >= 0) { // Validação para garantir que a quantidade disponível seja um número não negativo
            this.disponivel = disponivel;
        }
    }

    // emprestar: reduz a quantidade disponível se possível
    public boolean emprestar(int qtd) {
        if (qtd > 0 && disponivel >= qtd) {
            disponivel -= qtd;
            return true;
        }
        return false;
    }

    // devolver: aumenta a quantidade disponível
    public boolean devolver(int qtd) {
        if (qtd > 0) {
            disponivel += qtd;
            return true;
        }
        return false;
    }
}

