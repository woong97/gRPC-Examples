
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
$ go mod init pb
$ go get google.golang.org/protobuf/cmd/protoc-gen-go@v1.26
$ go get google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.1
$ export PATH="$PATH:$(go env GOPATH)/bin"
```

## Run
```
$ make gen
```
