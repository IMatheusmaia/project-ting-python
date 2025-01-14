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
    basic_results = exists_word(word, instance)
    detailed_results = []

    for result in basic_results:
        file_name = result["arquivo"]
        occurrences = result["ocorrencias"]

        detailed_occurrences = []
        file_meta_data = instance.search(0)
        file_lines = file_meta_data["linhas_do_arquivo"]

        for occurrence in occurrences:
            line_number = occurrence["linha"]
            line_content = file_lines[line_number - 1]
            detailed_occurrences.append({
                "linha": line_number,
                "conteudo": line_content
            })

        detailed_results.append({
            "palavra": word,
            "arquivo": file_name,
            "ocorrencias": detailed_occurrences
        })

    return detailed_results
