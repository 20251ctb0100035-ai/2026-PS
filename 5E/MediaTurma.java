public class MediaTurma {
static double calcularMedia(double[] numeros) {
    double total = 0;
    for (int i = 0; i < numeros.length; i++) {
        total = total + numeros[i];
    }
    return total / numeros.length;
}

public static void main(String[] args) {
double[] valores = {7.0, 8.0, 9.0};
System.out.println(calcularMedia(valores));

double[] valores1 = {6.0, 6.0, 6.0, 6.0};
System.out.println(calcularMedia(valores1));

double[] valores2 = {5.0, 10.0};
System.out.println(calcularMedia(valores2));
}

}