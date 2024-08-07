import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        processed_file = instance.search(i)
        if path_file == processed_file["nome_do_arquivo"]:
            return

    file_content = txt_importer(path_file)
    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content,
    }

    instance.enqueue(file_info)
    sys.stdout.write(f"{file_info}\n")


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        files = instance.dequeue()
        print(f"Arquivo {files['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(file)
    except IndexError:
        sys.stderr.write("Posição inválida")
