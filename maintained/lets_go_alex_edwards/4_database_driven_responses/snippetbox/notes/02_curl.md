```bash
# Request a specific byte range (100–199) from the file
$ curl -i -H "Range: bytes=100-199" --output - http://localhost:4000/static/img/logo.png
```
```yml
HTTP/1.1 206 Partial Content
Accept-Ranges: bytes
Content-Length: 100
Content-Range: bytes 100-199/1075
Content-Type: image/png
Last-Modified: Thu, 04 May 2017 13:07:52 GMT
Date: Sat, 29 Jan 2022 14:33:59 GMT
[binary data]
```

---

# first, request the file normally and note the Last-Modified

```bash
# First, request the file normally and note the Last-Modified header
$ curl -i http://localhost:4000/static/img/logo.png
```

```yml
HTTP/1.1 200 OK
Content-Type: image/png
Content-Length: 1075
Last-Modified: Thu, 04 May 2017 13:07:52 GMT
Date: Sat, 29 Jan 2022 14:35:10 GMT
[binary data]
```

---

```bash
# Now request again with If-Modified-Since set to the Last-Modified value
$ curl -i -H "If-Modified-Since: Thu, 04 May 2017 13:07:52 GMT" \
    http://localhost:4000/static/img/logo.png
```

```yml
HTTP/1.1 304 Not Modified
Date: Mon, 09 Sep 2025 10:32:00 GMT
```

---

✅ This shows the difference:

- **200 OK** → full file sent.
    
- **206 Partial Content** → only a byte range sent.
    
- **304 Not Modified** → no file sent, client should use cached copy.
