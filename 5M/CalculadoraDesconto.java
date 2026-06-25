public class CalculadoraDesconto {
    static double calcularDesconto(double valor, double percentual){
       double desconto = valor * (percentual / 100.0);
        double total = valor - desconto;
        return (int) total;
    }

public static void main(String[] args){
    double resultado = calcularDesconto(500,15);

        System.out.println(resultado);
    }
}