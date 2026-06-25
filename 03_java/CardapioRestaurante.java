import java.util.Scanner;

public class CardapioRestaurante { // Em Java, se a classe for pública, o nome do arquivo precisa ser igual ao nome da classe.

    public static void main(String[] args) { // metodo Main

        Scanner entrada = new Scanner (System.in); // permiti que o usuário escolha um item do cardápio.

        System.out.println("================================");
        System.out.println("          PAGA E COME           ");
        System.out.println("================================");
        System.out.println("     CARDÁPIO ELETRÔNICO");
        System.out.println("================================");
        System.out.println("1 - X-Burguer ......... R$ 18,00");
        System.out.println("2 - Pizza ............. R$ 35,00");
        System.out.println("3 - Suco Natural ...... R$ 8,00");
        System.out.println("4 - Café .............. R$ 5,00");
        System.out.println("5 - Refrigerante ...... R$ 5,00");
        System.out.println("6 - Bolo de chocolate . R$ 35,00");
        System.out.println("================================");

        System.out.print("Quantos itens você deseja escolher? ");
        int quantidade = entrada.nextInt();

            int opcao = entrada.nextInt();

            if (opcao == 1) {
                System.out.println("Você escolheu X-Burguer.");
            } else if (opcao == 2) {
                System.out.println("Você escolheu Pizza.");
            } else if (opcao == 3) {
                System.out.println("Você escolheu Suco Natural.");
            } else if (opcao == 4) {
                System.out.println("Você escolheu Café.");
            } else if (opcao == 5) {
                System.out.println("Você escolheu Refrigerante.");
            } else if (opcao == 6) {
                System.out.println("Você escolheu Bolo de chocolate.");
            } else {
                System.out.println("Opção inválida.");
            }
        }

        // fecha o Scanner quando já for selecionada a quantidade desejada antes de encerrar o programa
        entrada.close();
    }
}