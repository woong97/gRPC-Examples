gen:
	protoc --proto_path=proto --go_out . --go-grpc_out ./pb --go-grpc_opt=require_unimplemented_servers=false --go-grpc_opt paths=source_relative proto/*.proto

clean:
	rm pb/*

server1:
	go run cmd/server/main.go -port 50051

server2:
	go run cmd/server/main.go -port 50052

server1-tls:
	go run cmd/server/main.go -port 50051 -tls

server2-tls:
	go run cmd/server/main.go -port 50052 -tls

client:
	go run cmd/client/main.go -address 0.0.0.0:8080

client-tls:
	go run cmd/client/main.go -address 0.0.0.0:8080 -tls

test:
	go test -cover -race ./...

cert:
	cd cert; bash gen.sh; cd ..

.PHONY: gen clean server client test cert