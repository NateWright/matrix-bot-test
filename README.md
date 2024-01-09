### Get auth token

```bash
curl -XPOST   -d '{"type":"m.login.password", "user":"natebot", "password":"pass"}'   "https://matrix.nwright.tech/_matrix/client/r0/login"
```