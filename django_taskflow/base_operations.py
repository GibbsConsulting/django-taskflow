"""BAse operations, in a model-instance free manner

This permits use from inside migrations.
"""


_OPERATIONS = [
    {
        'name': '__init',
        'slug': '__init',
        'description': 'Task initialisation at the beginning of a ticket process',
        'function': 'django_taskflow.operations.Init',
    },
    {
        'name': 'Script',
        'slug': 'script',
        'description': 'Run a processing step',
        'function': 'django_taskflow.operations.Script',
    },
    {
        'name': 'External Task',
        'slug': 'external-task',
        'description': 'External processing step',
        'function': 'django_taskflow.operations.OperatorExternalTask',
    },
]


def forward(apps, schema_editor):
    Operation = apps.get_model('django_taskflow', 'Operation')
    for ops in _OPERATIONS:
        op = Operation(**ops)
        op.save()


def backward(apps, schema_editor):
    Operation = apps.get_model('django_taskflow', 'Operation')
    for obj in Operation.objects.all():
        obj.delete()


