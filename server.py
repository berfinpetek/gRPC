import grpc
from concurrent import futures
import university_pb2
import university_pb2_grpc


class BookService(university_pb2_grpc.BookServiceServicer):
    def ListBooks(self, request, context):
        books = [
            university_pb2.Book(
                id="1", title="Python 101", author="John Doe", isbn="1234567890123",
                publisher="TechBooks", pageCount=200, stock=10
            ),
        ]
        for book in books:
            yield book


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    university_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
