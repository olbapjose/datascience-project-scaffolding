import sys

from my_package.jobs.eda_job import main_eda
from my_package.jobs.features_creation_job import main_features_creation
from my_package.jobs.train_productivize_job import main_train_productivize
from my_package.jobs.predict_job import main_predict


def main(
    job_name,
    properties_path
):
    """
    :param job_name: name associated to the job. Must be one of the jobs defined in the job names dictionary
    :param properties_path: properties json path
    """

    job_args = {
        "properties_path": properties_path,
    }

    job_functions = {
        # Las claves deben coincidir con el argumento que le pasamos desde la línea de comandos al ejecutar
        # Los valores son los objetos función que queremos invocar
        "eda": main_eda,
        "features_creation": main_features_creation,
        "train_productivize": main_train_productivize,
        "predict": main_predict
    }

    f = job_functions.get(job_name, None)
    if not f:
        print("Job name invalid!!")

    else:
        f(**job_args)   # invocamos a la función correspondiente

if __name__ == "__main__":

    if len(sys.argv) < 3:
        # sys.argv[0] siempre es el nombre del propio fichero main_job así que no sirve para nada
        print("Error: se necesitan al menos 2 argumentos indicando el job y el path del JSON de properties")

    # El primer argumento es el job que queremos ejecutar, y el segundo el path al JSON de properties
    # Ejemplos de ejecución desde la terminal de Windows:
    # python mypackage/jobs/main_jobs eda config/project_config.json
    # python mypackage/jobs/main_jobs features_creation config/project_config.json

    job_name = sys.argv[1]
    properties_path = sys.argv[2]
    # Otros posibles argumentos estarán en sys.argv[2], sys.argv[3], etc, si fueran necesarios
    main(job_name, sys.argv[2])
