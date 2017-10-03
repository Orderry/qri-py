Qri Python interface
================================

This is only a part of our infrastructure for easy integration of push notifications between Server-side and Client-side. Our infrastructure are based on [SSE](http://www.w3.org/TR/eventsource/#abstract) interface.
Read more about other Qri components:

1. [SSE server](https://github.com/Orderry/orderry-qri);

Infrastructure
==============

```
 |--------|     |---------|     |--------|
 | Haskel | ... | Clojure | ... | Python | <-- qri-py
 |--------|     |---------|     |--------|
         \           |            /
          \          |           /
        |-------------------------|
        | Erlang SSE Proxy Server |
        |-------------------------|
             |               |
             |               |
       |----------|     |----------|
       | Client_1 | ... | Client_N |
       |----------|     |----------|
```

Installing
==========

```bash
$ pip install qri-py
```

Example
=======

```python
from qri_py import Qri
QRI = Qri(host="127.0.0.1", port=5679)
QRI.send(peer="123", checksum="2008521774", message="Hello, World!")
```
