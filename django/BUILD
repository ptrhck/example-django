python_sources()

pex_binary(
    name="manage",
    entry_point="manage.py",
)

__defaults__({
      (python_test): dict(dependencies=["django/mysite/settings.py"])
    })