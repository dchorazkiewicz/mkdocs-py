import re
import yaml
import textwrap

class add:
    """
    Dokumentacja

        sdsdsd
        sdsdsd
        sdsds

    Lista:
        - a
        - b
        - c
    
    Oto konfiguracja YAML dla przykładowej klasy:

    ```yaml
    name: ExampleClass
    version: 1.0
    description: To jest przykład klasy.
    params:
      - name: param1
        type: int
        description: Pierwszy parametr
      - name: param2
        type: str
        description: Drugi parametr
    ```
    """

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        self.doc_yaml = self._extract_yaml_from_docstring()

    def _extract_yaml_from_docstring(self):
        """
        Wyciąga YAML z docstringa klasy i zwraca sparsowany słownik.
        """
        docstring = self.__class__.__doc__
        if docstring:
            docstring = textwrap.dedent(docstring)  # Usunięcie wcięć
            print("Oczyszczony docstring:")
            print(repr(docstring))  # Do debugowania

            # Szukamy bloku YAML
            pattern = r"```yaml\n(.*?)\n```"
            match = re.search(pattern, docstring, re.DOTALL)

            if match:
                yaml_block = match.group(1)
                try:
                    return yaml.safe_load(yaml_block)
                except yaml.YAMLError as e:
                    print(f"Błąd parsowania YAML: {e}")
            else:
                print("Nie znaleziono bloku YAML w docstringu.")
        else:
            print("Docstring jest pusty.")
        return None

# Tworzenie instancji i sprawdzenie wyniku
instance = add(10, "test")
print(instance.doc_yaml)
