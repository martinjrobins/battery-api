# to generate client

```bash
source generate_client.sh
```

Then need to add the following to `client/batteryclient/model_utils.py`, line 1633:

```python
    if isinstance(model_instance, dict):
        return model_instance
```
