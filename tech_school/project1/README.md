```
$ go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.26
$ go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.1
$ protoc --proto_path=proto proto/*.proto --go_out=pb --go_opt=Mproto/processor_message.proto=github.com/woong97/grpc_study/tech_school/project1
```