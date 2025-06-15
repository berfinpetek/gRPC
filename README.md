# gRPC
# 📚 University Library System with gRPC

This project is a gRPC-based client-server application designed to manage an online library system for a university. It demonstrates the use of Protocol Buffers (`.proto`) to define APIs and implement services for managing books, students, and loan operations.

## 🚀 Features

- **Books Management**: List, view details, add, update, and delete books.
- **Students Management**: List, view details, add, update, and delete student records.
- **Loans Management**: List loans, borrow books, return books, and check loan status.

## 🛠️ Tech Stack

- **Protocol Buffers**: `.proto` file to define services and messages.
- **gRPC**: Communication between client and server.
- **Python**: Server and client implementation.

## 📋 Prerequisites

- Python 3.8+
- `grpcio` and `grpcio-tools` Python packages
- `grpcurl` for testing (optional)

## 📂 Project Structure

```plaintext
/
├── university.proto       # Protocol Buffers definition file
├── README.md              # Project documentation
├── grpcurl-tests.md       # grpcurl test documentation
├── server.py              # gRPC server implementation
├── client.py              # gRPC client implementation
└── requirements.txt       # Python dependencies
