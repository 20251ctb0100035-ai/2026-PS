/*
 * Disciplina: 2026-PS
 * Projeto   : bibliotech
 * Arquivo   : Leitor.java
 * Autor     : Anthony Pagani
 * Descricao : Leitor E UM TIPO DE Usuario: herda nome, matricula e entrar().
 */ 
public class Leitor extends Usuario {

    // So o que a caixa Leitor acrescenta. Nome e matricula ja vem de Usuario.
    private int limiteEmprestimos;
    private int LivrosEmMaos;   // nao estava na caixa: o codigo pediu

    public Leitor(String nome, String matricula, int limiteEmprestimos) {
        super(nome, matricula); // primeiro a parte de Usuario, depois a de Leitor
        this.limiteEmprestimos = limiteEmprestimos;
        this.LivrosEmMaos = 0;
    }
}
    public int getLimiteEmprestimos() {
        return limiteEmprestimos;
    }

    public int getLivrosEmMaos() {
        return livrosEmMaos;
    }

    // OPERACAO DA CAIXA: podePegarEmprestado().
    public boolean podePegarEmprestado() {
        return livrosEmMaos < limiteEmprestimos;
    }

    // Os dois metodos que o emprestimos vai usar na Aula 38.
    public void pegouLivro() {
        this.livrosEmMaos = this.livrosEmMaos + 1;
    }

    public void devolveuLivro() {
        this.livrosEmMaos = this.livrosEmMaos - 1;
    }

    public String toString() {
        return "Leitor " + getnome + " (" + getMatricula() + ") - "
               + livrosEmMaos + " de " + limiteEmprestimos + " livros";
    }