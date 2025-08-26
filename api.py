from flask import Flask, request, jsonify
import socket
from datetime import datetime

app = Flask(__name__)

# Configure the TCP server
server_host = "127.0.0.1"  # Replace with your server's IP
server_port = 1234

@app.route('/tp/post_data_tp', methods=['POST'])
def post_data_tp():
    print('post_data_tp')
    data = request.json
    print('Body', data)

    hn = data.get('hn','') or ''
    cid = data.get('cid','') or ''
    vn = data.get('vn','') or ''
    _dt = datetime.now().strftime("%Y%m%d%H%M%S")

    tp = data['data']['tp']
    hl7_message = (
        f"MSH|^~\\&|Device01|SMARTCONNECT|HIS|Hospital-OS|{_dt}||ORU^R01|MSGID101|P|2.3\n"
        f"PID|1||{hn}|{cid}\n"
        f"PV1||O|||{vn}||||||||||||||\n"
        f"OBR|1|||||{_dt}||||||||{_dt}\n"
        f"OBX|1|ST|TEMP||{tp}||||||F|||{_dt}\n"
    )
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_host, server_port))
        print(f"Connected to {server_host}:{server_port}")
        client_socket.sendall(hl7_message.encode())
        print("sent HL7 to the socket server.")
        response = client_socket.recv(1024)  # Buffer size
        print(f"Received from tcp server: {response}")

    except ConnectionError as e:
        print(f"Connection error: {e}")
    finally:
        client_socket.close()
        print("Connection closed")

    return jsonify({'status':'ok'}), 200



@app.route('/bp/post_data_bp_list', methods=['POST'])
def post_data_bp_list():
    print('post_data_bp_list')
    return jsonify({'status': 'ok'}), 200
@app.route('/bp/post_data_bp', methods=['POST'])
def post_data_bp():
    print('post_data_bp')
    data = request.json
    print('Body', data)

    hn = data.get('hn', '') or ''
    cid = data.get('cid', '') or ''
    vn = data.get('vn', '') or ''
    _dt = datetime.now().strftime("%Y%m%d%H%M%S")

    bps = data['data']['bps']
    bpd = data['data']['bpd']
    pulse = data['data']['pulse']
    hl7_message = (
        f"MSH|^~\\&|Device01|SMARTCONNECT|HIS|Hospital-OS|{_dt}||ORU^R01|MSGID101|P|2.3\n"
        f"PID|1||{hn}|{cid}\n"
        f"PV1||O|||{vn}||||||||||||||\n"
        f"OBR|1|||||{_dt}||||||||{_dt}\n"
        f"OBX|1|ST|SYSTOLIC||{bps}||||||F|||{_dt}\n"
        f"OBX|2|ST|DIASTOLIC||{bpd}||||||F|||{_dt}\n"
        f"OBX|3|ST|PUหหหหหLSE||{pulse}|bpm|||||F|||{_dt}"
    )
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_host, server_port))
        print(f"Connected to {server_host}:{server_port}")
        client_socket.sendall(hl7_message.encode())
        print("sent HL7 to the socket server.")
        response = client_socket.recv(1024)  # Buffer size
        print(f"Received from tcp server: {response}")

    except ConnectionError as e:
        print(f"Connection error: {e}")
    finally:
        client_socket.close()
        print("Connection closed")

    return jsonify({'status': 'ok'}), 200


@app.route('/bmi/post_data_bmi', methods=['POST'])
def post_data_bmi():
    print('post_data_bmi')
    data = request.json
    print('Body', data)

    hn = data.get('hn', '') or ''
    cid = data.get('cid', '') or ''
    vn = data.get('vn', '') or ''
    _dt = datetime.now().strftime("%Y%m%d%H%M%S")

    height = data['data']['height']
    weight = data['data']['weight']
    bmi = data['data']['bmi']
    hl7_message = (
        f"MSH|^~\\&|Device01|SMARTCONNECT|HIS|Hospital-OS|{_dt}||ORU^R01|MSGID101|P|2.3\n"
        f"PID|1||{hn}|{cid}\n"
        f"PV1||O|||{vn}||||||||||||||\n"
        f"OBR|1|||||{_dt}||||||||{_dt}\n"
        f"OBX|6|ST|HEIGHT||{height}|cm|||||F|||{_dt}\n"
        f"OBX|7|ST|WEIGHT||{weight}|kg||||||F|||{_dt}\n"
        f"OBX|8|ST|BMI||{bmi}|kg/m2|||||F|||{_dt}"
    )
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_host, server_port))
        print(f"Connected to {server_host}:{server_port}")
        client_socket.sendall(hl7_message.encode())
        print("sent HL7 to the socket server.")
        response = client_socket.recv(1024)  # Buffer size
        print(f"Received from tcp server: {response}")

    except ConnectionError as e:
        print(f"Connection error: {e}")
    finally:
        client_socket.close()
        print("Connection closed")

    return jsonify({'status': 'ok'}), 200

@app.route('/patient/get_patient_by_hn/<hn>', methods=['GET'])
def get_hn(hn):
    data = {
        'hn': hn,
        'cid': '',
        'fullname': hn,
        'sex': 1,
        'vn': '',
        'birth': '1980-04-18'
    }

    return jsonify(data),200

@app.route('/patient/get_patient_by_vn/<vn>', methods=['GET'])
def get_vn(vn):
    data = {
        'hn': '',
        'cid': '',
        'fullname': vn,
        'sex': 1,
        'vn': vn,
        'birth': '1980-04-18'
    }

    return jsonify(data),200

@app.route('/patient/get_patient_by_cid/<cid>', methods=['GET'])
def get_cid(cid):
    data = {
        'hn': '',
        'cid': cid,
        'fullname': cid,
        'sex': 1,
        'vn': '',
        'birth': '1980-04-18'
    }

    return jsonify(data),200


@app.route('/patient/get_patient_by_an/<an>', methods=['GET'])
def get_an(an):
    data = {
        'hn': '',
        'cid': '',
        'fullname': an,
        'sex': 1,
        'an':an,
        'birth': '1980-04-18'
    }

    return jsonify(data),200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
