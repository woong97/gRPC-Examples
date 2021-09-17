clean:
	rm pb/*

gen:
	protoc --proto_path=proto --go_out . --go-grpc_out . --go-grpc_opt paths=source_relative proto/*.proto

run:
	go run main.go
