# gRPC Messaging Application

This gRPC Messaging Application is a simple powerful demonstration of a client-server architecture using gRPC and Protocol Buffers. I created it to learn and play around with gRPC in python.

## Features

- **gRPC Implementation**
- **Protocol Buffers**: Uses Protocol Buffers for message serialization, providing a lightweight and cross-platform method for structuring data.


### Prerequisites

- Python 3.6 or higher
- gRPC Python Package
- Protocol Buffers Compiler (`protoc`)

### Installation
1. **Clone the repository**

    ```bash
    git clone https://github.com/piolad/grpcLanMessanger.git
    cd grpcLanMessanger
    ```
2. **Set up a Python virtual environment**
    ```bash
    python3 -m venv venv      
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements. txt
    ```

4. **Start the Server**
    ``
    python3 message_server.py
    ``

5. **Start the client**
    >if you want to try LAN connectivity a different PC, modify **SERVER_IP** in *message_client.py*:
    >```bash
    >SERVER_IP = "LOACLHOST" # set this to server's LAN ip
    >```

    ``
    python3 message_server.py
    ``