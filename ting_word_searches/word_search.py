def exists_word(word, instance):
    results = []

    for index in range(len(instance)):
        file_meta_data = instance.search(index)
        file_name = file_meta_data["nome_do_arquivo"]
        file_lines = file_meta_data["linhas_do_arquivo"]

        occurrences = [
            {"linha": line_num + 1}
            for line_num, line in enumerate(file_lines)
            if word.lower() in line.lower()
        ]

        if occurrences:
            results.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            })

    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
