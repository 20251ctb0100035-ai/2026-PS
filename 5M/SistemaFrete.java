public class SistemaFrete {
    // se for <= 1 dara 10.00 mas se for <= 5 o preco dara 20.00 e por ultimo 35 se for aind mais alto
    static double calcularFrete(double peso) {
        if (peso <= 1) {
            return 10.00;
        } else if (peso <= 5) {
            return 20.00;
        } else {
            return 35.00;
        }
    }

    public static void main(String[] args){
        double resultado = calcularFrete(0.5);

        System.out.println("R$" + resultado);
    }
}
