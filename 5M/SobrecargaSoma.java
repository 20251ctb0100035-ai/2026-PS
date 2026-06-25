public class SobrecargaSoma {

    static int somar(int a, int b){
        return a+b;
    }

    static double somar(double a, double b){
        return a+b;
    }

    public static void main(String[] args){
        double resultado = somar(2.5,3.5);

        System.out.println(resultado);
    }
}