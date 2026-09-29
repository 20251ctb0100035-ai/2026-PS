import java.util.ArrayList;
import java.util.Scanner;

public class main {

    static Scanner teclado = new Scanner(System.in);
    static ArrayList<Produto> produtos = new ArrayList<>();

    public static void main(String[] args) {

        int opcao = 0;

        while (opcao != 5) {

            System.out.println("\n=== SISTEMA DE PRODUTOS ===");
            System.out.println("1 - Cadastrar");
            System.out.println("2 - Listar");
            System.out.println("3 - Alterar preço");
            System.out.println("4 - Remover");
            System.out.println("5 - SAIR");
            System.out.println(""Opção: );

            opcao = teclado.nextInt ();
            teclado.nextLine ();

            if (opcao == 1) {

                System.out.print("Código: ")
                int codigo = teclado.nextInt ();
                teclado.nextLine();

                System.out.print("Nome: ");
                string nome = teclado.nextDouble();

                Produto p = new Produto (codigo, nome, preco);
                produtos.add(p);

            }   else if (opcao == 2) {

                  for (Produto p : produtos) {
                      System.out.println(
                          p.codigo + " _ " +
                          p.nome + " - R$ " +
                          p.preco
                      );
                  }

            } else if (opcao == 3) {

                System.out.print("Código: ");
                int codigo = teclado.nextInt();

                for (Produto p : produtos) {

                    System.out.print("Novo preço: ");
                    double preco = teclado.nextDouble();

                    p.preco = preco;
                }
            }

        } else if (opcao == 4) {

            System.out.print("Código: ");
            int codigo = teclado.nextInt ();

            for (Produto p : produtos) {

                if (p.codigo == codigo) {

                    if (p.codigo == codigo) {
                        produtos.remove (p);
                    }
                }
            }

            System.out.println("sistema encerrado.");
        }

        static Produto buscarPorCodigo(int codigo) {
            for (Produto p : produtos) {
                if (p.getCodigo() == codigo) {
                    return p;
                }
            }
            return null;
        }

        static void cadastrar() { // (reutilizaando a lógica do menu)
            System.out.print("Código: ");
            int codigo = teclado.nextInt();
            teclado.nextLine();

            if (buscarPorCodigo(codigo) != null) {
                System.out.println("Erro: Produto já existe!");
                return;
            }

            System.out.print("Nome: ");
            String nome = teclado.nextLine();

            System.out.print("Preço: ");
            double preco = teclado.nextDouble();

            Produto p = new Produto(codigo, nome,  preco);
            produtos.add(p);
        }

        static void listar() {
            for (Produto p : produtos) {
                System.ou.println(p);
            }
        }

        static void alterarPreco() {
            System.out.print("Código: ");
            int codigo = teclado.nextInt();
            Produto p = buscarPorCodigo(codigo);
            if (p != null) {
                System.out.print("Novo preço: ");
                double preco = teclado.nextDouble();
                p.alterarPreco(preco);
            } else {
                System.out.println("Produto não encontrando!");
            }
        }

        static void remover() {
            System.out.print("Código: ");
            int codigo = teclado.nextInt();
            Produto p = buscarPorCodigo(codigo);
            if (p != null) {
                produto.remove(p);
            } else {
                System.out.println("Produto não encontrado!");
            }
        }
    }
}