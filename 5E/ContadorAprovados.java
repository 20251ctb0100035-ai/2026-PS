public class ContadorAprovados {
static int contarAprovados(double[] notas, double limite) {
    int quantidade = 0;
    for (double n : notas) {
        if (n >= limite) {
            quantidade = quantidade + 1;
        }
    }
    return quantidade;
}

public static void main(String[] args) {
double[] valores = {7.0, 4.0, 9.0, 6.0};
System.out.println(contarAprovados(valores, 6.0));

double[] valores1 = {2.0, 3.0, 5.0};
System.out.println(contarAprovados(valores1, 6.0));

double[] valores2 = {10.0, 8.0, 6.0};
System.out.println(contarAprovados(valores2, 6.0));

}

}