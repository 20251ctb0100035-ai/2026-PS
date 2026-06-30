public class BoletimIntegrador {

    public static double calcularMedia(double[] notas) {
        double soma = 0;
        for (double nota : notas) {
            soma += nota;
        }
        return soma / notas.length;
    }

    public static int contarAprovados(double[] notas) {
        int aprovados = 0;
        for (double nota : notas) {
            if (nota >= 6.0) {
                aprovados++;
            }
        }
        return aprovados;
    }

    public static void exibirBoletim(double[] notas) {
        double media = calcularMedia(notas);
        int aprovados = contarAprovados(notas);
        String situacao = (media >= 6.0) ? "APROVADA" : "EM RECUPERAÇÃO";

        System.out.println("Média: " + media);
        System.out.println("Aprovados: " + aprovados);
        System.out.println("Situação: " + situacao);
        System.out.println(); // Linha em branco para separar os testes
    }

    public static void main(String[] args) {
        // Teste 1
        double[] turma1 = {7.0, 5.0, 9.0, 6.0};
        exibirBoletim(turma1);

        // Teste 2
        double[] turma2 = {4.0, 3.0, 5.0};
        exibirBoletim(turma2);
    }
}