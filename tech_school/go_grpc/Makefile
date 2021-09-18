clean:
	rm pb/*

gen:
	protoc --proto_path=proto --go_out . --go-grpc_out ./pb --go-grpc_opt=require_unimplemented_servers=false --go-grpc_opt paths=source_relative proto/*.proto

server:
	go run cmd/server/main.go -port 8080

client:
	go run cmd/client/main.go -address localhost:8080

test:
	go test -cover -race ./...