python_sources()

pex_binary(
    name="manage",
    entry_point="manage.py",
)

__defaults__({
      (python_tests): dict(dependencies=["django/mysite/settings.py"])
    })