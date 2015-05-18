Qri Python interface

================================

Example
=======

```python
from qri_py import QriPython
QRI = QriPython(host="127.0.0.1", port=5679)
QRI.send(peer="123", checksum="2008521774", message="Hello, World!")
QRI.close()
```
