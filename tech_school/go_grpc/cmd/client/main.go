package main

import (
	"context"
	"flag"
	"log"
	"time"

	"github.com/woong97/grpc_study/tech_school/go_grpc/pb"
	"github.com/woong97/grpc_study/tech_school/go_grpc/sample"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

func main() {
	serverAddress := flag.String("address", "", "the server address")
	flag.Parse()
	log.Printf("dial server %s", *serverAddress)

	conn, err := grpc.Dial(*serverAddress, grpc.WithInsecure())
	if err != nil {
		log.Fatal("cannot dial server: ", err)
	}

	laptopClient := pb.NewLaptopServiceClient(conn)

	laptop := sample.NewLaptop()
	req := &pb.CreateLaptopRequest{
		Laptop: laptop,
	}

	// set timeout
	ctx, cacnel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cacnel()

	res, err := laptopClient.CreateLaptop(ctx, req)
	if err != nil {
		st, ok := status.FromError(err)
		if ok && st.Code() == codes.AlreadyExists {
			log.Print("laptop already exists")
		} else {
			log.Fatal("cannot create laptop: ", err)
		}
		return

	}
	log.Printf("created laptop with id: %s", res.Id)
}
