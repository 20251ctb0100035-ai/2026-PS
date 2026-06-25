public class SistemaCardapioSobrecarga {
    // se for so o produto exibira isso
    static void exibirProduto(String nome){
        System.out.println("Produto: " + nome);
    }
    // se for o produto e o preco exibira os dois
    static void exibirProduto(String nome, double preco){
        System.out.println("Produto: " + nome);

        System.out.println("Preço: R$ " + preco);
    }

    public static void main(String[] args){
        exibirProduto("Pizza");
    }
}