import grpc
import university_pb2
import university_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = university_pb2_grpc.BookServiceStub(channel)
        for book in stub.ListBooks(university_pb2.Empty()):
            print(f"Book: {book.title}, Author: {book.author}")


if __name__ == "__main__":
    run()
