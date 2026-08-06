Public class contarAcima {
    public static int executar(int [] numeros, int limite) {
        int quantidade = 0;
        for (int i = 0; i < numeros.length; i++) {
            if (numeros[i] > limite) {
                quantidade++;
            }
        }
        return quantidade;
    }
}