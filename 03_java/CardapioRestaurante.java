import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int precoTotal = 0;
        boolean Pedido = true;    
        String itens = "";

        while (Pedido) {
            System.out.println("================================");
            System.out.println("Bem-vindo a loja food!");
            System.out.println("================================");
            System.out.println("1 - X-Burguer ......... R$ 18,00");
            System.out.println("2 - Pizza ............. R$ 35,00");
            System.out.println("3 - Suco Natural ...... R$ 8,00");
            System.out.println("4 - Café .............. R$ 5,00");
            System.out.println("5 - Refrigerante ...... R$ 5,00");
            System.out.println("6 - Bolo de chocolate . R$ 35,00");
            System.out.println("7 - Finalizar Pedido");
            System.out.println("================================");
            System.out.print("Escolha uma opção: ");

            int opcao = entrada.nextInt();

            switch (opcao) {
                case 1:
                    System.out.println("Você escolheu X-Burguer.");
                    precoTotal += 18;
                    itens += "X-Burguer\n";
                    break;
                case 2:
                    System.out.println("Você escolheu Pizza.");
                    precoTotal += 35;
                    itens += "Pizza\n";
                    break;
                case 3:
                    System.out.println("Você escolheu Suco Natural.");
                    precoTotal += 8;
                    itens += "Suco Natural\n";
                    break;
                case 4:
                    System.out.println("Você escolheu Café.");
                    precoTotal += 5;
                    itens += "Café\n";
                    break;
                case 5:
                    System.out.println("Você escolheu Refrigerante.");
                    precoTotal += 5;
                    itens += "Refrigerante\n";
                    break;
                case 6:
                    System.out.println("Você escolheu Bolo de chocolate.");
                    precoTotal += 35;
                    itens += "Bolo de chocolate\n";
                    break;
                case 7:
                    System.out.print("Deseja finalizar o pedido (S/N)? ");
                    String resposta = entrada.next();
                    if (resposta.equalsIgnoreCase("S")) {
                        Pedido = false;
                    } else if (resposta.equalsIgnoreCase("N")) {
                        System.out.println("Continuando com o pedido...");
                    } else {
                        System.out.println("Resposta inválida. Por favor, responda com 'S' ou 'N'.");
                    }
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
                    break;
            }
        }

        System.out.println("Pedidos adicionados: " + itens); // mostrar os pedidos escolhidos
        System.out.println("Valor total do pedido: R$ " + precoTotal + ",00");
        System.out.println("Escolha a forma de pagamento: 1 - Dinheiro, 2 - Cartão, 3 - Pix");
        int formaPagamento = entrada.nextInt();
        switch (formaPagamento) {
            case 1:
                System.out.println("Pagamento em dinheiro selecionado.");
                break;
            case 2:
                System.out.println("Pagamento em cartão selecionado.");
                break;
            case 3:
                System.out.println("Pagamento em pix selecionado.");
                break;
            default:
                System.out.println("Opção inválida.");
                break;
        }

        System.out.println("Pagamento realizado com sucesso. Número do pedido: (" + (int) (Math.random() * 100) + "). Aguarde a chamada do seu pedido.");
        entrada.close();
    }
}

