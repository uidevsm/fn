import socket
import logging
import time
import argparse

# إعداد تسجيل الأحداث (Logging)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_socket():
    """إنشاء مقبس TCP جديد"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.info("Socket successfully created.")
        return s
    except socket.error as err:
        logging.error(f"Socket creation failed with error {err}")

def connect_to_server(s, server_ip, server_port, retries=3, delay=5):
    """الاتصال بالخادم مع محاولات متعددة"""
    for attempt in range(retries):
        try:
            s.connect((server_ip, server_port))
            logging.info(f"Connected to {server_ip} on port {server_port}.")
            return True
        except socket.error as err:
            logging.warning(f"Connection attempt {attempt + 1} failed: {err}. Retrying in {delay} seconds...")
            time.sleep(delay)
    logging.error(f"Failed to connect to {server_ip} on port {server_port} after {retries} attempts.")
    return False

def send_minecraft_packet(s, packet_data):
    """إرسال الحزمة واستقبال الرد"""
    try:
        s.sendall(packet_data)
        logging.info(f"Packet sent: {len(packet_data)} bytes")
        response = s.recv(1024)
        logging.info(f"Response received: {response}")
        return response
    except socket.error as err:
        logging.error(f"Failed to send/receive data: {err}")
        return None

def close_socket(s):
    """إغلاق المقبس TCP"""
    try:
        s.close()
        logging.info("Socket successfully closed.")
    except socket.error as err:
        logging.error(f"Failed to close socket: {err}")

def main(server_ip, server_port, packet_data):
    """الدالة الرئيسية لتنفيذ العملية"""
    s = create_socket()
    if not s:
        return

    if connect_to_server(s, server_ip, server_port):
        response = send_minecraft_packet(s, packet_data)
        if response:
            logging.info(f"Final response: {response}")
        close_socket(s)
    else:
        logging.error("Failed to establish a connection to the server.")

if __name__ == "__main__":
    # استخدام argparse لإدخال القيم من سطر الأوامر
    parser = argparse.ArgumentParser(description="Minecraft Packet Sender")
    parser.add_argument("-ip", type=str, help="Server IP address")
    parser.add_argument("-p", type=int, help="Server port number")
    args = parser.parse_args()

    # إذا لم يتم توفير IP أو Port، يُطلب من المستخدم إدخالها
    SERVER_IP = args.ip if args.ip else input("Enter the server IP: ")
    SERVER_PORT = args.p if args.p else int(input("Enter the server port: "))

    # إنشاء بيانات بحجم 1 ميجابايت (1024 * 1024 بايت)
    PACKET_DATA = b'\x00' * (1024 * 1024)  # 1MB من البيانات

    retries = int(input("Enter the number of connection retries: "))
    delay = int(input("Enter the delay between retries (seconds): "))

    logging.info("Starting Minecraft packet sender...")

    main(SERVER_IP, SERVER_PORT, PACKET_DATA)
    
    logging.info("Minecraft packet sender finished.")