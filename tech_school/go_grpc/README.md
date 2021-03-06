
## VS Code settings
To get rid of red line for 'import' in proto file,
- Go Code -> Preference -> Settings
- Search Protoc, and edit settins.json so that it has this filed.
```
"protoc": {
    "path": "/usr/local/bin/protoc",
    "options": [
        "--proto_path=proto"
    ]
}
```
## Install Environment
```
$ brew install protobuf
$ go mod init github.com/{github id}/{repository}
$ go get google.golang.org/protobuf/cmd/protoc-gen-go@v1.26
$ go get google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.1
$ export PATH="$PATH:$(go env GOPATH)/bin"
```

### Nginx
- Copy cert directory to /usr/local/etc/nginx (nginx.conf existed in this directory)
- You should modify nginx.conf as I copied to this repository
- run command: nginx
- stop command: nginx -s stop
- log will be saved in /usr/local/var/log/nginx/error.log

## How to run
```
$ make server1-tls
$ make server2-tls
$ nginx
$ make client-tls
```
