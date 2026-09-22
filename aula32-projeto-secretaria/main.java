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
            System.out.println("[3] Buscar por matricula");
            System.out.println("[5] Remover aluno");
            System.out.println("[6] Relatorio");
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
            } else if (opcao.equals("3")) {
                buscar(lista, teclado);
            } else if (opcao.equals("4")) {
                atualizar(lista, teclado);
            } else if (opcao.equals("5")) {
                remover(lista, teclado);
            } else if (opcao.equals("3")) {
                relatorio(lista, teclado);
            } else{
                System.out.println("Opcao invalida! Vale 0, 1, 2, 3, 4, 5, ou 6.");
            }
        }
    }

    static Aluno buscarPorMatricula(ArrayList<Aluno> lista, String matricula) {
        for (int i = 0; i < lista.size(); i++) {
            Aluno a = lista.get(i);
            if (a.getMatricula().equalsIgnoreCase(matricula)) {
                return a;
            }
        }
        return null;
    }

    static void cadastrar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matricula: ");
        String matricula = teclado.nextLine().trim();

        if (buscarPorMatricula(lista, matricula) != null) {
            System.out.println("Ja exite ficha com matricula " + matricula + "!")
            return;
        }

        System.out.print("Nome: ");
        String nome = teclado.nextLine().trim();
        
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

        System.out.println("--- FICHAS NO GAVETEIRO: " + lista.size() +" ---");
        for (int i = 0; i < lista.size(); i++) {
            Aluno a = lista.get(i);
            System.out.println(a);
        }
    }

    static void buscar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matricula procurado: ");
        String matricula = teclado.nextLine().trim();

        Aluno a = buscarPorMatricula(lista, matricula);

        if (a == null) {
            System.out.println("Nenhuma ficha com a matricula " + matricula + ".");
        } else {
            System.out.println("Achei: " + a);
        }
    }

    static void atualizar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matricula da ficha a atualizar: ");
        String matricula = teclado.nextLine().trim();

        Aluno a = buscarPorMatricula(lista, matricula);

        if (a == null) {
            System.out.println("Nenhuma ficha com matricula " + matricula + ".");
        } else {
            System.out.print("Novo curso de " + a.getNome + ": ");
            String novoCurso = teclado.nextLine().trim();
            a.setCurso(novoCurso);
            System.out.println("Ficha atualizado: " + a);
        }
    }

    static void remover(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matricula da ficha a remover: ");
        String matricula = teclado.nextLine().trim();

        Aluno a = buscarPorMatricula(lista, matricula);

        if (a == null) {
            System.out.println("Nenhuma ficha com a matricula " + matricula + ".");
        } else {
            System.out.print("Tem certeza que remove " + a.getNome() + "? (s/n): ");
            String resp = teclado.nextLine().trim().toLowerCase();

            if (resp.equals("s")) {
                lista.remove;
                System.out.println("Ficha removida.");
            } else {
                System.out.println(Remocao cancelada)
            }
        }
    }

    static void relatorio(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.println("--- RELATORIO DA SECRETA ---");
        System.out.println("Total de fichas: " + lista.size());

        int contador = 0; //iniciador

        for (int i = 0; i < lista.size(); i++) {
            Aluno a = lista.get(i);
            if (a.getCurso().equalsIgnoreCase(cursoProcurado)) {
                contador++;
            }
        }

        System.out.println("Alunos de " + cursoProcurado + ": ");
    }
}