public class Produto {

    public int codigo;
    public String nome;
    public double preco;

    public Produto (int codigo, String nome, double preco) { // Construtor
        this.codigo = codigo;
        this.nome = nome;
        this.preco = preco;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo() {
        this.codigo = codigo;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public void alterarPreco (double preco) {
        this.preco = preco;
    }

    public void alterarPreco(double preco, double desconto) {
        // Aplica a porcentagem de desconto
        this.preco = preco - (preco * (desconto / 100.0));
    }

    public String toString() {
        return String.format("%d - %s - R$ %.2f", codigo, nome, preco);
    }
}