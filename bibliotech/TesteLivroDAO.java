public class TesteLivroDAO {

    public static void main(String[] args) {

    LivroDAO dao = new LivroDAO();

    System.out.println("Insercao");
    dao.adicionarLivro("Dom Casmurro", "Machado de Assis", 1899);
    dao.adicionarLivro("O Cortiço", "Aluísio Azevado", 1890);
    dao.adicionarLivro("Grande Sertão: Veredas", "João Guimarães Rosa", 1956);
    System.out.println("três livros foram cadastrados");

    System.out.println("Atualização e Exclusão");
    int IDAtualizar = 1;
    int IDExcluir = 2;

    atualizarLivro(IDAtualizar, "Dom Casmurro - speciel edition", "Machado de Assis", 1899);
    excluirLivro(IDExcluir);

    System.out.println("Teste adicional — Registro inexistente");
    boolean atualizou = dao.atualizarLivro(
        999999,
        "Livro Inexistente",
        "Autor Desconhecido",
        2026
    );

    boolean excluiu = dao.excluirLivro(999999);

    System.out.println("Atualização: " + atualizou);
    System.out.println("Exclusão: " + excluiu);
}
}
