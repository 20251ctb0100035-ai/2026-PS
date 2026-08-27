/*
 * Disciplina   : 2026 - PS
 * Estudante    : Anthony Pagani
 * Data         : 20/08/2026
 * Projeto      : aula32-projeto-secretaria
 * Arquivo      : Aluno.java
*/

import java.util.ArrayList;
import java.util.Scanner;

public class main {
    
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        ArrayList<Aluno> lista = new ArrayList<Aluno>();

        while (true) {
            System.out.println("===================================");
            System.out.println("    SECRETARIA DO SEU NOME");
            System.out.println("===================================");
            System.out.println("[1] Cadastrar aluno");
            System.out.println("[2] Listar aluno");
            System.out.println("[0] Sair");
            System.out.print("Sua escolha: ");
            String opcao = teclado.nextLine().trim();

            if (opcao.equals("0")) {
                System.out.println("Secretaria fechada. Ate a proxima!");
                break;
            } else if (opcao.equals("1")) {
                cadastrar(lista, teclado);
            } else if (opcao.equals("2")) {
                listar(lista);
            } else{
                System.out.println("Opcao invalida! Vale 0, 1 ou 2");
            }
        }
    }

    static void cadastrar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Nome: ");
        String nome = teclado.nextLine().trim();

        System.out.print("Matricula: ");
        int Matricula = teclado.nextLine().trim();
        
        System.out.print("Curso: ");
        String Curso = teclado.nextLine().trim();

        Aluno novoAluno = new Aluno(nome, matricula, curso);
        lista.add(novoAluno);

        System.out.println("Aluno Cadastrado com sucesso!");
    }

    static void listar(ArrayList<Aluno> lista) {
    if (list.size() == 0) {
        System.out.println("nenhum guardado");
        return;
    }
    System.out.println(a.getMatricula() + " | " + agetNome() + " | " + a.getCurso());
    for (int i = 0; i < lista.size(); i++) {
        Aluno a = list.get(i);
    }
    }
}