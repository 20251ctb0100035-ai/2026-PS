Public class Main {
    public static void main(Strings[] args) {
        int[] valores = {8, 3, 10, 5, 12};

        // Chamara casda metodo a partir do Nome da classe ou metodo
        System.out.println(calculaSoma.executar(valores));
        System.out.println(calculaMedia.executar(valores));
        System.out.println(menorValor.executar(valores));
        System.out.println(maiorValor.executar(valores));
        System.out.println(contarAcima.executar(valores, 6));

        System.out.println("\n--- Exemplos de Percurso");

        // FOR-EACH
        for (int n : valores) {
            System.out.println("For-each: " + n);
        }

        // FOR CLÁSSICO
        for (int i = 0; i < valores.length; i++) {
            System.out.println("For clássico: " + valores[i]);
        }

        // WHILE
        int it = 0;
        while (it < valores.length) {
            System.out.println("While: " + valores[it]);
        }
    }
}