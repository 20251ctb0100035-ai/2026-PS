import java.util.ArrayList;

public class CatalogoProdutos {

static void adicionarProduto(ArrayList<String> lista, String nome) {
    lista.add(nome);
}

static void listarProdutos(ArrayList<String> lista) {
    for (String nome : lista) {
        System.out.println("- " + nome);
    }
}

public static void main(String[] args) {
    ArrayList<String> lista = new ArrayList<>();
    
    adicionarProduto(lista, "Pizza");
    adicionarProduto(lista, "Suco");
    listarProdutos(lista);
    }
}