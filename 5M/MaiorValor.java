public class MaiorValor {

    static int maiorNumero(int a, int b) {
        if  (a > b) {
            return a;
        } else {
            return b;
        }
    }

public static void main(String[] args){
    int resultado = maiorNumero(50,5);

    System.out.println(resultado);
    }
}
